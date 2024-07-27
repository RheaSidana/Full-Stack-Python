from django.shortcuts import render, redirect
from .forms.Customers import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login

# Create your views here.
def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            login(request, user)
            messages.success(request, "USer is valid")
            return redirect("my_destinations")
        else:
           messages.error(request, "User is invalid") 
    else:
        form = UserRegistrationForm()
    return render(
        request=request,
        template_name="formTemplate.html",
        context={
        "form": form
        }
    )