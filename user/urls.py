from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup_view'),
    path('login/', views.LoginView.as_view(), name='login_view'),
    path('follow/<int:user_id>/', views.FollowView.as_view(), name='follow_view'),
    path('profile/<int:user_id>/', views.ProfileView.as_view(), name='profile_view'),
    path('mypage/<int:user_id>/',  views.MyPageView.as_view(), name='profile_view'),
]
