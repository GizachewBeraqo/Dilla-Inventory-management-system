from django.contrib import admin
from .models import Product,Order,Handover,Model20Nonfixedrequest,Propertyreturn,Model20fixedrequest,Approval,Approval
#from .models import Admin

#from django.contrib.auth.models import Group


admin.site.site_header = 'Dilla University Inventory Management Dashboard'

#admin.site.register(Approval)
#admin.site.register(Task)
@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('productname', 'model', 'serialNo', 'category', 'quantity', 'unitprice', 'totalprice')
    search_fields = ('productname', 'model', 'serialNo')
    list_filter = ('category',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('serviceprovided', 'productname', 'category', 'detailed_description', 'measurement',
                  'OfficialsRemarkforRequest', 'NumberofItems', 'PriceofEach', 'PropertiesNow',
                  'Remark', 'totalcost', 'supportdocument')
    search_fields = ('serviceprovided', 'productname')
    list_filter = ('category',) 

@admin.register(Handover)
class HandoverAdmin(admin.ModelAdmin):
    list_display = ('productname', 'measurement', 'NumberofItems', 'PriceofEach','totalcost','serial_number','condition','Remark','supportdocument')

@admin.register(Model20Nonfixedrequest)
class Model20NonfixedrequestAdmin(admin.ModelAdmin):
   list_display = ('productname','detailed_description','measurement','NumberofItems','PriceofEach','totalcost')


@admin.register(Model20fixedrequest)
class Model20fixedrequestAdmin(admin.ModelAdmin):
   list_display =('requestername','reason','productname','measurement','NumberofItems')

@admin.register(Propertyreturn)
class PropertyreturnAdmin(admin.ModelAdmin):
   list_display = ['productname','measurement','quantity','Condition_of_property_recently','PriceofEach','totalcost'] 

@admin.register(Approval)
class ApprovalAdmin(admin.ModelAdmin):
    class Meta:
        model = Approval
        fields = ('approver_name', 'date_of_approval')







