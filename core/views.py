from django.shortcuts import render ,redirect
from .models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
         

        contact = Contact(
            name= name,
            email= email,
            phone=phone,
            subject= subject,
            message=message,
            created_at = datetime.today()
        )
        contact.save()
        messages.success(request, "Your message has been sent successfully!")
        return redirect(request.META.get('HTTP_REFERER', 'contact'))  # back to same page
      

    return render(request, 'contact.html'  )
# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('contact')
#     else:
#         form = ContactForm()

#     return render(request, 'core/contact.html', {'form': form})