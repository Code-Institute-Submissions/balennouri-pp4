from django.contrib.auth.models import User
from django import forms
from .models import Product, Customer, Comment
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    SetPasswordForm)
"""
These forms were inspired by:
https://docs.djangoproject.com/en/5.0/topics/forms/
"""


class CommentForm(forms.ModelForm):
    """
    Form for comment section.
    """

    class Meta:
        model = Comment
        fields = ["commenter_body"]
        widgets = {
            "commenter_body": forms.Textarea(attrs={"class": "form-control"}),
        }


class CheckoutForms(forms.ModelForm):
    """
    Form for checkout page.
    """

    class Meta:
        model = Customer
        fields = ["phone"]
        widgets = {
            "phone": forms.TextInput(attrs={"class": "form-control"}),
        }


class ProductForm(forms.ModelForm):
    """
    Form for add products page.
    """

    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "sales_price": forms.TextInput(attrs={"class": "forms-control"}),
        }
        labels = {
            "name": "Enter Product Name",
            "image": "Select an Image",
            "category": "Select Category",
            "price": "Enter a price",
            "description": "Enter a Description",
            "is_sales": "Is the product on sale?",
            "sales_price": "Enter a Sales price",
        }


class ChangePassword(SetPasswordForm):
    """
    Form for change the password.
    """

    class Meta:
        model = User
        fields = ["new_password1", "new_password2"]

    def __init__(self, *args, **kwargs):
        super(ChangePassword, self).__init__(*args, **kwargs)

        self.fields["new_password1"].widget.attrs["class"] = "form-control"
        self.fields["new_password1"].widget.attrs["placeholder"] = "Password"
        self.fields["new_password1"].label = ""
        self.fields["new_password1"].help_text = None

        self.fields["new_password2"].widget.attrs["class"] = "form-control"
        self.fields["new_password2"].widget.attrs[
            "placeholder"
        ] = "Confirm \
            Password"
        self.fields["new_password2"].label = ""
        self.fields["new_password2"].help_text = (
            '<span class="form-text text-muted"><small>Enter the same \
                password as before, for verification.</small></span>'
        )


class UserEditProfile(UserChangeForm):
    """
    Form for update profile details.
    """

    password = None
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Email Address"}
        ),
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )

    def __init__(self, *args, **kwargs):
        super(UserEditProfile, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "User Name"
        self.fields["username"].label = ""
        self.fields["username"].help_text = (
            '<span class="form-text text-muted"><small>Required. 150 \
                characters or fewer. Letters, digits and @/./+/-/_ \
                    only.</small></span>'
        )


class SignUpForm(UserCreationForm):
    """
    Form for the sign-up page.
    """

    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Email Address"}
        ),
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "User Name"
        self.fields["username"].label = ""
        self.fields["username"].help_text = (
            '<span class="form-text text-muted"><small>Required. 150 \
                characters or fewer. Letters, digits and @/./+/-/_ \
                    only.</small></span>'
        )

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password1"].label = ""
        self.fields["password1"].help_text = None

        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs[
            "placeholder"
        ] = "Confirm \
            Password"
        self.fields["password2"].label = ""
        self.fields["password2"].help_text = (
            '<span class="form-text text-muted"><small>Enter the same \
                password as before, for verification.</small></span>'
        )
