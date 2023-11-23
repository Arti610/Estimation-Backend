from django.db import models
import datetime
from accounts.models import CustomUser,Departments
from django.utils import timezone


class UserLog(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,blank=True)
    timestamp=models.DateTimeField(default=datetime.datetime.now)
    transactions_reference=models.CharField(max_length=120,null=True)

    def __str__(self) -> str:
        return self.transactions_string()
    
    def transactions_string(self):
        return f'{self.transactions_reference} by {self.user.first_name if self.user.first_name else self.user}'
    
    

class Customers(models.Model):
    ACC_STATUS=(
        ('Active', 'Active'),
        ('Closed', 'Closed'),
        ('Suspended','Suspended'),
    )
    name=models.CharField(max_length=50,null=True,blank=True)
    address=models.CharField(max_length=225,null=True,blank=True)
    email=models.EmailField()
    contact_person=models.CharField(max_length=225,null=True,blank=True)
    country=models.CharField(max_length=225,null=True,blank=True)
    mobile_number=models.CharField(max_length=15,null=True,blank=True)
    account_status=models.CharField(max_length=30, choices=ACC_STATUS, null=True,blank=True,default='Active')
    kyc_status=models.BooleanField(default=False)
    trn_number=models.CharField(max_length=100,null=True,blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True,related_name='CustomerCreate')
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Updated Date")

    def __str__(self):
        return str(self.name)
    
class Employer(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    address=models.TextField(blank=True)
    email=models.EmailField()
    country=models.CharField(max_length=55,null=True,blank=True)
    # contact_number=models.CharField(max_length=15,null=True,blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True,related_name='employercreate')
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Updated Date")

    def __str__(self):
        return str(self.name)
    
    
class SourceOfInquiry(models.Model):
    name=models.CharField(max_length=225,null=True,blank=True)
    description=models.TextField(blank=True,null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True,related_name='sourceinquiry')
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Updated Date")

    def __str__(self):
        return str(self.name)


class TaxAgency(models.Model):
    name = models.CharField(max_length=60)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True,related_name='CreatedBy')
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Updated Date")

    def __str__(self):
        return self.name


class Tax(models.Model):
    name = models.CharField(max_length=20)
    rate = models.DecimalField(decimal_places=2,max_digits=10)
    agency = models.ForeignKey(TaxAgency, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True,related_name='CreatedTax')
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Updated Date")

    def __str__(self):
        return f"{self.name}"
    
    
class Catalouge(models.Model):
    name=models.CharField(max_length=225,null=True, blank=True)
    type=models.CharField(max_length=225,null=True, blank=True)
    category=models.CharField(max_length=225,null=True, blank=True)
    sub_category=models.CharField(max_length=225,null=True, blank=True)
    type_sub_category=models.CharField(max_length=225,null=True, blank=True)
    origin=models.CharField(max_length=225,null=True, blank=True)
    finish=models.CharField(max_length=225,null=True, blank=True)
    brand=models.CharField(max_length=225,null=True, blank=True)
    series=models.CharField(max_length=225,null=True, blank=True)
    model=models.CharField(max_length=225,null=True, blank=True)
    size=models.CharField(max_length=225,null=True, blank=True)
    specification=models.TextField(null=True,blank=True)
    tax=models.ForeignKey(Tax,on_delete=models.SET_NULL,null=True,blank=True,related_name='inquiry_tax')
    list_price=models.CharField(max_length=100,null=True,blank=True)
    currency=models.CharField(max_length=100,null=True,blank=True)
    discount=models.CharField(max_length=100,null=True,blank=True)
    unit_of_measurement=models.CharField(max_length=100,null=True,blank=True)
    base_of_pricing=models.CharField(max_length=100,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    # datasheet=models.FileField(upload_to='catalogueImage',null=True,blank=True)
    primary_image=models.FileField(upload_to='catalogueImage',null=True,blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True,related_name='CreatedCatelouge')
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Updated Date")
    

    def __str__(self):
        return str(self.name)

class CatelougeFile(models.Model):
    catalogue=models.ForeignKey(Catalouge,on_delete=models.CASCADE,null=True,blank=True)
    files=models.FileField(upload_to='Catalougefiles',null=True,blank=True)

    def __str__(self):
        return str(self.catalogue)
    
class CatelougeCertificate(models.Model):
    catalogue=models.ForeignKey(Catalouge,on_delete=models.CASCADE,null=True,blank=True)
    files=models.FileField(upload_to='Catalouge_certificate',null=True,blank=True)

    def __str__(self):
        return str(self.catalogue)
    
class CatelougeDataSheet(models.Model):
    catalogue=models.ForeignKey(Catalouge,on_delete=models.CASCADE,null=True,blank=True)
    datasheet=models.FileField(upload_to='catalogueSheet',null=True,blank=True)

    def __str__(self):
        return str(self.catalogue)
    
    
class InquiryHeader(models.Model):
    inquirydate=models.DateField(null=True, blank=True)
    client_reference_no=models.CharField(max_length=50,null=True,blank=True)
    submission_date=models.DateField()
    customer=models.ForeignKey(Customers,on_delete=models.SET_NULL, null=True,blank=True)
    employer=models.ForeignKey(Employer,on_delete=models.SET_NULL, null=True,blank=True)
    source_of_inquiry=models.ForeignKey(SourceOfInquiry,on_delete=models.SET_NULL, null=True,blank=True)
    department=models.ForeignKey(Departments,on_delete=models.SET_NULL, null=True,blank=True)
    estimator=models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,blank=True,related_name='estimator')
    salesman=models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,blank=True,related_name='salesman')
    scope_of_work=models.CharField(max_length=100,null=True,blank=True)
    attachments=models.FileField(upload_to='inquiryheader',null=True,blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True,related_name='inqheader')
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Updated Date")

    def __str__(self):
        return str(f'{self.customer.name} {self.inquirydate}')
    
    
    
class InquiryDetail(models.Model):
    inquiryno=models.ForeignKey(InquiryHeader,on_delete=models.CASCADE,null=True,blank=True)
    boq_number=models.CharField(max_length=100,null=True,blank=True)
    boq_description=models.TextField(null=True,blank=True)
    unit=models.CharField(max_length=50,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    rate=models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)
    total_price=models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)

    def __str__(self):
        return str(f'{self.inquiryno.customer.name} {self.inquiryno.inquirydate}')
    
    

class EstimatioHeader(models.Model):
    inquiry_no=models.ForeignKey(InquiryHeader,on_delete=models.SET_NULL,null=True,blank=True)
    estimation_date=models.DateField(null=True,blank=True)
    net_total=models.DecimalField(decimal_places=2,max_digits=15,null=True,blank=True)
    is_paid=models.BooleanField(default=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True,related_name='estimationheader')
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Updated Date")

    def __str__(self):
        return str(self.inquiry_no)

    
class EstimatioDetail(models.Model):
    inquirydetail=models.ForeignKey(InquiryDetail,on_delete=models.SET_NULL,null=True,blank=True)
    estimation_number=models.ForeignKey(EstimatioHeader,on_delete=models.SET_NULL,null=True,blank=True)
    vat_tax=models.ForeignKey(Tax,on_delete=models.SET_NULL,blank=True,null=True)
    estimation_rate=models.DecimalField(decimal_places=2,max_digits=15,null=True,blank=True)
    salesprice=models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)
    markup=models.CharField(max_length=10,null=True,blank=True)
    markup_value=models.CharField(max_length=50,null=True,blank=True)
    gross_price=models.CharField(max_length=15,null=True,blank=True)
    taxable=models.CharField(max_length=25,null=True,blank=True)
    NetTotal=models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)

    def __str__(self):
        return str(self.inquirydetail)

class EstimatioResourceHeader(models.Model):
    inquiry_detail=models.ForeignKey(InquiryDetail,on_delete=models.CASCADE,null=True,blank=True)
    total_price=models.DecimalField(decimal_places=2,max_digits=15,null=True,blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True,related_name='estresource')
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Updated Date")
    
    def __str__(self):
        return str(self.inquiry_detail)
    
    
class EstimatioResourceDetail(models.Model):
    estimation_res_header=models.ForeignKey(EstimatioResourceHeader,on_delete=models.CASCADE,null=True,blank=True)
    item = models.ForeignKey(Catalouge,on_delete=models.CASCADE,null=True, blank=True)
    # unit= models.CharField(max_length=225,null=True, blank=True)
    quantity=models.IntegerField(null=True, blank=True)
    # rate=models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)
    # discount=models.IntegerField(null=True, blank=True)
    gross_total=models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)
    # vat_type=models.ForeignKey(Tax, on_delete=models.SET_NULL,null=True,blank=True)
    vat_percentage=models.IntegerField(null=True, blank=True)
    vat_amount=models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)
    estimation_rate=models.DecimalField(decimal_places=2,max_digits=15,null=True,blank=True)   
    

    def __str__(self):
        return str(self.item.category)


