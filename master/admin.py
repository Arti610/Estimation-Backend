from django.contrib import admin
from .models import *

admin.site.register(UserLog)
admin.site.register(Customers)
admin.site.register(SourceOfInquiry)
admin.site.register(Tax)
admin.site.register(TaxAgency)
admin.site.register(Catalouge)
admin.site.register(CatelougeCertificate)
admin.site.register(CatelougeDataSheet)
admin.site.register(CatelougeFile)
admin.site.register(Employer)
admin.site.register(InquiryHeader)
admin.site.register(InquiryDetail)
admin.site.register(EstimatioDetail)
admin.site.register(EstimatioHeader)
admin.site.register(EstimatioResourceDetail)
admin.site.register(EstimatioResourceHeader)
