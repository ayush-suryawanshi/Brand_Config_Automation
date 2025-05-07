from django.db import models
import uuid
#................................................

BRAND_CHOICES = [
    ('Oppo', 'Oppo'),
    ('Vivo', 'Vivo'),
    ('Xiaomi', 'Xiaomi'),
    ('Realme', 'Realme'),
    ('Samsung', 'Samsung'),
    ]

BANK_CHOICES = [
    ('HDFC CC', 'HDFC CC'), ('HDFC DC', 'HDFC DC'),
    ('ICICI CC', 'ICICI CC'), ('ICICI DC', 'ICICI DC'),
    ('AXIS CC', 'AXIS CC'), ('AXIS DC', 'AXIS DC'),
    ('UNIPAY CC', 'UNIPAY CC'), ('UNIPAY DC', 'UNIPAY DC'),
    ('CITIBANK CC', 'CITIBANK CC'), ('CITIBANK DC', 'CITIBANK DC'),
    ('STANDARD CHARTERED CC', 'STANDARD CHARTERED CC'), ('STANDARD CHARTERED DC', 'STANDARD CHARTERED DC'),
    ('HSBC CC', 'HSBC CC'), ('HSBC DC', 'HSBC DC'),
    ('KOTAK CC', 'KOTAK CC'), ('KOTAK DC', 'KOTAK DC'),
    ('SBI CC', 'SBI CC'), ('SBI DC', 'SBI DC'),
    ('AMEX CC', 'AMEX CC'),
    ('INDUSIND CC', 'INDUSIND CC'), ('INDUSIND DC', 'INDUSIND DC'),
    ('BAJAJ CC', 'BAJAJ CC'), ('BAJAJ DC', 'BAJAJ DC'),
    ('RBL CC', 'RBL CC'), ('RBL DC', 'RBL DC'),
    ('YES CC', 'YES CC'), ('YES DC', 'YES DC'),
    ('Bank of Baroda CC', 'Bank of Baroda CC'), ('Bank of Baroda DC', 'Bank of Baroda DC'),
    ('FEDERAL CC', 'FEDERAL CC'), ('FEDERAL DC', 'FEDERAL DC'),
    ('J&K CC', 'J&K CC'), ('J&K DC', 'J&K DC'),
    ('AU CC', 'AU CC'), ('AU DC', 'AU DC'),
    ('ONECARD CC', 'ONECARD CC'),
    ('IDFC FIRST CC', 'IDFC FIRST CC'), ('IDFC FIRST DC', 'IDFC FIRST DC'),
]


class Manager(models.Model):
    id = models.CharField(default=uuid.uuid4,primary_key=True,editable=False,max_length=20,unique=True)
    name = models.CharField(editable=True,max_length=50,blank=False,null=False)
    email = models.EmailField(editable=True,max_length=100,blank=False,null=False)
    password = models.CharField(max_length=50,editable=True,blank=False,null=False)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'The User ID is : {self.id}')

class Input_Row(models.Model):

    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,blank=False)
    processed_at = models.DateField(auto_now_add=True)
    brand = models.CharField(max_length=50,editable=False,choices=BRAND_CHOICES)
    jsonified_row_data = models.CharField(max_length=2000,editable=True,blank=False)
    email_attachment = models.ForeignKey('EmailAttachment', related_name='input_rows', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return (f"Row data is as follows : {self.jsonified_row_data}")


class Scheme(models.Model):

    input_row = models.ForeignKey(Input_Row, on_delete=models.CASCADE, related_name='schemes',null=True,blank=True,editable=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    brand = models.CharField(max_length=50, editable=True)
    category = models.CharField(default='N/A', max_length=100, null=True, blank=True)
    model_name = models.CharField(default='N/A', max_length=100, null=True, blank=True)
    model_description = models.CharField(default='N/A', max_length=500, null=True, blank=True)  # Changed to CharField
    sku = models.CharField(max_length=100, unique=False, null=False)
    mrp = models.CharField(default='N/A', max_length=100, null=True, blank=True)  # Changed to CharField
    mop = models.CharField(default='N/A', max_length=100, null=True, blank=True)  # Changed to CharField
    bank_name = models.CharField(max_length=100, null=True, blank=True, choices=BANK_CHOICES)
    scheme_type = models.CharField(max_length=50, default='Brand EMI')
    emi_type = models.CharField(default='No Cost EMI', max_length=50, null=True, blank=True)
    emi_tenure = models.CharField(default='N/A', max_length=50, null=True, blank=True)
    low_cost_emi_subvention = models.CharField(default='N/A', max_length=100, null=True, blank=True)  # Changed to CharField
    cashback_type = models.CharField(default='N/A', max_length=100, null=True, blank=True)
    cashback_amount = models.CharField(default='N/A', max_length=100, null=True, blank=True)  # Changed to CharField
    max_cashback_amount = models.CharField(default='N/A', max_length=100, null=True, blank=True)  # Changed to CharField
    promo_start_date = models.CharField(default='N/A', max_length=100, null=True, blank=True)  # Changed to CharField
    promo_end_date = models.CharField(default='N/A', max_length=100, null=True, blank=True)  # Changed to CharField
    scheme_id = models.CharField(default='N/A', max_length=100, null=True, blank=True)
    is_emi = models.BooleanField(default=False)
    is_cashback = models.BooleanField(default=False)
    is_upfront = models.BooleanField(default=False, null=True, blank=True)
    emi_brand_subvention = models.CharField(max_length=100, null=True, blank=True)  # Changed to CharField
    emi_bank_subvention = models.CharField(max_length=100, null=True, blank=True)  # Changed to CharField
    cashback_brand_subvention = models.CharField(max_length=100, default='0', null=True, blank=True)  # Changed to CharField
    cashback_bank_subvention = models.CharField(max_length=100, default='0', null=True, blank=True)  # Changed to CharField
    additional_terms = models.CharField(default='N/A', max_length=500, null=True, blank=True)  # Changed to CharField
    is_approved = models.BooleanField(default=False, editable=True)
    jsonified_data = models.CharField(max_length=1000, editable=True, null=True, blank=True)

    def __str__(self):
        return f"{self.brand} - {self.model_name} ({self.scheme_id})"

class Email_Failure_Tracker(models.Model):
    tracker_id = models.UUIDField(default=uuid.uuid4)
    email_failure = models.IntegerField(default=0,editable=True)
    row_failure = models.IntegerField(default=0,editable=True)


class Email(models.Model):
    id = models.UUIDField(primary_key=True ,default = uuid.uuid4 ,editable=False , blank=True , null=False)
    subject = models.CharField(max_length=900,editable=True)
    sender = models.CharField(max_length=200,editable=True,default='N/A')
    created_at = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(default='N/A',editable=True,max_length=50)
    processed = models.BooleanField(default=False,editable=True,blank=True,null=False)
    rejected = models.BooleanField(default=False,editable=True,blank=True,null=False)

    def __str__(self):
        return f"{self.subject} from {self.sender}"


class EmailAttachment(models.Model):
    email = models.ForeignKey(Email, related_name='attachments', on_delete=models.CASCADE)
    name = models.CharField(default='N/A',editable=True)
    attachment = models.FileField(upload_to='email_attachments/',editable=True)
    #attachment_name = models.CharField(default='N/A',max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False,editable=True,blank=True)

    def __str__(self):
        return f"Attachment: ({self.email.subject})"


    
