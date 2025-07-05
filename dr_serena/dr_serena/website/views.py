from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.

def index(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def services(request):
    return render(request, 'website/services.html')

def faq(request):
    return render(request, 'website/faq.html')

def contact(request):
    return render(request, 'website/contact.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'website/contact_success.html', {'name': form.cleaned_data['name']})
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})




