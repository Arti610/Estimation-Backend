from django.urls import path
from .views import *

urlpatterns = [
    # customers
    path('api/customers',CustomersAPI.as_view()),
    path('api/customers/<int:pk>',CustomersAPI.as_view()),
    path('api/delete_customers/<int:pk>',CustomersDeleteAPI.as_view()),
    
    # Employer
    path('api/employer',EmployerAPI.as_view()),
    path('api/employer/<int:pk>',EmployerAPI.as_view()),
    path('api/delete_employer/<int:pk>',EmployerDeleteAPI.as_view()),
    
    # sourceofinquiry
    path('api/sourceofinquiry',SourceOfInquiryAPI.as_view()),
    path('api/sourceofinquiry/<int:pk>',SourceOfInquiryAPI.as_view()),
    path('api/delete_soi/<int:pk>',SourceOfInquiryDeleteAPI.as_view()),
    
    # tax agency
    path('api/tax_agency',TaxAgencyAPI.as_view()),
    path('api/tax_agency/<int:pk>',TaxAgencyAPI.as_view()),
    path('api/delete_taxagency/<int:pk>',TaxAgencyDeleteAPI.as_view()),
    
    #TAX 
    path('api/tax',TaxAPI.as_view()),
    path('api/tax/<int:pk>',TaxAPI.as_view()),
    path('api/delete_tax/<int:pk>',TaxDeleteAPI.as_view()),
    
    #catelouge
    path('api/catalogue',CatalougeAPI.as_view()),
    path('api/catalogue/<int:pk>',CatalougeAPI.as_view()),
    path('api/delete_catalogue/<int:pk>',CatalougeDeleteAPI.as_view()),
    path('api/search_catalogue',CatelogueSearchAPI.as_view()),
    
    # catelogue images
    path('api/delete_catelogue_image/<int:pk>',CatelogueImageDelete.as_view()),
    path('api/add_catelogue_image/<int:pk>',CatelogueImageAdd.as_view()),
    path('api/get_catelogue_image/<int:pk>',CatelogueImageAdd.as_view()),
    # catelogue certificates
    path('api/add_catelogue_certificate/<int:pk>',CatelougeCertificateAdd.as_view()),
    path('api/delete_catelogue_certificate/<int:pk>',CatelougeCertificateDelete.as_view()),
    # catelogue datasheet
    path('api/add_catelogue_datasheet/<int:pk>',CatelougeDataSheetAdd.as_view()),
    path('api/delete_catelogue_datasheet/<int:pk>',CatelougeDataSheetDelete.as_view()),

    #inquiry
    path('api/inquiry',InquiryAPI.as_view()),
    path('api/inquiry/<int:pk>',InquiryAPI.as_view()),
    path('api/delete_inquiry/<int:pk>',InquiryAPIDelete.as_view()),
    
    #inquiry details
    path('api/inquiry_details_update/<int:pk>',InquiryDetailsUpdateAPI.as_view()),
    path('api/inquiry_details_delete/<int:pk>',InquiryDetailsDeleteAPI.as_view()),
    path('api/inquiry_details_add',InquiryDetailsAddAPI.as_view()),
    
    #Estimations resource 
    path('api/estimation_resource_details',EstimatioResourceDetailAPI.as_view()),
    
    # Estimation
    
    path('api/estimation',EstimationAPI.as_view()),
    path('api/estimation/<int:pk>',EstimationAPI.as_view()),
    path('api/delete_estimation/<int:pk>',EstimationDelete.as_view()),
    
    #log
    path('api/userlog',UserLogAPI.as_view()),
    
    #estimation resource detail
    path('api/estimation_res_detail/<int:pk>',EstimatioResourceDetailAPI.as_view()),
    
    
    
    
]