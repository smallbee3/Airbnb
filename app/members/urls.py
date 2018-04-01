from django.urls import path

from .views import (
    AuthTokenView,
    UserCreateView,
    UserListView,
    UserDetailView,
    LogoutView
)


app_name = 'user'
urlpatterns = [
    path('auth-token/', AuthTokenView.as_view(), name='auth-token'),
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    path('logout/', LogoutView.as_view(), name='logout'),
]
