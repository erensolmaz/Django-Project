from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from secondapp.models import Contact_Us, Category, register_table, add_product,cart,Order
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from secondapp.forms import add_product_form
from django.db.models import Q
from datetime import datetime
from django.core.mail import EmailMessage

def index(request):
    # if "user_id"in request.COOKIES:
    #     uid = request.COOKIES["user_id"]
    #     usr = get_object_or_404(User,id=uid)
    #     login(request,usr)
    #     if usr.is_superuser:
    #         return HttpResponseRedirect("/admin")
    #     if usr.is_active:
    #         return HttpResponseRedirect("/cust_dashboard")
            
    recent = Contact_Us.objects.all().order_by("-id")[:5]
    cats = Category.objects.all().order_by("cat_name")

    return render(request,"home.html",{"messages":recent,"category":cats})

def aboutpage(request):
    cats = Category.objects.all().order_by("cat_name")
    return render(request,"about.html",{"category":cats})

def contactpage(request):
    cats = Category.objects.all().order_by("cat_name")
    all_data = Contact_Us.objects.all().order_by("-id")
    if request.method=="POST":
        nm = request.POST["name"]
        con = request.POST["contact"]
        sub = request.POST["subject"]
        msz = request.POST["message"]

        data = Contact_Us(name=nm,contact_number=con,subject=sub,message=msz)
        data.save()
        res = "Dear {} Thanks for your feedback".format(nm)
        return render(request,"contact.html",{"status":res,"messages":all_data,"category":cats})
        # return HttpResponse("<h1 style='color:green;'>Dear {} Data Saved Successfully!</h1>".format(nm))
        

    return render(request,"contact.html",{"messages":all_data,"category":cats})

def register(request):
    if "user_id"in request.COOKIES:
        uid = request.COOKIES["user_id"]
        usr = get_object_or_404(User,id=uid)
        login(request,usr)
        if usr.is_superuser:
            return HttpResponseRedirect("/admin")
        if usr.is_active:
            return HttpResponseRedirect("/cust_dashboard")
    if request.method=="POST":
        fname = request.POST["first"]
        last = request.POST["last"]
        un = request.POST["uname"]
        pwd = request.POST["password"]
        em = request.POST["email"]
        con = request.POST["contact"]
        tp = request.POST["utype"]
        
        usr = User.objects.create_user(un,em,pwd)
        usr.first_name = fname
        usr.last_name = last
        if tp=="sell":
            usr.is_staff = True
        usr.save()

        reg = register_table(user=usr, contact_number=con)
        reg.save()
        return render(request,"register.html",{"status":"Mr/Miss. {} your Account created Successfully".format(fname)})
    return render(request,"register.html")

def check_user(request):
    if request.method=="GET":
        un = request.GET["usern"]
        check = User.objects.filter(username=un)
        if len(check) == 1:
            return HttpResponse("Exists")
        else:
            return HttpResponse("Not Exists")

def user_login(request):
    if request.method=="POST":
        un = request.POST["username"]
        pwd = request.POST["password"]

        user = authenticate(username=un,password=pwd)
        if user:
            login(request,user)
            if user.is_superuser:
                return HttpResponseRedirect("/admin")
            else:
                res = HttpResponseRedirect("/cust_dashboard")
                if "rememberme" in request.POST:
                    res.set_cookie("user_id",user.id)
                    res.set_cookie("date_login",datetime.now())
                return res
            # if user.is_active:
            #     return HttpResponseRedirect("/cust_dashboard")
                
        else:
            return render(request,"home.html",{"status":"Invalid Username or Password"})

    return HttpResponse("Called")

@login_required
def cust_dashboard(request):
    context = {}
    check = register_table.objects.filter(user__id=request.user.id)
    if len(check)>0:
        data = register_table.objects.get(user__id=request.user.id)
        context["data"] = data
    return render(request,"cust_dashboard.html",context)

@login_required
def seller_dashboard(request):
    return render(request,"seller_dashboard.html")
    
@login_required
def user_logout(request):
    logout(request)
    res =  HttpResponseRedirect("/")
    res.delete_cookie("user_id")
    res.delete_cookie("date_login")
    return res

def edit_profile(request):
    context = {}
    check = register_table.objects.filter(user__id=request.user.id)
    if len(check)>0:
        data = register_table.objects.get(user__id=request.user.id)
        context["data"]=data    
    if request.method=="POST":
        fn = request.POST["fname"]
        ln = request.POST["lname"]
        em = request.POST["email"]
        con = request.POST["contact"]
        age = request.POST["age"]
        ct = request.POST["city"]
        gen = request.POST["gender"]
        occ = request.POST["occ"]
        abt = request.POST["about"]

        usr = User.objects.get(id=request.user.id)
        usr.first_name = fn
        usr.last_name = ln
        usr.email = em
        usr.save()

        data.contact_number = con
        data.age = age
        data.city = ct
        data.gender = gen
        data.occupation = occ
        data.about = abt
        data.save()

        if "image" in request.FILES:
            img = request.FILES["image"]
            data.profile_pic = img
            data.save()


        context["status"] = "Changes Saved Successfully"
    return render(request,"edit_profile.html",context)

def change_password(request):
    context={}
    ch = register_table.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        data = register_table.objects.get(user__id=request.user.id)
        context["data"] = data
    if request.method=="POST":
        current = request.POST["cpwd"]
        new_pas = request.POST["npwd"]
        
        user = User.objects.get(id=request.user.id)
        un = user.username
        check = user.check_password(current)
        if check==True:
            user.set_password(new_pas)
            user.save()
            context["msz"] = "Password Changed Successfully!!!"
            context["col"] = "alert-success"
            user = User.objects.get(username=un)
            login(request,user)
        else:
            context["msz"] = "Incorrect Current Password"
            context["col"] = "alert-danger"

    return render(request,"change_password.html",context)


def add_product_view(request):
    context={}
    ch = register_table.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        data = register_table.objects.get(user__id=request.user.id)
        context["data"] = data
    form = add_product_form()
    if request.method=="POST":
        form = add_product_form(request.POST,request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            login_user =User.objects.get(username=request.user.username)
            data.seller = login_user
            data.save()
            context["status"] ="{} Added Successfully".format(data.product_name)

    context["form"] = form

    return render(request,"addproduct.html",context)

def my_products(request):
    context = {}
    ch = register_table.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        data = register_table.objects.get(user__id=request.user.id)
        context["data"] = data
        
    all = add_product.objects.filter(seller__id=request.user.id).order_by("-id")
    context["products"] = all
    return render(request,"myproducts.html",context)

def single_product(request):
    context = {}
    id = request.GET["pid"]
    obj = add_product.objects.get(id=id)
    context["product"] = obj
    return render(request,"single_product.html",context)

def update_product(request):
    context ={}
    cats = Category.objects.all().order_by("cat_name")
    context["category"] = cats

    pid = request.GET["pid"]
    product = get_object_or_404(add_product,id=pid)
    context["product"] = product

    if request.method=="POST":
        pn = request.POST["pname"]
        ct_id = request.POST["pcat"]
        pr = request.POST["pp"]
        sp = request.POST["sp"]
        des = request.POST["des"]
        
        cat_obj = Category.objects.get(id=ct_id)

        product.product_name =pn
        product.product_category =cat_obj
        product.product_price =pr
        product.sale_price =sp
        product.details =des
        if "pimg" in request.FILES:
            img = request.FILES["pimg"]
            product.product_image = img
        product.save()
        context["status"] = "Changes Saved Successfully"
        context["id"] = pid
    return render(request,"update_product.html",context)

def delete_product(request):
    context = {}
    if "pid" in request.GET:
        pid = request.GET["pid"]
        prd = get_object_or_404(add_product, id=pid)
        context["product"] = prd

        if "action" in request.GET:
            prd.delete()
            context["status"] = str(prd.product_name)+" removed Successfully!!!"
    return render(request,"deleteproduct.html",context)

def all_products(request):
    context = {}
    cats = Category.objects.all().order_by("cat_name")
    context["category"] = cats
    all_products = add_product.objects.all().order_by("product_name")
    context["products"] = all_products
    if "qry" in request.GET:
        q = request.GET["qry"]
        # p = request.GET["price"]
        prd = add_product.objects.filter(Q(product_name__icontains=q)|Q(product_category__cat_name__contains=q))
        # prd = add_product.objects.filter(Q(product_name__icontains=q)& Q(sale_price__lt=p))
        # prd = add_product.objects.filter(product_name__contains=q)
        context["products"] = prd   
        context["abcd"]="search"
    if "cat" in request.GET:
        cid = request.GET["cat"]
        prd = add_product.objects.filter(product_category__id=cid)
        context["products"] = prd   
        context["abcd"]="search"

    return render(request,"allproducts.html",context)

def sendemail(request):
    context = {}
    ch = register_table.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        data = register_table.objects.get(user__id=request.user.id)
        context["data"] = data

    if request.method=="POST":
    
        rec = request.POST["to"].split(",")
        print(rec)
        sub = request.POST["sub"]
        msz = request.POST["msz"]

        try:
            em = EmailMessage(sub,msz,to=rec)
            em.send()
            context["status"] = "Email Sent"
            context["cls"] = "alert-success"
        except:
            context["status"] = "Could not Send, Please check Internet Connection / Email Address"
            context["cls"] = "alert-danger"
    return render(request,"sendemail.html",context  )

def forgotpass(request):
    context = {}
    if request.method=="POST":
        un = request.POST["username"]
        pwd = request.POST["npass"]

        user = get_object_or_404(User,username=un)
        user.set_password(pwd)
        user.save()

        login(request,user)
        if user.is_superuser:
            return HttpResponseRedirect("/admin")
        else:
            return HttpResponseRedirect("/cust_dashboard")
        # context["status"] = "Password Changed Successfully!!!"

    return render(request,"forgot_pass.html",context)

import random

def reset_password(request):
    un = request.GET["username"]
    try:
        user = get_object_or_404(User,username=un)
        otp = random.randint(1000,9999)
        msz = "Dear {} \n{} is your One Time Password (OTP) \nDo not share it with others \nThanks&Regards \nMyWebsite".format(user.username, otp)
        try:
            email = EmailMessage("Account Verification",msz,to=[user.email])
            email.send()
            return JsonResponse({"status":"sent","email":user.email,"rotp":otp})
        except:
            return JsonResponse({"status":"error","email":user.email})
    except:
        return JsonResponse({"status":"failed"})

def add_to_cart(request):
    context={}
    items = cart.objects.filter(user__id=request.user.id,status=False)
    context["items"] = items

    if request.user.is_authenticated:
        if request.method=="POST":
            pid = request.POST["pid"]
            qty = request.POST["qty"]
            is_exist = cart.objects.filter(product__id=pid,user__id=request.user.id,status=False)
            if len(is_exist)>0:
                context["msz"] = "Item Already Exists in Your Cart"
                context["cls"] = "alert alert-warning"
            else:    
                product =get_object_or_404(add_product,id=pid)
                usr = get_object_or_404(User,id=request.user.id)
                c = cart(user=usr,product=product,quantity=qty)
                c.save()
                context["msz"] = "{} Added in Your Cart".format(product.product_name)
                context["cls"] = "alert alert-success"
    else:
        context["status"] = "Please Login First to View Your Cart"
    return render(request,"cart.html",context)

def get_cart_data(request):
    items = cart.objects.filter(user__id=request.user.id, status=False)
    sale,total,quantity =0,0,0
    for i in items:
        sale += float(i.product.sale_price)*i.quantity
        total += float(i.product.product_price)*i.quantity
        quantity+= int(i.quantity)

    res = {
        "total":total,"offer":sale,"quan":quantity,
    }
    return JsonResponse(res)

def change_quan(request):
    if "quantity" in request.GET:
        cid = request.GET["cid"]
        qty = request.GET["quantity"]
        cart_obj = get_object_or_404(cart,id=cid)
        cart_obj.quantity = qty
        cart_obj.save()
        return HttpResponse(cart_obj.quantity)

    if "delete_cart" in request.GET:
        id = request.GET["delete_cart"]
        cart_obj = get_object_or_404(cart,id=id)
        cart_obj.delete()
        return HttpResponse(1)

from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings 

def process_payment(request):
    items = cart.objects.filter(user_id__id=request.user.id,status=False)
    products=""
    amt=0
    inv = "INV10001-"
    cart_ids = ""
    p_ids =""
    for j in items:
        products += str(j.product.product_name)+"\n"
        p_ids += str(j.product.id)+","
        amt += float(j.product.sale_price)
        inv +=  str(j.id)
        cart_ids += str(j.id)+","

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': str(amt),
        'item_name': products,
        'invoice': inv,
        'notify_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format("127.0.0.1:8000",
                                              reverse('payment_cancelled')),
    }
    usr = User.objects.get(username=request.user.username)
    ord = Order(cust_id=usr,cart_ids=cart_ids,product_ids=p_ids)
    ord.save()
    ord.invoice_id = str(ord.id)+inv
    ord.save()
    request.session["order_id"] = ord.id
    
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'process_payment.html', {'form': form})

def payment_done(request):
    if "order_id" in request.session:
        order_id = request.session["order_id"]
        ord_obj = get_object_or_404(Order,id=order_id)
        ord_obj.status=True
        ord_obj.save()
        
        for i in ord_obj.cart_ids.split(",")[:-1]:
            cart_object = cart.objects.get(id=i)
            cart_object.status=True
            cart_object.save()
    return render(request,"payment_success.html")

def payment_cancelled(request):
    return render(request,"payment_failed.html")

def order_history(request):
    context = {}
    ch = register_table.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        data = register_table.objects.get(user__id=request.user.id)
        context["data"] = data

    all_orders = []
    orders = Order.objects.filter(cust_id__id=request.user.id).order_by("-id")
    for order in orders:
        products = []
        for id in order.product_ids.split(",")[:-1]:
            pro = get_object_or_404(add_product, id=id)
            products.append(pro)
        ord = {
            "order_id":order.id,
            "products":products,
            "invoice":order.invoice_id,
            "status":order.status,
            "date":order.processed_on,
        }
        all_orders.append(ord)
    context["order_history"] = all_orders
    return render(request,"order_history.html",context)