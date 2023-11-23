from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customers
        fields='__all__'

        
class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employer
        fields='__all__'
 
        
class SourceOfInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model=SourceOfInquiry
        fields='__all__'

        
class TaxAgencySerializer(serializers.ModelSerializer):
    class Meta:
        model=TaxAgency
        fields='__all__'
        
        
class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tax
        fields='__all__'
        
        
class TaxSerializer1(serializers.ModelSerializer):
    class Meta:
        model=Tax
        fields='__all__'
        depth=1
        
class CatalougeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Catalouge
        fields='__all__'
        
        
class CatalougeSerializer1(serializers.ModelSerializer):
    class Meta:
        model=Catalouge
        fields='__all__'
        depth=1
        
class CatelougeFileSerializer(serializers.ModelSerializer):
    class Meta:
        model=CatelougeFile
        fields='__all__'
        
class CatelougeCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model=CatelougeCertificate
        fields='__all__'
        
class CatelougeDataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model=CatelougeDataSheet
        fields='__all__'
        
class InquiryHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model=InquiryHeader
        fields='__all__'
        
class InquiryHeaderSerializer1(serializers.ModelSerializer):
    class Meta:
        model=InquiryHeader
        fields='__all__'
        depth=1
        
        
class InquiryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=InquiryDetail
        fields='__all__'
        
class InquiryDetailSerializer1(serializers.ModelSerializer):
    class Meta:
        model=InquiryDetail
        fields='__all__'
        depth=1
        
        
class EstimatioHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model=EstimatioHeader
        fields='__all__'
        
class EstimatioHeaderSerializer1(serializers.ModelSerializer):
    class Meta:
        model=EstimatioHeader
        fields='__all__'
        depth=2
        
class EstimatioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=EstimatioDetail
        fields='__all__'
        
        
class EstimatioDetailSerializer1(serializers.ModelSerializer):
    class Meta:
        model=EstimatioDetail
        fields='__all__'
        depth=2
        
class EstimatioResourceHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model=EstimatioResourceHeader
        fields='__all__'
        
        
class EstimatioResourceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=EstimatioResourceDetail
        fields='__all__'
        
        
class UserLogSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserLog
        fields='__all__'
        depth=1
        
        