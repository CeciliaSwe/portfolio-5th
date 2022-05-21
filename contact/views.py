from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render


from .models import Contact
from .forms import ContactForm


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Your message has been sent! We will get back to you as soon as we can')
            return redirect(reverse('contact'))

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
