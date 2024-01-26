from django.urls import path
from . import views
#from .views import admin_approval
from django.contrib import admin
from .views import create_superuser
from .views import delete_superuser
from . import routing
from django.urls import include, path
from django.urls import path, include
from channels.routing import ProtocolTypeRouter, URLRouter

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from django.core.asgi import get_asgi_application


urlpatterns = [
    path('mytemplate/', views.mytemplate, name='dashboard-mytemplate'),
    path('users/', views.users, name='dashboard-users'),
    path('users/detail/<int:pk>/', views.users_detail, name='dashboard-users_detail'),
    path('product/', views.product, name='dashboard-product'),
    path('order/', views.order, name='dashboard-order'),
    path('users_index/', views.users_index, name='dashboard-users_index'),
    path('product/delete/<int:pk>/', views.product_delete, name='dashboard-product_delete'),
    path('product/update/<int:pk>/', views.product_update, name='dashboard-product_update'),
    path('handover/', views.handover, name='dashboard-handover'),
    path('model20request/', views.model20request, name='dashboard-model20request'),
    path('return/', views.Preturn, name='dashboard-return'),
    path('fixed/', views.fixed, name='dashboard-fixed'),
    path('handoverer/', views.handoverer, name='dashboard-handoverer'),
    path('returner/', views.returner, name='dashboard-returner'),
    path('requester1/', views.requester1, name='dashboard-requester1'),
    path('requester2/', views.requester2, name='dashboard-requester2'),
    path('create_superuser/', create_superuser, name='create_superuser'),
    path('delete_superuser/', views.delete_superuser, name='delete_superuser'),
    path('approval/',views.approval_view, name='dashboard-approval'),
    #path('approval/', views.approval_page, name='dashboard-approval'),
    
    #path('approval/', include('dashboard.urls')),
    path('napproval/',views.napproval_view, name='dashboard-napproval'),
    path('handoverapp/',views.handoverapp_view, name='dashboard-handoverapp'),
    path('old/',views.old_view, name='dashboard-old'),
    path('napproval/',views.napproval_view, name='dashboard-napproval'),
    path('save_approval/',views.save_approval, name='save_approval'),
    path('approval/',views.approval_page, name='dashboard-approval'),

]




