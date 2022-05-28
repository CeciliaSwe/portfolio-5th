from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail

from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm


def newsletter_signup(request):
    """
    newsletter signup
    """
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, "Hey, you are alredy signed up, thanks!")
        else:
            instance.save()
            messages.success(request, "You have successfully signed up!")
            subject = "Welcome to Active8!"
            to_email = [instance.email]
            signup_message = """Thank you for signing up! Let's go for an adventure\
            Need to unsubscribe? Follow this link but we miss you!\
            https://active8-adventures.herokuapp.com/newsletter/unsubscribe/"""
            send_mail(
                subject=subject,
                from_email="from@active8.com",
                recipient_list=to_email,
                message=signup_message,
                fail_silently=False,
            )

    context = {
        "form": form,
    }
    template = "newsletters/sign_up.html/"
    return render(request, template, context)


def newsletter_unsubscribe(request):
    """
    Newsletter unsubscribe
    """
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request, "You have successfully unsubscribed!")
            subject = "Sorry you're leaving!"
            to_email = [instance.email]
            unsubscribe_message = """Come back for more adventures"""
            send_mail(
                subject=subject,
                from_email="from@active8.com",
                recipient_list=to_email,
                message=unsubscribe_message,
                fail_silently=False,
            )
        else:
            messages.warning(request, "Email not found - are you signed up?")

    context = {
        "form": form,
    }
    template = "newsletters/unsubscribe.html"
    return render(request, template, context)
