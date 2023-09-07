from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView, DetailView
from django_filters.views import FilterView
from store.filters import StoreFilter
from store.forms import ImageForm, StoreForm, HourFormset
from store.models import Image, Store
from user.models import User


class Index(TemplateView):
    """
    This view is used to display index page.
    """
    template_name = 'index.html'


class ImageCreateView(LoginRequiredMixin, CreateView):
    """
    This view is used to create image using image form.
    """
    form_class = ImageForm
    success_url = reverse_lazy('store:my_store_list')

    def post(self, request, *args, **kwargs):
        """
        This method should check whether form is valid or not.
        """
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)

    def form_valid(self, form):
        """
        This method should save the data of form.
        """
        instance = form.save(commit=False)
        user = User.objects.get(id=self.request.user.id)
        instance.user = user
        instance.save()
        return super(ImageCreateView, self).form_valid(form)


class ImageDeleteView(LoginRequiredMixin, DeleteView):
    """
    This view is used to delete images.
    """
    model = Image
    success_url = reverse_lazy('store:my_store_list')


class StoreCreateView(CreateView):
    """
    This view is used to create store using store form.
    """
    form_class = StoreForm
    template_name = 'store/store_create.html'
    success_url = reverse_lazy('store:my_store_list')

    def get_context_data(self, **kwargs):
        """
        This method should pass extra context form and formset to template.
        """
        context = super(StoreCreateView, self).get_context_data(**kwargs)
        context['formset'] = HourFormset()
        return context

    def post(self, request, *args, **kwargs):
        """
        This method should check whether form and formset are valid or not.
        """
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = HourFormset(self.request.POST)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)

    def form_valid(self, form, formset):
        """
        This method should save the data of form and formset.
        """
        instance = form.save(commit=False)
        instance.user = self.request.user
        form.save()
        formset.instance = instance
        formset.save()
        return super(StoreCreateView, self).form_valid(form)


class StoreUpdateView(UpdateView):
    """
    This view is used to update stores.
    """
    model = Store
    form_class = StoreForm
    template_name = 'store/store_update.html'
    success_url = reverse_lazy('store:my_store_list')

    def get_context_data(self, **kwargs):
        """
        This method should pass extra context form and formset with instance of object to template.
        """
        context = super(StoreUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = HourFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = HourFormset(instance=self.object)
        return context

    def form_valid(self, form):
        """
        This method should save the data of form and formset.
        """
        context = self.get_context_data()
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
        return super().form_valid(form)


class StoreListView(FilterView):
    """
    This view will display list of stores.
    """
    template_name = 'store/store_list.html'
    context_object_name = 'stores'
    filterset_class = StoreFilter

    def get_queryset(self):
        """
        This method should return queryset of stores.
        """
        query = self.request.GET.get('search')
        if query:
            return Store.objects.filter(
                Q(name__icontains=query) | Q(category__name__icontains=query))
        else:
            return Store.objects.all()


class MyStoreListView(LoginRequiredMixin, FilterView):
    """
    This view will display list of stores of specific user.
    """
    template_name = 'store/my_store_list.html'
    context_object_name = 'stores'
    filterset_class = StoreFilter

    def get_queryset(self):
        """
        This method should return queryset of stores of specific user.
        """
        query = self.request.GET.get('search')
        if query:
            return Store.objects.filter(Q(name__icontains=query) |
                                        Q(category__name__icontains=query))
        else:
            return Store.objects.filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        This method should pass extra context to template.
        """
        context = super(MyStoreListView, self).get_context_data(**kwargs)
        context['form'] = ImageForm
        return context


class StoreDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    """
    This view is used to delete stores.
    """
    model = Store
    success_url = reverse_lazy('store:my_store_list')

    def test_func(self):
        """
        This method will test if user has permission or not.
        """
        instance = self.get_object()
        if instance.user.id == self.request.user.id:
            return True


class StoreDetailView(LoginRequiredMixin, DetailView):
    """
    This view will show the details of store.
    """
    model = Store
    template_name = 'store/store_detail.html'
    context_object_name = 'store'
