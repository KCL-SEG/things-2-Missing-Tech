from django.shortcuts import render
from .forms import ThingForm
from .models import Thing

def home(request):
    if request.method == 'POST':
        form = ThingForm(request.POST)
        
        if form.is_valid():
            form.save()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ThingForm()
    return render(request, 'home.html', {'form': form})
