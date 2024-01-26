from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
#from .forms import UserUpdateForm
#from .forms import ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            #group = Group.objects.get(name='Customers')
            #user.groups.add(group)
            return redirect('user-login')
    else:
        form = CreateUserForm()
    
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)


def profile(request):
    context = {
        # Add any necessary data to be passed to the profile template
    }
    return render(request, 'user/profile.html', context)


def profile_update(request):
    {
   # if request.method == 'POST':
       
           # request.POST, request.FILES, instance=request.user.profile)
       
          #  return redirect('user-profile')
   # else:
       

    
    }
   # return render(request, 'user/profile_update.html', context)