from django.shortcuts import render,redirect
from WomensAdmin.models import employeedb, categorydb, productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from WomenWeb.models import contactdetails
from django.contrib import messages
# Create your views here.
def indexpage(request):
    return render(request,"index.html")
def addemployee(request):
    return render(request, "Addemployee.html")
def employeepage(request):
    if request.method == "POST":
        na = request.POST.get("name")
        em = request.POST.get("email")
        mob = request.POST.get("mob")
        img = request.FILES["img"]
        pwd=request.POST.get('pwd')
        cwd=request.POST.get('cpwd')
        obj = employeedb(Name=na, Email=em, Mobile=mob, Image=img, Password=pwd, CPassword=cwd)
        obj.save()
        messages.warning(request, "Employee added successfully")
        return redirect(addemployee)
def displayemp(request):
    data = employeedb.objects.all()
    return render(request, "Displayemployee.html", {'data': data})
def editdata(request,dataid):
    data=employeedb.objects.get(id=dataid)
    print(data)
    return render(request,"editemployee.html", {'data':data})
def updatedata(request,dataid):
    if request.method== "POST":
        na=request.POST.get('name')
        em = request.POST.get("email")
        mob = request.POST.get("mob")
        pwd = request.POST.get('pwd')
        cwd = request.POST.get('cpwd')
        try:
            img = request.FILES["img"]
            fs=FileSystemStorage()
            file= fs.save(img.name,img)
        except MultiValueDictKeyError:
            file= employeedb.objects.get(id=dataid).Image
        employeedb.objects.filter(id=dataid).update(Name=na, Email=em, Mobile=mob, Image=file, Password=pwd, CPassword=cwd)
        return redirect(displayemp)
def deletedata(request,dataid):
    data= employeedb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayemp)
def displaycategory(request):
    return render(request,'category.html')
def categorypage(request):
    if request.method == "POST":
        ca = request.POST.get("cname")
        img = request.FILES["image"]
        des = request.POST.get("des")
        object = categorydb(CName=ca,CImage=img, Description=des)
        object.save()
        messages.warning(request, "Category added successfully")
        return redirect(displaycategory)
def viewcategory(request):
    data = categorydb.objects.all()
    return render(request,'viewcategory.html', {'data': data})
def editcategory(request,dataid):
    data=categorydb.objects.get(id=dataid)
    print(data)
    return render(request,"editcategory.html", {'data':data})
def updatecategory(request,dataid):
    if request.method== "POST":
        ca = request.POST.get("cname")
        des = request.POST.get("des")
        try:
            cimage = request.FILES["image"]
            fs = FileSystemStorage()
            file = fs.save(cimage.name, cimage)
        except MultiValueDictKeyError:
            file= categorydb.objects.get(id=dataid).CImage
        categorydb.objects.filter(id=dataid).update(CName=ca,CImage=file, Description=des)
        return redirect(displaycategory)
def deletecategory(request,dataid):
    data= categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategory)
def addproduct(request):
    data=categorydb.objects.all()
    return render(request,"product.html",{'data':data})
def productpage(request):
    if request.method == "POST":
        p = request.POST.get("pname")
        pr = request.POST.get("price")
        q = request.POST.get("qty")
        d = request.POST.get("pdes")
        pi = request.FILES["pimg"]
        c = request.POST.get('cat')
        a= productdb(Product=p,Price=pr,Quantity=q,PDescription=d,PImage=pi,Category=c)
        a.save()
        messages.warning(request, "Product added successfully")
        return redirect(addproduct)
def viewproduct(request):
    data = productdb.objects.all()
    return render(request, 'viewproduct.html', {'data': data})

def editproduct(request, dataid):
    data = productdb.objects.get(id=dataid)
    das = categorydb.objects.all()
    print(data)
    return render(request, "editproduct.html", {'data': data, 'das': das})
def updateproduct(request, dataid):
    if request.method == "POST":
        qr = request.POST.get("pname")
        pr = request.POST.get("price")
        q = request.POST.get("qty")
        d = request.POST.get("pdes")
        v = request.POST.get('cat')
    try:
        pi = request.FILES["pimg"]
        fs = FileSystemStorage()
        file = fs.save(pi.name, pi)
    except MultiValueDictKeyError:
        file = productdb.objects.get(id=dataid).pi
    productdb.objects.filter(id=dataid).update(Product=qr, Price=pr, Quantity=q, PDescription=d, PImage=file,Category=v)
    return redirect(addproduct)

def deleteproduct(request, dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(addproduct)

def loginpage(request):
    return render(request, "login.html")
def adminlogin(request):
    if request.method == 'POST':
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request, user)
                request.session['username'] = username_r
                request.session['password'] = password_r
                return redirect(indexpage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)
def contactpages(request):
    datas = contactdetails.objects.all()
    return render(request,'acontact.html',{'dat':datas})

def deletecontact(request,dataid):
    data =contactdetails.objects.filter(id=dataid)
    data.delete()
    return redirect(contactpages)