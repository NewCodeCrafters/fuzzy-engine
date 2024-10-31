from django.shortcuts import render, redirect
from .models import Anime, Category
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth import logout, update_session_auth_hash, login, authenticate


def home(request):
    animes = Anime.objects.all()
    categories = Category.objects.all()
    context = {
        'animes': animes,
        'categories': categories,
        'numbers': [1, 2, 3, 4]
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def catgories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, "categories.html", context)

def delete_anime(request, id):
    anime = anime.objects.get(id=id)
    anime.delete()
    return redirect('homepage')
    
# def download_document(request, book_id):
#     try:
#         book = Book.objects.get(id=id)
#         response = FileResponse(book.documents.open(), as_attachment=True)
#         return response
#     except Exception:
#         raise Http404("Document not found.")

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context = {
        'form': form,        
    }
    return render(request, 'signup.html', context)

# detail view
def anime_view(request, id):
    animes = Anime.objects.get(id=id)
    context = {
     'anime': animes,   
    }
    return render(request, "anime_view.html", context)


def logout_page(request):
    logout(request)    
    return redirect('homepage')

def change_password(request):
    form = PasswordChangeForm()
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('login')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'password-change.html', context)

def login_view(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Pass 'data=request.POST' for form data
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("homepage")
            else:
                form.add_error(None, "Invalid username or password")  # Add error if authentication fails

    context = {
        'form': form,
    }
    return render(request, 'registration/login.html', context)

