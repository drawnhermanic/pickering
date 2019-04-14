import re
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView

from pickering.forms import LogMessageForm
from pickering.models import LogMessage

def hello_there(request, name):
    return render(
        request,
        'pickering/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )  

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context
        
def about(request):
    return render(request, "pickering/about.html")

def contact(request):
    return render(request, "pickering/contact.html")    

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "pickering/log_message.html", {"form": form})    