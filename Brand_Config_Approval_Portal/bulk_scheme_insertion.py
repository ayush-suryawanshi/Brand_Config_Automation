import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Brand_Config_Approval_Portal.settings')
django.setup()

from core.models import Scheme
import pandas as pd 
#.......................................

data = []

source_file = "E:\Brand_Config_Automation_Gemini_Version\\scheme_dump_14_4_25.xlsx"
df = pd.read_excel(source_file,'Sheet1',engine='openpyxl')

for index,row in df.iterrows():
    
    try:
        scheme = Scheme(
        brand=row.get('Brand','N/A'),
        category=row.get('Category', 'N/A'),
        model_name=row.get('Model Name', 'N/A'),
        model_description=row.get('Model Description', 'N/A'),
        sku=row.get('SKU', ''),
        mrp=row.get('MRP', '0.00'),
        mop=row.get('MOP', '0.00'),
        bank_name=row.get('Bank Name', 'N/A'),
        scheme_type=row.get('Scheme Type', 'Brand EMI'),
        emi_type=row.get('EMI Type', 'No Cost EMI'),
        emi_tenure=row.get('EMI Tenure', 'N/A'),
        low_cost_emi_subvention=row.get('Low Cost EMI Subvention', '0.00'),
        cashback_type=row.get('Cashback Type', 'N/A'),
        cashback_amount=row.get('Cashback Amount', '0.00'),
        max_cashback_amount=row.get('Max Cashback Amount', '0.00'),
        promo_start_date=row.get('Promo Start Date', None),
        promo_end_date=row.get('Promo End Date', None),
        scheme_id=row.get('Scheme ID', ''),
        is_emi=bool(row.get('Is EMI', False)),
        is_cashback=bool(row.get('Is Cashback', False)),
        is_upfront=bool(row.get('Is Upfront', False)),
        emi_brand_subvention=row.get('EMI Brand Subvention', '0.00'),
        emi_bank_subvention=row.get('EMI Bank Subvention', '0.00'),
        cashback_brand_subvention=row.get('Cashback Brand Subvention', 0),
        cashback_bank_subvention=row.get('Cashback Bank Subvention', 0),
        additional_terms=row.get('Additional Terms', 'N/A'),
        is_approved=False)
        
        data.append(scheme)

        print('Append Successful')
    except:
        print('Failed')
        continue



    print('Value updated successfully !!')
    

Scheme.objects.bulk_create(data)