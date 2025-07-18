from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required
def chat(request):
    return render(request, "chat/single_chat.html")
