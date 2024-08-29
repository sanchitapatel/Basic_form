# from django.shortcuts import render
# from .forms import *
# def home(request):
#     form=Stu_Registration()
#     # return render(request,"home.html",{"form":form})
#     if request.method=="POST":
#         form=Stu_Registration(request.POST)
        
#         if form.is_valid():
#             fname=form.cleaned_data["fname"]
#             lname=form.cleaned_data["lname"]
#             email=form.cleaned_data["email"]
#             contact=form.cleaned_data["contact"]
#             #print(fname,lname,email,contact)
#             user=Registration.objects.filter(email=email)
#             if user:
#                 msg="Email already exits"
#                 form=Registration()
#                 return render(request,'home.html',{'form':form,'msg':msg})
#             else:
#                 form.save()
#                 msg="registration successful"
#             #data={"fname":fname,"lname":lname,"email":email,"contact":contact}
#     return render(request,"home.html",{"form":form})
# def login(request):
#     form=Stu_Login()
#     if request.method=='POST':
#         data=Stu_Login(request.Post)
#         login_email=data.cleaned_data['email']
#         login_contact=data.cleaned_data['contact']
#         user=Registration.objects.filter(email=login_email)
#         if user:
#             user=Registration.objects.get(email=login_email)
#             print(user)
#     return render(request,'login.html',{'form':form})
from django.shortcuts import render
from app.forms import RegistrationForm,LoginForm,QueryForm
from .models import StudentModel,StudentQuery
# Create your views here.

def home(request):
    form = RegistrationForm()
    if request.method=='POST':
        data = RegistrationForm(request.POST)
        if data.is_valid():
            name=data.cleaned_data['stu_name']
            email=data.cleaned_data['stu_email']
            city=data.cleaned_data['stu_city']
            contact=data.cleaned_data['stu_mobile']
            password = data.cleaned_data['stu_password']
            print(name,email,city,contact,password)
            data.save()
            msg="Registration Successfully"
            return render(request,'home.html',{'form':form,'msg':msg})
    else:
        return render(request,'home.html',{'form':form})
    
def login(request):
    form = LoginForm()
    if request.method=="POST":
        data = LoginForm(request.POST)
        if data.is_valid():
            email = data.cleaned_data['stu_email']
            password = data.cleaned_data['stu_password']
            # print(email,password)
            user = StudentModel.objects.filter(stu_email=email)
            
            if user:
                user = StudentModel.objects.get(stu_email=email)
                # print(user.stu_password)
                if user.stu_password==password:
                    name = user.stu_name
                    email = user.stu_email
                    contact = user.stu_mobile
                    city = user.stu_city
                    password = user.stu_password
                    data = {
                        'name':name,
                        'email':email,
                        'contact':contact,
                        'city':city,
                        'password':password
                    }
                    form1=QueryForm()
                    return render(request,'dashboard.html',{'data':data,'query':form1})
                else:
                    msg = "Email & Password not matched"
                    return render(request,'login.html',{'form':form,'msg':msg})
            else:
                msg = "Email not register so please register first"
                return render(request,'login.html',{'form':form,'msg':msg})
    else:
        return render(request,'login.html',{'form':form})