from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from accounts import views as account_views


app_name = "accounts"
urlpatterns = [
    path(
        "",
        account_views.LoginView.as_view(),
        name="login",
    ),
    path(
        "register/",
        account_views.register_page,
        name="register",
    ),
    path(
        "forgot-password/",
        TemplateView.as_view(template_name="accounts/forgot-password.html"),
        name="forgot-password",
    ),
    path(
        "reset-password/",
        TemplateView.as_view(template_name="accounts/reset-password.html"),
        name="reset-password",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="accounts:login"),
        name="logout",
    ),
]
