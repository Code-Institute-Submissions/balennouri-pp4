from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import user_passes_test
from .models import Product, Category, Comment
from cart.cart import Cart
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime
from .forms import (
    SignUpForm,
    UserEditProfile,
    ChangePassword,
    ProductForm,
    CheckoutForms,
    CommentForm,
)


def DeleteComments(request, pk):
    comment = Comment.objects.filter(product=pk).last()
    product_id = comment.product.id
    comment.delete()
    messages.success(request, "Your latest comment have been deleted")
    return redirect(reverse('product', args=[product_id]))


def AddComments(request, pk):
    product = Product.objects.get(id=pk)
    form = CommentForm(instance=product)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=product)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data["commenter_body"]
            sms = Comment(
                product=product,
                commenter_name=name,
                commenter_body=body,
                date_added=datetime.now(),
            )
            sms.save()
            messages.success(request, "Your comment have been added")
            return redirect(reverse('product', args=[pk]))
        else:
            pass
    else:
        form = CommentForm()

    return render(request, "add_comment.html", {"form": form})


@user_passes_test(lambda u: u.is_staff, login_url='home')
def StaffAdmin(request):
    products = Product.objects.all()
    return render(
        request,
        "staff.html",
        {"products": products},
    )


@user_passes_test(lambda u: u.is_staff, login_url='home')
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    messages.success(request, "Product Is Deleted")
    return redirect("staff")


@user_passes_test(lambda u: u.is_staff, login_url='home')
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)

    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Is Updated")
            return redirect("staff")

    context = {"form": form}

    return render(request, "updateproduct.html", context)


@user_passes_test(lambda u: u.is_staff, login_url='home')
def addProduct(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New Product Is Added")
            return redirect("staff")
    else:
        form = ProductForm()
    context = {"form": form}
    return render(request, "addproduct.html", context)


def password_update(request):
    if request.user.is_authenticated:
        user_active = request.user
        if request.method == "POST":
            form = ChangePassword(user_active, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your Password Is Changed")
                login(request, user_active)
                return redirect("user_update")
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect("password_update")
        else:
            form = ChangePassword(user_active)
            return render(
                request,
                "password_update.html",
                {"form": form},
            )
    else:
        messages.success(request, "You Must Be Logged in To Change Password")
        return redirect("home")


def deleteUser(request):
    user = request.user
    user.delete()
    messages.success(request, "Your Account Is Deleted")
    return redirect("register")


def user_update(request):
    if request.user.is_authenticated:
        active_user = User.objects.get(id=request.user.id)
        user_form = UserEditProfile(request.POST or None, instance=active_user)
        if user_form.is_valid():
            user_form.save()
            login(request, active_user)
            messages.success(request, "Profile Has Been Updated")
            return redirect("home")
        return render(request, "user_update.html", {"user_form": user_form})
    else:
        messages.success(request, "You Must be Logged In to Update A Profile")
        return redirect("home")


def category(request, foo):
    foo = foo.replace("-", " ")
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(
            request,
            "category.html",
            {"products": products, "category": category},
        )
    except:
        messages.success(request, ("That Category Doesn't Exist.."))
        return redirect("home")


def product(request, pk):
    product = Product.objects.get(id=pk)
    comment_num = Comment.objects.filter(product=product).count()
    context = {
        "product": product,
        "comment_num": comment_num
    }
    return render(request, "product.html", context)


def home(request):
    products = Product.objects.all()
    return render(
        request,
        "home.html",
        {"products": products},
    )


def about(request):
    return render(
        request,
        "about.html",
        {},
    )


def checkout_views(request):
    form = CheckoutForms()
    if request.method == "POST":
        del request.session['session_key']
        messages.success(
            request,
            "Thank you for your request, We will contact\
             you in 30 minutes",
        )
        return redirect("home")
    return render(request, "checkout.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Logged In"))
            return redirect("home")
        else:
            messages.success(
                request,
                (
                    "There Was An Error, \
                Please Try Again.."
                ),
            )
            return redirect("login")
    else:
        return render(
            request,
            "login.html",
            {},
        )


def logout_user(request):
    logout(request)
    messages.success(request, ("You Have Been Logged Out!"))
    return redirect("home")


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request,
                (
                    "You Have Registered \
                Successfully!! Welcome"
                ),
            )
            return redirect("home")
        else:
            messages.success(
                request,
                (
                    "Whoops! There was a problem registering,\
                    Please try again."
                ),
            )
            return redirect("register")
    else:
        return render(
            request,
            "register.html",
            {"form": form},
        )
