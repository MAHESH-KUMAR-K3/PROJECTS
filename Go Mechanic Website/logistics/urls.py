"""logistics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from logapp import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name="index"),
    path('about/', v.about, name="about"),
    path('contact/', v.contact, name="contact"),
    path('blog/', v.blog, name="blog"),
    path('industries/', v.industries, name="industries"),
    path('services/', v.services, name="services"),

    #Customer urls
    path('customer/', v.customer, name="customer"),
    path('customer_loginpage/', v.customer_loginpage, name="customer_loginpage"),
    path('regpage/', v.regpage, name="regpage"),
    path('reg/', v.reg, name="reg"),
    path('customer_login/', v.customer_login, name="customer_login"),
    path('customer_change/', v.customer_change, name="customer_change"),
    path('customer_display/', v.customer_display, name="customer_display"),
    path('customer_delete/<int:id>', v.customer_delete, name="customer_delete"),
    path('customer_edit/<int:id>', v.customer_edit, name="customer_edit"),
    path('customer_update/', v.customer_update, name="customer_update"),
    path('customer_logout/', v.customer_logout, name="customer_logout"),

    #Mechanic urls
    path('mechanic/', v.mechanic, name="mechanic"),
    path('mechanic_loginpage/', v.mechanic_loginpage, name="mechanic_loginpage"),
    path('mechanic_regpage/', v.mechanic_regpage, name="mechanic_regpage"),
    path('mechanic_reg/', v.mechanic_reg, name="mechanic_reg"),
    path('mechanic_login/', v.mechanic_login, name="mechanic_login"),
    path('mechanic_change/', v.mechanic_change, name="mechanic_change"),
    path('mechanic_display/', v.mechanic_display, name="mechanic_display"),
    path('mechanic_delete/<str:email>', v.mechanic_delete, name="mechanic_delete"),
    path('mechanic_edit/<str:email>', v.mechanic_edit, name="mechanic_edit"),
    path('mechanic_update/', v.mechanic_update, name="mechanic_update"),
    path('viewmechanic/', v.viewmechanic, name="viewmechanic"),
    path('book/<str:email>', v.book, name="book"),
    path('book_update/', v.book_update, name="book_update"),
    path('review/<str:email>', v.review, name="review"),
    path('review_update/', v.review_update, name="review_update"),
    path('mechanic_logout/', v.mechanic_logout, name="mechanic_logout"),
    path('booked_slots/', v.booked_slots, name="booked_slots"),
    path('slot_approve/<int:slot_id>', v.slot_approve, name="slot_approve"),
    path('slot_reject/<int:slot_id>', v.slot_reject, name="slot_reject"),
    path('mechanic_booked_slots/', v.mechanic_booked_slots, name="mechanic_booked_slots"),

    #Admin urls
    path('administration/', v.administration, name="administration"),
    path('admin_login/', v.admin_login, name="admin_login"),
    path('view_customer/', v.view_customer, name="view_customer"),
    path('admin_viewmechanic/', v.admin_viewmechanic, name="admin_viewmechanic"),
    path('admin_logout/', v.admin_logout, name="admin_logout"),
    path('view_bookings/', v.view_bookings, name="view_bookings"),
    path('view_reviews/', v.view_reviews, name="view_reviews"),
    path('admin_customer_delete/<str:email>', v.admin_customer_delete, name="admin_customer_delete"),
    path('admin_mechanic_delete/<str:email>', v.admin_mechanic_delete, name="admin_mechanic_delete"),

]
