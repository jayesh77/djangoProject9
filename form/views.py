from django.http import HttpResponse
from django.shortcuts import render
from .models import sfrom

# Create your views here.
def form(request):
    if request.method=="POST":
        if request.POST.get('che')=='on':
          name=request.POST.get('name')
          email=request.POST.get('email')
          fm=sfrom(na=name,em=email)
          fm.save()
        else:
            return HttpResponse("Terms and conditions not accepted")

    return render(request,'form.html')