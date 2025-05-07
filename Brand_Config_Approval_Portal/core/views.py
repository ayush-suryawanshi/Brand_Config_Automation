from django.shortcuts import render,redirect,get_object_or_404
import json
from .models import Manager,Scheme,Email
from django.contrib.auth.decorators import login_required
#.............................................................................

def brand_email_selection(request,brand):
    brand = str(brand)
    emails = Email.objects.filter(brand=brand,processed=False,rejected=False)

    context = {
        'emails' : emails 
    }
    return render(request,'core/email_select.html',context=context)
#.............................................................................

#.............................................................................
def email_sku_list(request,email_id):
    schemes = Scheme.objects.filter(
    input_row__email_attachment__email__id=email_id
    )

    context = {
        'skus' : schemes
    }

    return render(request,'core/sku_list.html',context=context)


#..............................................................................

def sku_bank_list(request,sku_id):
    schemes = Scheme.objects.filter(sku=sku_id)

    banks = []
    for scheme in schemes:
        if scheme.bank_name not in banks:
            banks.append(scheme.emi_tenure)

    context = {
        'banks' : banks
    }

    return render(request,'core/bank_list.html')

#..............................................................................

def login_page(request):
    return render(request,'core/login.html')

#..............................................................................

def landing_page(request):
    return render(request,'core/landing_page.html')

#...............................................................................

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try: 
            try:
                user = Manager.objects.get(email=email)
            except Exception as e:
                print(f"The following exception took place : {e}")
                return redirect('/login/')
            
            # if User.objects.all(email=email).exists():

            if user.password == password:
                return redirect('/home/')

        except:
            return redirect('/login/')
        
#..................................................................................................


def individual_scheme(request,scheme_id):

    scheme_object = Scheme.objects.get(id=scheme_id)

    raw_json = scheme_object.input_row.jsonified_row_data
    output_json = scheme_object.jsonified_data

    raw_json = json.loads(raw_json) if raw_json else {}

    context = {
        'raw_json':raw_json,
        'output_json':output_json,
        'scheme' : scheme_object
        }
    
    return render(request,'core/individual_scheme_display.html',context=context)

#....................................................................................................


def scheme_approval(request,scheme_id):

    scheme = get_object_or_404(Scheme,id=scheme_id)
    scheme.is_apporved = True
    scheme.save()

    return redirect(f'/home/')

#......................................................................................................

def scheme_rejection(request,scheme_id):
    scheme = get_object_or_404(Scheme,id=scheme_id)
    scheme.is_apporved = False
    scheme.save()

    return redirect(f'/home/')
#.......................................................................................................

def confirm_scheme_edit(request,scheme_id):
    if request.method == 'POST':
        updated_scheme = request.POST.get('jsonInput')
        scheme = Scheme.objects.get(id=scheme_id)
        scheme.jsonified_data = updated_scheme
        scheme.save()

        print(f"The Output is : {scheme.jsonified_data}")

    return redirect(f'/home/')

#.......................................................................................................

def edit_scheme(request,scheme_id):
    
    scheme_object = Scheme.objects.get(id=scheme_id)

    raw_json = scheme_object.input_row.jsonified_row_data
    output_json = scheme_object.jsonified_data
    
    raw_json = json.loads(raw_json) if raw_json else {}
    # raw_json = extract_json_like_dicts(str(raw_json))
    # raw_json = dict(raw_json[0])

    context = {
        'raw_json':raw_json,
        'output_json':output_json,
        'scheme_id':scheme_id,
        'scheme':scheme_object
        }
    
    return render(request,'core/edit_scheme.html',context=context)

#...........................................................................................................
