from django.shortcuts import render,redirect
from logapp.forms import ContactForms, CustomerForms, MechanicForms, AdminForms, BookForms, ReviewForms
from logapp.models import Contact, Customer, Mechanic, Admin, Book, Review

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def about(request):
    return render(request, "about.html", {})

def contact(request):
    if request.method == "POST":
        print("hii")
        form = ContactForms(request.POST)
        print("hii")
        if form.is_valid():
            form.save()
        return render(request, "contact.html", {"msg": ""})
    return render(request, "contact.html", {})

def blog(request):
    return render(request, "blog.html", {})

def industries(request):
    return render(request, "industries.html", {})

def services(request):
    return render(request, "services.html", {})

#customer views

def customer(request):
    return render(request, "customer.html", {})


def customer_loginpage(request):
    return render(request, "customer_login.html", {"msg": ""})

def regpage(request):
    return render(request, "reg.html", {})

def reg(request):
    if request.method == "POST":
        form = CustomerForms(request.POST)
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                print(e)
    return render(request, "customer_login.html", {"msg": ""})

def customer_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email, " ", password)
        customer = Customer.objects.filter(email=email, password=password)
        if customer.exists():
            request.session["email"] = email
            return render(request, "customer.html", {"msg": email})
    else:
        return render(request, "customer_login.html", {"msg": "email or password not exist"})
    return render(request, "customer_login.html", {"msg": ""})

def is_customer_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False
def customer_change(request):
    if is_customer_login(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]
            try:
                customer = Customer.objects.get(email=email, password=password)
                customer.password = newpassword
                customer.save()
                msg = "password updated successfully"
                return render(request, "customer_login.html", {"msg": msg})
            except:
                msg = "inavlid data"
                return render(request, "customer_change.html", {"msg": msg})
        return render(request, "customer_change.html", {})
    else:
        return render(request, "customer_change.html", {})

def customer_display(request):
    email = request.session["email"]
    customer = Customer.objects.get(email=email)
    print("hello")
    return render(request, "customer_edit.html", {"customer": customer})

def customer_delete(request, email):
    customer = Customer.objects.get(email=email)
    customer.delete()
    return redirect("/reg")

def customer_edit(request, email):
    customer = Customer.objects.get(email=email)
    return render(request, "customer_edit.html", {"customer": customer})


def customer_update(request):
    if request.method == "POST":
        customerid = request.POST["email"]
        customer = Customer.objects.get(email=customerid)
        customer = CustomerForms(request.POST, instance=customer)
        print(customer.errors)
        if customer.is_valid():
            print(customer.errors)
            customer.save()
        return redirect("/customer_display")
    return redirect("/customer_display")

def viewmechanic(request):
    mechanic = Mechanic.objects.all()
    print("hello")
    return render(request, "viewmechanic.html", {"mechanic": mechanic})





def book(request, email):
    email1 = request.session['email']
    customer = Customer.objects.get(email=email1)
    mechanic = Mechanic.objects.get(email=email)
    if request.method == "POST":
        print("hii")
        print(customer.email)
        book = BookForms(request.POST)
        print("hii", book.errors)
        if book.is_valid():
            book.save()
        return render(request, "customer.html", {"msg": "success", "mail": mechanic.email,  "customer": customer.email})
    return render(request, "book.html", {"mail": mechanic.email, "customer": email1})

def book_update(request):
    if request.method == "POST":
        bookemail = request.POST["email"]
        book = Book.objects.get(email=bookemail)
        book = BookForms(request.POST, instance=book)
        if book.is_valid():
            book.save()
        return redirect("/viewmechanic")
    return redirect("/viewmechanic")


def review(request,email):
    email1 = request.session['email']
    customer = Customer.objects.get(email=email1)
    mechanic = Mechanic.objects.get(email=email)
    if request.method == "POST":
        print("hii")
        print(customer.email)
        review = ReviewForms(request.POST)
        print("hii", review.errors)
        if review.is_valid():
            review.save()
        return render(request, "review.html", {"msg": "success", "email": mechanic.email,  "customer": customer.email})
    return render(request, "review.html", {"email": mechanic.email, "customer": customer.email})


def review_update(request):
    if request.method == "POST":
        reviewemail = request.POST["email"]
        review = Review.objects.get(email=reviewemail)
        review = ReviewForms(request.POST, instance=review)
        if review.is_valid():
            review.save()
        return redirect("/viewmechanic")
    return redirect("/viewmechanic")


def customer_logout(request):
    if request.session.has_key("email"):
        email = request.session["email"]
    return render(request, "customer_login.html", {"email": email})


def mechanic_booked_slots(request):
    email = request.session["email"]
    customer = Book.objects.filter(customer_id=email)
    return render(request, "my_slots.html", {"customers": customer})

#mechanic views

def mechanic(request):
    return render(request, "mechanic.html", {})

def mechanic_loginpage(request):
    return render(request, "mechanic_loginpage.html", {"msg": ""})

def mechanic_regpage(request):
    return render(request, "mechanic_reg.html", {})

def mechanic_reg(request):
    if request.method == "POST":
        form = MechanicForms(request.POST)
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                print(e)
    return render(request, "mechanic_login.html", {"msg": ""})

def mechanic_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email, " ", password)
        mechanic = Mechanic.objects.filter(email=email, password=password)
        if mechanic.exists():
            request.session["email"] = email
            return render(request, "mechanic.html", {"msg": email})
    else:
        return render(request, "mechanic_login.html", {"msg": "email or password not exist"})
    return render(request, "mechanic_login.html", {"msg": ""})

def is_mechanic_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False
def mechanic_change(request):
    if is_mechanic_login(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]

            try:
                mechanic = Mechanic.objects.get(email=email, password=password)
                mechanic.password = newpassword
                mechanic.save()
                msg = "password updated successfully"
                return render(request, "mechanic_login.html", {"msg": msg})
            except:
                msg = "inavlid data"
                return render(request, "mechanic_change.html", {"msg": msg})
        return render(request, "mechanic_change.html", {})
    else:
        return render(request, "customer_change.html", {})

def mechanic_display(request):
    email = request.session["email"]
    mechanic = Mechanic.objects.get(email=email)
    print("hello")
    return render(request, "mechanic_display.html", {"mechanic": mechanic})

def mechanic_delete(request, email):
    mechanic = Mechanic.objects.get(email=email)
    mechanic.delete()
    return redirect("/reg")

def mechanic_edit(request, email):
    mechanic = Mechanic.objects.get(email=email)
    return render(request, "mechanic_edit.html", {"mechanic": mechanic})

def mechanic_update(request):
    if request.method == "POST":
        mechanicid = request.POST["id"]
        mechanic = Customer.objects.get(id=mechanicid)
        mechanic = CustomerForms(request.POST, instance=mechanic)
        if mechanic.is_valid():
            mechanic.save()
        return redirect("/mechanic_display")
    return redirect("/mechanic_display")

def mechanic_logout(request):
    if request.session.has_key("email"):
        email = request.session["email"]
    return render(request, "mechanic_login.html", {"email": email})

def booked_slots(request):
    email = request.session["email"]
    booked = Book.objects.filter(mechanic_id=email)
    return render(request, "booked_slots.html", {"booked": booked})


def slot_approve(request, slot_id):
    approve = Book.objects.get(id=slot_id)
    approve.slot_status = 'approved'
    approve.save()
    return render(request, "mechanic.html", {})


def slot_reject(request, slot_id):
    reject = Book.objects.get(id=slot_id)
    reject.job_status = 'rejected'
    reject.save()
    return render(request, "mechanic.html", {})


#admin views

def administration(request):
    return render(request, "administration.html", {})

def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username, " ", password)
        admin = Admin.objects.all()
        if admin.exists():
            print("hello")
            request.session["username"] = username
            return render(request, "administration.html", {"msg": username})
        else:
            return render(request, "admin_login.html", {"msg": "email or password not exist"})
    return render(request, "admin_login.html", {"msg": ""})

def view_customer(request):
    customer = Customer.objects.all()
    print("hello")
    return render(request, "view_customer.html", {"customer": customer})

def view_mechanic(request):
    mechanic = Mechanic.objects.all()
    print("hello")
    return render(request, "view_mechanic.html", {"mechanic": mechanic})

def admin_logout(request):
    if request.session.has_key("username"):
        username = request.session["username"]
    return render(request, "admin_login.html", {"username": username})


def view_bookings(request):
    book = Book.objects.all()
    return render(request, "view_bookings.html", {"book": book})


def admin_viewmechanic(request):
    mechanic = Mechanic.objects.all()
    print("hello")
    return render(request, "view_mechanic.html", {"mechanic": mechanic})


def admin_customer_delete(request, email):
    customer = Customer.objects.get(email=email)
    customer.delete()
    return redirect("/administration")


def admin_mechanic_delete(request, email):
    mechanic = Mechanic.objects.get(email=email)
    mechanic.delete()
    return redirect("/administration")


def view_reviews(request):
    review = Review.objects.all()
    return render(request, "view_reviews.html", {"review": review})


