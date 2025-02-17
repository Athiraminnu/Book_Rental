from datetime import date, timedelta
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .forms import EditProfileForm
from .models import Category, Books, Wishlist
from django.contrib.auth.decorators import login_required

def dashboard(request):
    # currentDate = date.today()
    # todayDate = currentDate.isoformat()
    # sixMonths = currentDate - timedelta(days=180)
    # sixMonthsAgo = sixMonths.isoformat()
    # book = Books.objects.filter(created=(sixMonthsAgo, todayDate))
    book = Books.objects.all()

    paginator = Paginator(book, 6)  # Show 6 books per page

    # Get the current page number from the request
    page_number = request.GET.get('page')
    bookInPage = paginator.get_page(page_number)  # Get the books for the current page

    return render(request, "dashboard.html", {'data': bookInPage})


def aboutUs(request):
    return render(request, "about_us.html")


def fiction(request):
    try:
        fictionCategory = Category.objects.get(name='FICTION')
        fictionBook = Books.objects.filter(var=fictionCategory)
    except Category.DoesNotExist:
        messages.error(request, "Fiction category doesnot exist!!!")
    return render(request, "fiction.html", {'fbooks': fictionBook})


def anime(request):
    try:
        animeCategory = Category.objects.get(name='anime')
        animeBooks = Books.objects.filter(var=animeCategory)
    except Category.DoesNotExist:
        messages.error(request, "anime category doesnot exist!!!")
    return render(request, 'anime.html', {'abooks': animeBooks})


def horror(request):
    try:
        horrorCategory = Category.objects.get(name='horror')
        horrorBooks = Books.objects.filter(var=horrorCategory)
    except Category.DoesNotExist:
        messages.error(request, "Horror category does not exist!!!")
        horrorBooks = []

    return render(request, 'horror.html', {'hbooks': horrorBooks})


def novels(request):
    try:
        novelCategory = Category.objects.get(name='novels')
        novelBooks = Books.objects.filter(var=novelCategory)
    except Category.DoesNotExist:
        messages.error(request, "Novels category does not exist!!!")
        novelBooks = []
    return render(request, 'novels.html', {'nbooks': novelBooks})


def details(request, id):
    detail = get_object_or_404(Books, id=id)
    return render(request, 'bookdetails.html', {'itemdetails': detail})


def user_login(request):
    if request.method == 'POST':
        userName = request.POST['username']
        Password = request.POST['password']
        user = authenticate(request, username=userName, password=Password)
        if user is not None:
            login(request, user)
            messages.success(request, "LOGIN SUCCESS")
            return redirect('library:dashBoard')
        else:
            messages.error(request, "LOGIN FAILED")
            return redirect('library:login')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    messages.success(request, "Logged Out Sucessfully")
    return redirect('library:dashBoard')


@login_required
def rent(request):
    if request.method == 'POST':
        messages.success(request, "Sucessfully Rented")
    return render(request, 'rent.html')


@login_required
def viewProfile(request, id):
    profile_details = get_object_or_404(User, id=id)
    return render(request, 'profile.html', {'profileDetails': profile_details})


@login_required
def editProfile(request):
    if request.method == 'POST':
        # Bind the form with POST data and associate it with the logged-in user
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('library:profile', id=request.user.id)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'editprofile.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('library:register')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('library:register')
        # Create the user
        try:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password
            )
            user.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('library:login')
        except Exception as e:
            messages.error(request, "An error occurred during registration.")
            print(e)
            return redirect('library:register')
    return render(request, 'register.html')


@login_required
def wishlist(request, id):
    addBook = get_object_or_404(Books, id=id)
    # Get or create the wishlist entry for the logged-in user
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, book=addBook)
    # Retrieve the entire wishlist for the logged-in user
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wish': wishlist_items})


def cart(request):
    return render(request, 'cart.html')
