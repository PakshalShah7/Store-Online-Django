from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from category.filters import CategoryFilter
from category.forms import CategoryForm
from category.models import Category
from user.views import CustomPermissionRequired


class CategoryCreateView(LoginRequiredMixin, CustomPermissionRequired, CreateView):
    """
    This view is used to create category using category form.
    """
    form_class = CategoryForm
    success_url = reverse_lazy('category:category_list')


class CategoryListView(LoginRequiredMixin, CustomPermissionRequired, FilterView):
    """
    This view will display list of categories.
    """
    template_name = 'category/category_list.html'
    context_object_name = 'categories'
    filterset_class = CategoryFilter

    def get_queryset(self):
        """
        This method should return queryset of categories.
        """
        query = self.request.GET.get('search')
        if query:
            return Category.objects.filter(Q(name__icontains=query))
        else:
            return Category.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        This method should pass extra context to template.
        """
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['form'] = CategoryForm
        return context


class CategoryUpdateView(LoginRequiredMixin, CustomPermissionRequired, UpdateView):
    """
    This view is used to update categories.
    """
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_create.html'
    success_url = reverse_lazy('category:category_list')


class CategoryDeleteView(LoginRequiredMixin, CustomPermissionRequired, DeleteView):
    """
    This view is used to delete categories.
    """
    model = Category
    success_url = reverse_lazy('category:category_list')
