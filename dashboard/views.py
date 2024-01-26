from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProductForm,OrderForm
from .models import Product,Order,Handover, Model20Nonfixedrequest,Propertyreturn,Model20fixedrequest,Approval
from django.contrib.auth.models import User
from .forms import HandoverForm,Model20NonfixedrequestForm,PropertyreturnForm,Model20fixedrequestForm,ApprovalForm
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib import messages
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.utils import timezone
from datetime import datetime
from django.utils import timezone
from decimal import Decimal, InvalidOperation
@login_required
def mytemplate(request):
    
   orders=Order.objects.all()
   products=Product.objects.all()
   if request.method=='POST':
        form=OrderForm(request.POST)
   else:
        form=OrderForm()
        if form.is_valid():
            instance=form.save(commit=False)
            instance.staff=request.user
            instance.save()
            return redirect('dashboard-mytemplate')
   context = {
    'orders': orders,
    'form': form,
    'products':products,
}
   return render(request, 'dashboard/mytemplate.html', context)
@login_required
def users(request):
    
    workers=User.objects.all()
    context={
        'workers':workers,
    }
    return render(request, 'dashboard/users.html',context)
@login_required
def users_detail(request,pk):
    workers=User.objects.get(id=pk)
    context={
        'workers':workers,
    }

    return render(request, 'dashboard/users_detail.html',context)
def users_detail(request, pk):
    user = User.objects.filter(groups=2)
    user_count =user.count()
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    users = User.objects.get(id=pk)
    context = {
        'users': users,
        'user_count': user_count,
        'product_count': product_count,
        'order_count': order_count,

    }
    return render(request, 'dashboard/users_detail.html', context)
def format_number(value):
    try:
        if value is None or not isinstance(value, Decimal):
            return None
        
        value = value.quantize(Decimal('0.00'))
        return value
    except InvalidOperation:
        return None
@login_required
def product(request):
   
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm()

    items = Product.objects.all()
    decimal_value = Decimal('10.1234')
    formatted_value = format_number(decimal_value)
    print(formatted_value) 

    context = {
        'items': items,
        'form': form,
    }

    return render(request, 'dashboard/product.html', context)
@login_required
def order(request):
    orders=Order.objects.all()
    context = {
        'orders':orders,
    }
    return render(request, 'dashboard/order.html',context)


@login_required
def users_index(request):
    orders = Order.objects.all()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-mytemplate')
    else:
        form = OrderForm()

    context = {
        'orders': orders,
        'form': form,
    }
    return render(request, 'dashboard/users_index.html', context)
    
@login_required
def product_delete(request, pk):
    item = Product(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

@login_required
def product_update(request, pk):
    item =Product.objects.get(id=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
           form.save()
           return redirect('dashboard-product')
    else:
     form = ProductForm(instance=item)

     context = {
        'form': form,
    }
    return render(request, 'dashboard/product_update.html', context)


    
@login_required
def order_update(request, pk):
    order =Order.objects.get(id=pk)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
           form.save()
           return redirect('dashboard-users_index')
    else:
     form = OrderForm(instance=order)

     context = {
        'form': form,
    }
    return render(request, 'dashboard/order_update.html', context)

def handover(request):
    if request.method == 'POST':
        form = HandoverForm(request.POST, request.FILES)
        if form.is_valid():
           # handover = form.save()  # Save the form data to the database
            # Optionally, you can perform additional actions or redirect to a success page
            return redirect('dashboard-users_index')
    else:
        form = HandoverForm()
    
    # Retrieve existing handovers from the database
    handovers = Handover.objects.all()  # Assuming you have a Handover model defined
    
    return render(request, 'dashboard/handover.html', {'form': form, 'handovers': handovers})



def model20request(request):
    if request.method == 'POST':
        form = Model20Nonfixedrequest(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard-users_index')
    else:
        form = Model20NonfixedrequestForm()
    
    Model20requests = Model20Nonfixedrequest.objects.all()
    context = {
        'form': form,
        'Model20requests ': Model20requests
    }
    return render(request, 'dashboard/model20request.html', context)
@login_required
def requester2(request):
    if request.method == 'POST':
        form =  Model20NonfixedrequestForm(request.POST, request.FILES)
        if form.is_valid():
            requester = form.save()  # Save the form data to the database
            return redirect('dashboard-model20request')  # Redirect to the same page to display the updated table
    else:
        form =  Model20NonfixedrequestForm()
    
    Model20requests = Model20Nonfixedrequest.objects.all()  # Retrieve all stored handovers from the database
    
    return render(request, 'dashboard/requester2.html', {'form': form, 'Model20requests': Model20requests})


def Preturn(request):
    if request.method == 'POST':
        form = PropertyreturnForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard-users_index')
    else:
        form = PropertyreturnForm()
    
    Preturns = Propertyreturn.objects.all()
    context = {
        'form': form,
        'Preturns ': Preturns
    }
    return render(request, 'dashboard/return.html', context)
def returner(request):
    if request.method == 'POST':
        form =   PropertyreturnForm(request.POST, request.FILES)
        if form.is_valid():
            returner = form.save()  # Save the form data to the database
            return redirect('dashboard-return')  # Redirect to the same page to display the updated table
    else:
        form =   PropertyreturnForm()
    
    Preturns =  Propertyreturn.objects.all()  # Retrieve all stored handovers from the database
    
    return render(request, 'dashboard/returner.html', {'form': form, 'Preturns': Preturns})


def fixed(request):
    if request.method == 'POST':
        form = Model20fixedrequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard-users_index')
    else:
        form = Model20fixedrequestForm()
    
    fixeds = Model20fixedrequest.objects.all()
    context = {
        'form': form,
        'fixeds ': fixeds
    }
    return render(request, 'dashboard/fixed.html', context)

@login_required
def requester1(request):
    if request.method == 'POST':
        form =  Model20fixedrequestForm(request.POST, request.FILES)
        if form.is_valid():
            requester = form.save()  # Save the form data to the database
            return redirect('dashboard-fixed')  # Redirect to the same page to display the updated table
    else:
        form =  Model20fixedrequestForm()
    
    fixeds = Model20fixedrequest.objects.all()  # Retrieve all stored handovers from the database
    
    return render(request, 'dashboard/requester1.html', {'form': form, 'fixeds': fixeds})




@login_required
def handoverer(request):
    if request.method == 'POST':
        form = HandoverForm(request.POST, request.FILES)
        if form.is_valid():
            handover = form.save()  # Save the form data to the database
            return redirect('dashboard-handover')  # Redirect to the same page to display the updated table
    else:
        form = HandoverForm()
    
    handovers = Handover.objects.all()  # Retrieve all stored handovers from the database
    
    return render(request, 'dashboard/handoverer.html', {'form': form, 'handovers': handovers})
    

def create_superuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            
            return render(request, 'dashboard/create_superuser.html', {'error': 'Username or email already exists'})

        
        superuser = User.objects.create_superuser(username=username, email=email, password=password)

        
        superuser.save()

       
        return redirect('dashboard-mytemplate')

    return render(request, 'dashboard/create_superuser.html')



@csrf_exempt
def delete_superuser(request):
    if request.method == "DELETE":
        username = request.GET.get("username")

        try:
            user = User.objects.get(username=username)
            if user.is_superuser:
                user.delete()
                return JsonResponse({"message": "Superuser deleted successfully!"})
            else:
                return JsonResponse({"error": "The specified user is not a superuser"})
        except User.DoesNotExist:
           return JsonResponse({"error": "User not found"})

    return render(request, "dashboard/delete_superuser.html")


def approval_view(request):
    if request.method == 'POST':
        # Process the form submission
        approver_name = request.POST.get('approver-name')
        date_of_approval = timezone.now()
        notification_message = f"Property Approved by {approver_name} on {date_of_approval}"
        

        return HttpResponse("Property approved")

    else:
        # Render the approval page
        approvers = ['Old Property Store Head', 'Garage Technician', 'Property Control Employee 1', 'Property Control Employee 2', 'Property Management Service Head']
        context = {'approvers': approvers}
        return render(request, 'dashboard/approval.html', context)

def napproval_view(request):
    if request.method == 'POST':
        # Process the form submission
        approver_name = request.POST.get('approver-name')
        date_of_approval = timezone.now()
        notification_message = f"Property Approved by {approver_name} on {date_of_approval}"
        

        return HttpResponse("Property approved")

    else:
        # Render the approval page
        approvers = ['Old Property Store Head', 'Garage Technician', 'Property Control Employee 1', 'Property Control Employee 2', 'Property Management Service Head']
        context = {'approvers': approvers}
        return render(request, 'dashboard/napproval.html', context)
    
def handoverapp_view(request):
    if request.method == 'POST':
        # Process the form submission
        approver_name = request.POST.get('approver-name')
        date_of_approval = timezone.now()
        notification_message = f"Property Approved by {approver_name} on {date_of_approval}"
        
        return HttpResponse("Property approved")

    else:
        # Render the approval page
        approvers = ['Old Property Store Head', 'Garage Technician', 'Property Control Employee 1', 'Property Control Employee 2', 'Property Management Service Head']
        context = {'approvers': approvers}
        return render(request, 'dashboard/handoverapp.html', context)
def old_view(request):
    if request.method == 'POST':
        # Process the form submission
        approver_name = request.POST.get('approver-name')
        date_of_approval = timezone.now()
        notification_message = f"Property Approved by {approver_name} on {date_of_approval}"
       

        return HttpResponse("Property approved")

    else:
        # Render the approval page
        approvers = ['Old Property Store Head', 'Garage Technician', 'Property Control Employee 1', 'Property Control Employee 2', 'Property Management Service Head']
        context = {'approvers': approvers}
        return render(request, 'dashboard/old.html', context)
    
def approval(request):
    return render(request, 'dashboard/approval.html')

def save_approval(request):
    if request.method == 'POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            form.save()
            # Handle form submission success
        else:
            # Handle form validation errors
            pass
    else:
        form = ApprovalForm()
    
    context = {'form': form}
    return render(request, 'dashboard/approval.html', context)
def approval_page(request):
    approvals = Approval.objects.all()
    approval_counts = {}
    for approval in approvals:
        if approval.approver_name in approval_counts:
            approval_counts[approval.approver_name] += 1
        else:
            approval_counts[approval.approver_name] = 1
    
    context = {
        'approval_counts': approval_counts
    }
    
    return render(request, 'dashboard/approval.html', context)