from django.shortcuts import render, redirect
from accounts_app.forms import UserForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Thank you for registering with us {username}')
            form.save()
            return redirect('login')
    else:
        form = UserForm()

    
    return render(request, 'account/register.html', {'form': form})