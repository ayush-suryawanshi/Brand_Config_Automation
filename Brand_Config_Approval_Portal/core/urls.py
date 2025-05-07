from django.urls import path
from .views import *
#...................................................

urlpatterns = [
    path('login/',login_page,name='login_page'),
    path('login_user/',login_user,name='login_user'),
    path('home/',landing_page,name='home_page'),
    path('<str:brand>/email_selection/',brand_email_selection,name='email_selection'),
    path('sku_list/<uuid:email_id>',email_sku_list,name='sku_list'),
    path('scheme/<str:scheme_id>/',individual_scheme,name='individual_scheme'),
    path('edit/<str:scheme_id>/',edit_scheme,name='edit_scheme'),
    path('approve/<str:scheme_id>/',scheme_approval,name='approve_scheme'),
    path('reject/<str:scheme_id>/',scheme_rejection,name='reject_scheme'),
    path('confirm_edit/<str:scheme_id>',confirm_scheme_edit,name='scheme_edit_confirm')

]