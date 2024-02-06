from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields["username"].label = "Your username"
        self.fields["password1"].label = "Your password"
        self.fields["password2"].label = "Confirm Password"

        for _, field in self.fields.items():
            field.help_text = None

            field.widget.attrs.update(
                {
                    "class": "bg-red-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500",
                    "placeholder": "johndoe",
                }
            )

            if field.widget.input_type == "password":
                field.widget.attrs.update(
                    {
                        "placeholder": "••••••••",
                    }
                )


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Your username",
        widget=forms.TextInput(attrs={"autofocus": "true", "placeholder": "John doe"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "••••••••"})
    )

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                }
            )
