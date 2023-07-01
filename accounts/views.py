from django.shortcuts import render
from .forms import RegistrationForm
from .models import Account

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.clean_data('first_name')
            last_name = form.clean_data('last_name')
            phone_number = form.clean_data('phone_number')
            email = form.clean_data('email')
            password = form.clean_data('password')
            username = email.split("@")[0]

            user = Account.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, username=username)
            user.phone_number = phone_number
            user.save()
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    
    return render(request, 'accounts/register.html', context)

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return 