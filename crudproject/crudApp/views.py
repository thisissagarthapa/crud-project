from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def home(request):
    data=Student.objects.filter(isDelete=False)
    return render(request,'crudapp/home.html',{'data':data})
def contact(request):
    return render(request,'crudapp/contact.html')

def form(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        email=request.POST.get('email')
        message=request.POST.get('message')
        Student.objects.create(name=name,age=age,email=email,message=message)
        messages.success(request,'Successfully register') 
        subject="python training"
        message="thanks for register"
        from_email='kingstonboysagar@gmail.com'
        recipient_list=['sujanthadarai710@gmail.com']
        send_mail(subject,message,from_email,recipient_list,fail_silently=False)
        messages.success(request,f"Hi {name} successfully register check your mail!!!")
        
        return redirect('form')
    return render(request,'crudapp/form.html')
def about(request):
    return render(request,'crudapp/about.html')

def delete_data(request,id):
    data=Student.objects.get(id=id)
    data.isDelete=True
    data.save()
    return redirect('home')

def search_data(request):
        if request.method=='POST':
           search=request.POST['search']
           finds=Student.objects.filter(name__icontains=search)
           redirect('home')
        return render(request, 'crudapp/search.html',{'finds':finds})

def update_data(request,id):
    data=Student.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        email=request.POST.get('email')
        message=request.POST.get('message')
        stu=Student.objects.get(id=id)
        stu.name=name
        stu.age=age
        stu.email=email
        stu.message=message
        stu.save()
        messages.success(request,'successfully updated')
        return redirect('home')
        
    return render(request,'crudapp/update.html',{'data':data})