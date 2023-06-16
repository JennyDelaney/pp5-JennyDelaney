from django.shortcuts import render
from django.contrib import messages

from .forms import MailingListForm


def mailing_list(request):
    """
    Customers can sign up for our newsletter
    """
    if request.method == 'POST':
        form = MailingListForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Thank you for signing up for our Newsletter')

    form = MailingListForm

    context = {
        'form': form,
    }

    template = 'mailing_list/mailing_list.html'

    return render(request, template, context)
