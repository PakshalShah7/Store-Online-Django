from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from storeonline import settings
from user.forms import LoginForm
from user.views import SignupView, ProfileView, UserDeleteView, UserListView

app_name = 'user'

urlpatterns = [

    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name="registration/login.html", form_class=LoginForm),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('user/list/', UserListView.as_view(), name='user_list')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
