from django.shortcuts import render
from .forms import ThingForm
from .models import Thing

def home(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ThingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            Thing(name=form.cleaned_data['name'], description=form.cleaned_data['description'], quantity=form.cleaned_data['quantity']).save()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ThingForm()
    return render(request, 'home.html', {'form': form})
