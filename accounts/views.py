from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from accounts.forms import UserRegisterForm, UserLoginForm
from django.contrib import messages

# Create your views here.


def register_page(request):
    if request.user.is_authenticated:
        return redirect("/accounts/profile")

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Akun <strong>{username}</strong> berhasil dibuat!"
            )
            return redirect("accounts:sign-in")
    else:
        form = UserRegisterForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/sign-up.html", context)


class LoginView(auth_views.LoginView):
    form_class = UserLoginForm
    next_page = "/accounts/profile"
    template_name = "accounts/sign-in.html"

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context["title"] = "Login"
    #     return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/accounts/profile")

        return super().dispatch(request, *args, **kwargs)
