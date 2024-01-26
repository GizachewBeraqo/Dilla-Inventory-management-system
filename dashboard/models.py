from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

# Create your models here.
MEASUREMENT_CHOICES = (
    ('GigaByte', 'GigaByte'),
    ('NumbersofItem', 'NumbersofItem'),
    ('Cartoon', 'Cartoon'),
    ('Meter', 'Meter'),
    ('inch','inch'),
)
SERVICES=(
    ('Request((for non fixed)','Request(for non fixed)'),
    ('Return to used(old fixed property)','Return to used(old fixed property)'),
    ('Handover(fixed-property)','Handover(fixed-property)'),
          )
STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

REQUEST_TYPE_CHOICES = (
        ('handover', 'Handover'),
        ('request', 'request'),
        ('return', 'return'),
    )
SERVICEPROVIDED_CHOICES = (
        ('request for non-fixed', 'Request for non-Fixed'),
        ('handover', 'Handover'),
        ('return old property', 'Return Old Property'),
)

CATEGORY_CHOICES = (
        ('fixed', 'Fixed'),
        ('non-fixed', 'Non-Fixed'),
    )
PROPERTIESNOW_CHOICES = (
        ('working', 'Working'),
        ('Notworking', 'NotWorking '),
    )
APPROVAL_CHOICES = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
)
CATEGORY= (
    ('fixed', 'fixed'),
    ('non-fixed', 'non-fixed'),
    
)

class Product(models.Model):
    productname = models.CharField( max_length=100,null=True)
    model= models.CharField( max_length=100,null=True,blank=True)
    serialNo = models.CharField( max_length=100,null=True,blank=True)
    category = models.CharField( max_length=20,choices=CATEGORY,null=True)
    quantity= models.PositiveIntegerField(null=True)
    unitprice = models.DecimalField(max_digits=10, decimal_places=2)
    totalprice = models.DecimalField(max_digits=10, decimal_places=2, default=('0.0'))
   
    def save(self, *args, **kwargs):
        self.totalprice = self.unitprice * self.quantity
        super(Product, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.productname
    class Meta:
        verbose_name_plural = 'Product'

def __str__(self):
    return f'{self.productname}-{self.quantity}'


class Order(models.Model):
    
    serviceprovided = models.CharField(max_length=100, choices=SERVICEPROVIDED_CHOICES)
    productname = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    detailed_description = models.TextField()
    measurement = models.CharField(max_length=100)
    OfficialsRemarkforRequest=models.TextField()
    NumberofItems = models.IntegerField(default=0)
    PriceofEach = models.DecimalField(max_digits=10, decimal_places=2)
    PropertiesNow=models.CharField(max_length=100, choices= PROPERTIESNOW_CHOICES)
    Remark = models.CharField(max_length=100)
    totalcost = models.DecimalField(max_digits=10, decimal_places=2, editable=True)
    supportdocument = models.FileField(upload_to='documents/')

    def save(self, *args, **kwargs):
        self.totalcost = self.PriceofEach* self.NumberofItems
        super(Order, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.productname
    class Meta:
        verbose_name_plural = 'Order'

def __str__(self):
    return f'{self.productname}-{self.NumberofItems}'
class Handover(models.Model):
    productname = models.CharField(max_length=100)
    measurement = models.CharField(max_length=100)
    NumberofItems = models.IntegerField()
    PriceofEach = models.DecimalField(max_digits=10, decimal_places=2)
    totalcost = models.DecimalField(max_digits=10, decimal_places=2)
    serial_number = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    Remark = models.TextField()
    supportdocument = models.FileField(upload_to='support_documents/')

    current_admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_approved = models.BooleanField(default=False)
     # Add fields for approval
    def save(self, *args, **kwargs):
        self.totalcost= self.PriceofEach * self.NumberofItems
        super(Handover, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.productname
    class Meta:
        verbose_name_plural = 'Handover'

def __str__(self):
    return f'{self.productname}-{self.NumberofItems}'
    

class Model20Nonfixedrequest(models.Model):
    productname=models.CharField(max_length=100)
    detailed_description=models.TextField()
    measurement=models.CharField(max_length=100)
    NumberofItems = models.IntegerField()
    PriceofEach = models.DecimalField(max_digits=10, decimal_places=2)
    totalcost = models.DecimalField(max_digits=10, decimal_places=2)
    def save(self, *args, **kwargs):
        self.totalcost = self.PriceofEach * self.NumberofItems
        super(Model20Nonfixedrequest, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.productname
    class Meta:
        verbose_name_plural = 'Model20Nonfixedrequest'

def __str__(self):
    return f'{self.productname}-{self.NumberofItems}'

class Model20fixedrequest(models.Model):
    requestername=models.CharField(max_length=100)
    reason=models.TextField()
    productname=models.CharField(max_length=100)
    measurement = models.CharField(max_length=100, choices=MEASUREMENT_CHOICES)
    NumberofItems = models.IntegerField()
   
    def __str__(self):
        return self.productname
    class Meta:
        verbose_name_plural = 'Model20fixedrequest'

def __str__(self):
    return f'{self.productname}-{self.NumberofItems}'

class Propertyreturn(models.Model):
    productname=models.CharField(max_length=100)
    measurement=models.CharField(max_length=100)
    quantity=models.IntegerField()
    Condition_of_property_recently = models.CharField(max_length=100, choices= PROPERTIESNOW_CHOICES)
    PriceofEach = models.DecimalField(max_digits=10, decimal_places=2)
    totalcost = models.DecimalField(max_digits=10, decimal_places=2)
    def save(self, *args, **kwargs):
        self.totalcost = self.PriceofEach * self.quantity
        super(Propertyreturn, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.productname
    class Meta:
        verbose_name_plural = 'Propertyreturn'

def __str__(self):
    return f'{self.productname}-{self.quantity}'


class Approval(models.Model):
    approver_name = models.CharField(max_length=100)
    date_of_approval = models.DateField()

    def __str__(self):
        return self.approver_name