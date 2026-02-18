from django.shortcuts import render ,redirect
from .models import Contact
from datetime import datetime
from django.contrib import messages
from techoraa import settings
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

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

        # email 

        sub= 'this is test' 
        from_emaill = settings.EMAIL_HOST_USER
        to_list = ['sharpstark057@gmail.com']
        
        html_msg = render_to_string('emails/success.html')
        plain_msg = strip_tags(html_msg)

        msg = EmailMultiAlternatives(
            subject = subject,
            body= plain_msg,
            from_email = from_emaill,
            to= [email],
        )
        msg.attach_alternative(html_msg,'text/html')
        msg.send(fail_silently=False);
        print('send')
        # sub= 'this is test'
        # msg= 'this is message from ' + name + 'for enquiry'
        # from_email = settings.EMAIL_HOST_USER
        # to_list = ['sharpstark057@gmail.com']
        # send_mail(sub,msg,from_email,to_list,fail_silently= True)





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



