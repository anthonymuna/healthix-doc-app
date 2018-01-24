from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SearchForm
from .forms import SignUpForm
from .models import Search

# Create your views here.
#@login_required(redirect_field_name='login')
def index(request):
    auth = True
    if not request.user.is_authenticated:
        auth = False
    return render(request, 'index.html', {'auth':auth})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(is_staff=True, is_active=True, **form.cleaned_data)
            messages.success(request, "Your response has been recorded")
            if login_user(request, user):
                return redirect('index')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

def login_user(request, user):
    login(request, user)
    return True

def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Please check your user name and password!")
    return render(request, 'login.html')

@login_required(redirect_field_name='login')
def homepage(request):
    if request.POST:
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        mobile_num = request.POST['mobilenumber']
        search = Search(first_name=firstname, last_name=lastname, mobile_num=mobilenumber)
        search.save()
        return redirect('index')
    return render(request, 'search.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def search(request):
    form = SearchForm(request.GET or {})
    if form.is_valid():
        results = form.get_queryset()
    else:
        results = Search.objects.none()

    return  render(request, 'search.html', {
        'form': form,
        'results': results,
    })

def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv",
                                       file_name="download")
    else:
        form = UploadFileForm()
    return render(
        request,
        'search.html',
        {
            'form': form,
            'title': 'Excel file upload',
            'header': ('Please upload excel file: ')
        })