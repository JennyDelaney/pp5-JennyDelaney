from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    """
    Customers can send a message with the form
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Your message has been submitted. \
                Someone from our team will be in touch shortly.')

    form = ContactForm

    context = {
        'form': form,
    }

    template = 'contact/contact.html'

    return render(request, template, context)
