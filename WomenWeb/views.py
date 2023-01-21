from django.shortcuts import render, redirect
from WomensAdmin.models import categorydb, productdb
from WomenWeb.models import Customerdetails,contactdetails,billing,itemcart
from django.contrib import messages


# Create your views here.
def mainpage(request):
    data = categorydb.objects.all()
    return render(request, "main.html", {'data': data})

def Contactpage(request):
    data = categorydb.objects.all()
    return render(request, "contactpage.html", {'data': data})

def savedata(request):
    if request.method=="POST":
        contact=request.POST.get('name')
        em=request.POST.get('email')
        sub=request.POST.get('subject')
        msg=request.POST.get('message')
        ob= contactdetails(Name=contact,Email=em,Subject=sub,Message=msg)
        ob.save()
        messages.warning(request, "Message sent")
        return redirect(Contactpage)

def Aboutpage(request):
    data=categorydb.objects.all()
    return render(request,"About.html",{'data':data})

def catpage(request,itemCatg):
    data=categorydb.objects.all()
    print("===itemCatg===", itemCatg)
    catg=itemCatg.upper()
    products=productdb.objects.filter(Category=itemCatg)
    context={
        'products':products,
        'catg':catg,
        'data':data
    }
    return render(request,'categorydisplay.html',context)

def productdetails(request,dataid):
    datas=productdb.objects.get(id=dataid)
    data=categorydb.objects.all()
    return render(request,"productdetails.html",{'dat':datas,'data':data})

def cart(request):
    datas =itemcart.objects.all()
    return render(request,"cart.html",{'data':datas})

def cartsave(request):
    if request.method=="POST":
        pr=request.POST.get("Product")
        qu=request.POST.get("qty")
        total=request.POST.get("totalprice")
        abc = itemcart(Product=pr,quantity=qu,totalprice=total)
        abc.save()
        return redirect(cart)

def deletecart(request,dataid):
    datas= itemcart.objects.filter(id=dataid)
    datas.delete()
    return redirect(cart)
def billingpage(request):
    return render(request,"biiling.html")

def savebilling(request):
    if request.method=='POST':
        fn=request.POST.get('fname')
        ln=request.POST.get('lname')
        un=request.POST.get('uname')
        em=request.POST.get('email')
        ad=request.POST.get('address')
        obj = billing(Fname=fn, Lname=ln, Uname=un, Email=em, Address=ad)
        obj.save()
        return redirect(mainpage)

def mylogin(request):
    data= categorydb.objects.all()
    return render(request, "loginpage.html",{'data':data})
def regdata(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if password==confirmpassword:
            athu=Customerdetails(username=username,email=email,password=password,confirmpassword=confirmpassword)
            athu.save()
            return redirect(mylogin)
        else:
            messages.warning(request,"password and confirm password doesnot match")
        return render(request, 'loginpage.html')
def customerlogin(request):
    if request.method == 'POST':
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')
        if Customerdetails.objects.filter(username=username_r,password=password_r).exists():
            data=Customerdetails.objects.filter(username=username_r,password=password_r).values('email','id').first()
            request.session['username']=username_r
            request.session['password']=password_r
            return redirect(mainpage)
        else:
            messages.warning(request, "sorry invalid user")
        return render(request,'loginpage.html')

def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(mainpage)
