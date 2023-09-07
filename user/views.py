from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from user.filters import UserFilter
from user.forms import SignupForm, ProfileForm
from user.models import User


class CustomPermissionRequired(PermissionRequiredMixin):
    """
    This view will give permission to user.
    """
    permission_required = ('user.is_staff', 'user.is_superuser')


class SignupView(CreateView):
    """
    This view will create user instance.
    """
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('user:login')


class ProfileView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    """
    This view will display profile of user.
    """
    model = User
    form_class = ProfileForm
    template_name = 'user/profile.html'
    success_url = reverse_lazy('store:index')

    def test_func(self):
        """
        This method will check that user has permission or not.
        """
        instance = self.get_object()
        if instance.id == self.request.user.id:
            return True


class UserDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    """
    This view will delete user.
    """
    model = User
    success_url = reverse_lazy('user:login')

    def test_func(self):
        """
        This method will check that user has permission or not.
        """
        instance = self.get_object()
        if instance.id == self.request.user.id:
            return True


class UserListView(LoginRequiredMixin, CustomPermissionRequired, FilterView):
    """
    This view will display list of all users.
    """
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'
    filterset_class = UserFilter

    def get_queryset(self):
        """
        This method should return queryset of users.
        """
        query = self.request.GET.get('search')
        if query:
            return User.objects.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query) |
                Q(username__icontains=query) | Q(email__iexact=query) |
                Q(phone_number__exact=query))
        else:
            return User.objects.all()
