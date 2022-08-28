from django.shortcuts import redirect, render
from portfolio.models import Project
from django.core.mail import send_mail
from django.http import HttpResponse
import sethbrittaindotdev.settings.production as settings

# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', { 'projects': projects })

def mail(request):
    if request.method == 'POST':
        if request.POST['address']:
            return HttpResponse("Access Denied")
        if request.POST['firstname'] and request.POST['lastname'] and request.POST['subject'] and request.POST['email'] and request.POST['body']:
            email_text = "From: {fname} {lname}\nEmail Address: {email}\nCompany: {company}\n\n".format(fname=request.POST["firstname"], lname=request.POST["lastname"], email=request.POST["email"], company=request.POST["company"])
            email_text += request.POST["body"]
            send_mail(request.POST['subject'], email_text, settings.EMAIL_HOST_USER, ['contact@sethbrittain.dev'], fail_silently=True)
    
    return redirect("/")