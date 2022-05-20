from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail

from .models import Contact
from .forms import ContactForm


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Your message has been sent!')
            return redirect(reverse('contact'))
            #subject = "Thank you for contacting us"
            #to_email = [form.email]
            #auto_message = """Thank you for contacting us! We will get back to as soon as possible!"""
            #send_mail(subject=subject, from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=to_email, message=auto_message, fail_silently=False)

        else:
            messages.error(request, 'Failed to submit contact form.\
                                        Please ensure the form is valid')
    else:
        form = ContactForm()

    context = {
        'form' : form,
    }
    template = "contact/contact.html/"
    return render(request, template, context)
