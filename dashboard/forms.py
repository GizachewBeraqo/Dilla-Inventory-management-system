from django import forms
from .models import Product, Order,Handover,Model20Nonfixedrequest,Propertyreturn,Model20fixedrequest,Approval
from django.contrib.auth.forms import UserCreationForm


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['productname', 'model', 'serialNo', 'category', 'quantity', 'unitprice', 'totalprice']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['serviceprovided', 'productname', 'category', 'detailed_description', 'measurement',
                  'OfficialsRemarkforRequest', 'NumberofItems', 'PriceofEach', 'PropertiesNow',
                  'Remark', 'totalcost', 'supportdocument']
class HandoverForm(forms.ModelForm):
    class Meta:
          model = Handover
          fields = ['productname', 'measurement', 'NumberofItems', 'PriceofEach','totalcost','serial_number','condition','Remark','supportdocument']

class Model20NonfixedrequestForm(forms.ModelForm):
    class Meta:
          model = Model20Nonfixedrequest
          fields = ['productname','detailed_description','measurement','NumberofItems','PriceofEach','totalcost']

class Model20fixedrequestForm(forms.ModelForm):
    class Meta:
          model = Model20fixedrequest
          fields =  ['requestername','reason','productname','measurement','NumberofItems']




class PropertyreturnForm(forms.ModelForm):
    class Meta:
          model = Propertyreturn
          fields =['productname','measurement','quantity','Condition_of_property_recently','PriceofEach','totalcost'] 
          
         


class ApprovalForm(forms.ModelForm):
    class Meta:
        model = Approval
        fields = ['approver_name', 'date_of_approval']