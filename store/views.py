from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm, UserEditProfile, ChangePassword, ProductForm


def updateProduct(request, pk):
    product = Product.objects.get(id=pk)

    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        "form": form
    }

    return render(request, 'updateproduct.html', context)


def addProduct(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
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
                messages.success(request, "Your Password Is Changed, Please")
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
    return render(
        request,
        "product.html",
        {"product": product},
    )


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
