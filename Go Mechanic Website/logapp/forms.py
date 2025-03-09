from django import forms
from logapp.models import Contact, Customer, Mechanic, Admin, Book, Review
class ContactForms(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class CustomerForms(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class MechanicForms(forms.ModelForm):
    class Meta:
        model = Mechanic
        fields = "__all__"

class AdminForms(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"

class BookForms(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


class ReviewForms(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

