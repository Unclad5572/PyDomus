from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm

# Create your views here.
def account_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            #Ajouter ensuite la logique de connexion ici. A faire apres que la BDD soit mise en place.
            return HttpResponse(f"Email: {email}, Password: {password}")
    else:
        form = LoginForm()
        return render(request, 'login.html', context={'form': form})