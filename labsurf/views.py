from django.shortcuts import render

# Create your views here.
def index(request):
    context= {
        'title': 'Welcome to Labsurf',
    }
    return render(request, 'labsurf/pages/index.html', context)

def blank(request):
    return render(request, 'labsurf/pages/blank.html')

def buttons(request):
    return render(request, 'labsurf/pages/buttons.html')

def charts(request):
    return render(request, 'labsurf/pages/charts.html')

def elements(request):
    return render(request, 'labsurf/pages/elements.html')

def formu(request):
    return render(request, 'labsurf/pages/formu.html')

def signup(request):
    return render(request, 'labsurf/pages/signup.html')

def signin(request):
    return render(request, 'labsurf/pages/signin.html')

def tables(request):
    return render(request, 'labsurf/pages/tables.html')

def typography(request):
    return render(request, 'labsurf/pages/typography.html')

def widget(request):
    return render(request, 'labsurf/pages/widget.html')



