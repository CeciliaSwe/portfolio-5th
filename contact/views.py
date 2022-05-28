from django.shortcuts import render, redirect, reverse
from django.contrib import messages


from .forms import ContactForm


def contact(request):
    """
    To submit contact form
    """
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Thank you, message sent successfully!")
            return redirect(reverse("contact"))

        else:
            messages.error(
                request,
                "Failed to submit contact form.\
                                        Please ensure the form is valid",
            )
    else:
        form = ContactForm()

    context = {
        "form": form,
    }
    template = "contact/contact.html/"
    return render(request, template, context)
