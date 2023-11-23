from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.filters import SearchFilter,OrderingFilter


class CustomersAPI(APIView):
    def post(self, request):
        try:
            ser=CustomerSerializer(data=request.data)
            print(request.data)
            if ser.is_valid():
                ser.save(created_by=request.user)
                UserLog.objects.create(user=request.user, transactions_reference=f"Customer {ser.data['name']} has created ")
                return Response(ser.data,status=status.HTTP_201_CREATED)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('error:', e)
            return Response("somthing went wrong",status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,pk=None):
        try:
            if pk is not None:
                company=Customers.objects.get(id=pk)
                ser=CustomerSerializer(company)
                return Response(ser.data,status=status.HTTP_200_OK)
            all_company=Customers.objects.all()
            ser=CustomerSerializer(all_company,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        except Customers.DoesNotExist:
            print('Customers does not exist')
            return Response('Customers does not exist',status=status.HTTP_404_NOT_FOUND)
        
    
    def put(self,request,pk):
        try:
            company=Customers.objects.get(id=pk)
            ser=CustomerSerializer(company,data=request.data,partial=True)
            if ser.is_valid():
                ser.save()
                UserLog.objects.create(user=request.user, transactions_reference=f"Customer {ser.data['name']} has updated")
                return Response(ser.data,status=status.HTTP_200_OK)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        except Customers.DoesNotExist:
            msg='Customers does not exist'
            print(msg)
            return Response(msg,status=status.HTTP_400_BAD_REQUEST)

class CustomersDeleteAPI(APIView):    
       def delete(self, request,pk=None):
        try:
            customer=Customers.objects.get(id=pk)
            UserLog.objects.create(user=request.user, transactions_reference=f"Customer {customer.name} has deleted")
            customer.delete()
            return Response({'customer has deleted'},status=status.HTTP_200_OK)
        except Customers.DoesNotExist:
            print('Customers does not exist')
            return Response('Customers does not exist',status=status.HTTP_404_NOT_FOUND)
        
         
class EmployerAPI(APIView):
    def post(self, request):
        try:
            ser=EmployerSerializer(data=request.data)
            print(request.data)
            if ser.is_valid():
                ser.save(created_by=request.user)
                UserLog.objects.create(user=request.user, transactions_reference=f"Employer {ser.data['name']} has created ")
                return Response(ser.data,status=status.HTTP_201_CREATED)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('error:', e)
            return Response("somthing went wrong",status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,pk=None):
        try:
            if pk is not None:
                company=Employer.objects.get(id=pk)
                ser=EmployerSerializer(company)
                return Response(ser.data,status=status.HTTP_200_OK)
            all_company=Employer.objects.all()
            ser=EmployerSerializer(all_company,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        except Employer.DoesNotExist:
            print('Employer does not exist')
            return Response('Employer does not exist',status=status.HTTP_404_NOT_FOUND)
        
    
    def put(self,request,pk):
        try:
            company=Employer.objects.get(id=pk)
            ser=EmployerSerializer(company,data=request.data,partial=True)
            if ser.is_valid():
                ser.save()
                UserLog.objects.create(user=request.user, transactions_reference=f"Employer {ser.data['name']} has updated")
                return Response(ser.data,status=status.HTTP_200_OK)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        except Employer.DoesNotExist:
            msg='Employer does not exist'
            print(msg)
            return Response(msg,status=status.HTTP_400_BAD_REQUEST)

class EmployerDeleteAPI(APIView):    
       def delete(self, request,pk=None):
        try:
            employer=Employer.objects.get(id=pk)
            UserLog.objects.create(user=request.user, transactions_reference=f"employer {employer.name} has deleted")
            employer.delete()
            return Response({'employer has deleted'},status=status.HTTP_200_OK)
        except Employer.DoesNotExist:
            print('employer does not exist')
            return Response('employer does not exist',status=status.HTTP_404_NOT_FOUND)
        
        
class SourceOfInquiryAPI(APIView):
    def post(self, request):
        try:
            ser=SourceOfInquirySerializer(data=request.data)
            print(request.data)
            if ser.is_valid():
                ser.save(created_by=request.user)
                UserLog.objects.create(user=request.user, transactions_reference=f"SourceOfInquiry {ser.data['name']} has created ")
                return Response(ser.data,status=status.HTTP_201_CREATED)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('error:', e)
            return Response("somthing went wrong",status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,pk=None):
        try:
            if pk is not None:
                company=SourceOfInquiry.objects.get(id=pk)
                ser=SourceOfInquirySerializer(company)
                return Response(ser.data,status=status.HTTP_200_OK)
            all_company=SourceOfInquiry.objects.all()
            ser=SourceOfInquirySerializer(all_company,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        except SourceOfInquiry.DoesNotExist:
            print('SourceOfInquiry does not exist')
            return Response('SourceOfInquiry does not exist',status=status.HTTP_404_NOT_FOUND)
        
    
    def put(self,request,pk):
        try:
            company=SourceOfInquiry.objects.get(id=pk)
            ser=SourceOfInquirySerializer(company,data=request.data,partial=True)
            if ser.is_valid():
                ser.save()
                UserLog.objects.create(user=request.user, transactions_reference=f"SourceOfInquiry {ser.data['name']} has updated")
                return Response(ser.data,status=status.HTTP_200_OK)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        except SourceOfInquiry.DoesNotExist:
            msg='SourceOfInquiry does not exist'
            print(msg)
            return Response(msg,status=status.HTTP_400_BAD_REQUEST)
        
class SourceOfInquiryDeleteAPI(APIView):    
       def delete(self, request,pk=None):
        try:
            soi=SourceOfInquiry.objects.get(id=pk)
            UserLog.objects.create(user=request.user, transactions_reference=f"SourceOfInquiry {soi.name} has deleted")
            soi.delete()
            return Response({'SourceOfInquiry has deleted'},status=status.HTTP_200_OK)
        except SourceOfInquiry.DoesNotExist:
            print('SourceOfInquiry does not exist')
            return Response('SourceOfInquiry does not exist',status=status.HTTP_404_NOT_FOUND)


class TaxAgencyAPI(APIView):
    def post(self, request):
        try:
            ser=TaxAgencySerializer(data=request.data)
            print(request.data)
            if ser.is_valid():
                ser.save(created_by=request.user)
                UserLog.objects.create(user=request.user, transactions_reference=f"Tax Agency {ser.data['name']} has created ")
                return Response(ser.data,status=status.HTTP_201_CREATED)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('error:', e)
            return Response("somthing went wrong",status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,pk=None):
        try:
            if pk is not None:
                tax_agency=TaxAgency.objects.get(id=pk)
                ser=TaxAgencySerializer(tax_agency)
                return Response(ser.data,status=status.HTTP_200_OK)
            all_tax_agency=TaxAgency.objects.all()
            ser=TaxAgencySerializer(all_tax_agency,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        except TaxAgency.DoesNotExist:
            print('TaxAgency does not exist')
            return Response('TaxAgency does not exist',status=status.HTTP_404_NOT_FOUND)
        
    
    def put(self,request,pk):
        try:
            tax_agency=TaxAgency.objects.get(id=pk)
            ser=TaxAgencySerializer(tax_agency,data=request.data,partial=True)
            if ser.is_valid():
                ser.save()
                UserLog.objects.create(user=request.user, transactions_reference=f"Tax Agency {ser.data['name']} has updated")
                return Response(ser.data,status=status.HTTP_200_OK)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        except TaxAgency.DoesNotExist:
            msg='TaxAgency does not exist'
            print(msg)
            return Response(msg,status=status.HTTP_400_BAD_REQUEST)
        

class TaxAgencyDeleteAPI(APIView):    
       def delete(self, request,pk=None):
        try:
            tax_agency=TaxAgency.objects.get(id=pk)
            UserLog.objects.create(user=request.user, transactions_reference=f"tax agency {tax_agency.name} has deleted")
            tax_agency.delete()
            return Response({'tax agency has deleted'},status=status.HTTP_200_OK)
        except TaxAgency.DoesNotExist:
            print('TaxAgency does not exist')
            return Response('TaxAgency does not exist',status=status.HTTP_404_NOT_FOUND)
        


class TaxAPI(APIView):
    def post(self, request):
        try:
            ser=TaxSerializer(data=request.data)
            print(request.data)
            if ser.is_valid():
                ser.save(created_by=request.user)
                UserLog.objects.create(user=request.user, transactions_reference=f"Tax {ser.data['name']} has created ")
                return Response(ser.data,status=status.HTTP_201_CREATED)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('error:', e)
            return Response("somthing went wrong",status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,pk=None):
        try:
            if pk is not None:
                tax_agency=Tax.objects.get(id=pk)
                ser=TaxSerializer1(tax_agency)
                return Response(ser.data,status=status.HTTP_200_OK)
            all_tax_agency=Tax.objects.all()
            ser=TaxSerializer1(all_tax_agency,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        except Tax.DoesNotExist:
            print('Tax does not exist')
            return Response('Tax does not exist',status=status.HTTP_404_NOT_FOUND)
        
    
    def put(self,request,pk):
        try:
            tax_agency=Tax.objects.get(id=pk)
            ser=TaxSerializer(tax_agency,data=request.data,partial=True)
            if ser.is_valid():
                ser.save()
                UserLog.objects.create(user=request.user, transactions_reference=f"Tax {ser.data['name']} has updated")
                return Response(ser.data,status=status.HTTP_200_OK)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        except Tax.DoesNotExist:
            msg='Tax does not exist'
            print(msg)
            return Response(msg,status=status.HTTP_400_BAD_REQUEST)
        

class TaxDeleteAPI(APIView):    
       def delete(self, request,pk=None):
        try:
            tax_agency=Tax.objects.get(id=pk)
            UserLog.objects.create(user=request.user, transactions_reference=f"tax {tax_agency.name} has deleted")
            tax_agency.delete()
            return Response({'tax has deleted'},status=status.HTTP_200_OK)
        except Tax.DoesNotExist:
            print('Tax does not exist')
            return Response('Tax does not exist',status=status.HTTP_404_NOT_FOUND)


class CatalougeAPI(APIView):
    def post(self, request):
        ser=CatalougeSerializer(data=request.data)
        print('data received',request.data)
        try:
            if ser.is_valid():
                catalouge=ser.save(created_by=request.user)
                image=request.FILES.getlist('images')
                datasheet=request.FILES.getlist('datasheet')
                certificate=request.FILES.getlist('certificate')
                print(image,datasheet,certificate)
                for i in range(len(image)):
                    CatelougeFile.objects.create(catalogue=catalouge,files=image[i])
                    print('image',image[i])

                for i in range(len(datasheet)):
                    CatelougeDataSheet.objects.create(catalogue=catalouge,datasheet=datasheet[i])
                    print('datasheet',datasheet[i])
                    
                for i in range(len(certificate)):
                    CatelougeCertificate.objects.create(catalogue=catalouge,files=certificate[i])
                    print('certificate',certificate[i])
                    
                UserLog.objects.create(user=request.user, transactions_reference=f"catalouge {ser.data['name']} has created ")
                return Response('catalouge created', status=status.HTTP_201_CREATED)
        except Exception as e:
            print('error', e)
            return Response('something went wrong', status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request,pk=None):
        try:
            if pk is not None:
                catelouge=Catalouge.objects.get(id=pk)
                catelouge_ser=CatalougeSerializer1(catelouge)
                image=Catalouge.objects.prefetch_related('catelougefile_set').get(id=pk)
                image_ser=CatelougeFileSerializer(image.catelougefile_set.all(),many=True)
                certificate=Catalouge.objects.prefetch_related('catelougecertificate_set').get(id=pk)
                certificate_ser=CatelougeCertificateSerializer(certificate.catelougecertificate_set.all(),many=True)
                datasheet=Catalouge.objects.prefetch_related('catelougedatasheet_set').get(id=pk)
                datasheet_ser=CatelougeDataSheetSerializer(datasheet.catelougedatasheet_set.all(),many=True)
                print(';;;;;;;;;;;;;;;;',image.catelougefile_set.all())
                cont={
                    'catelouge':catelouge_ser.data,
                    'images':image_ser.data,
                    'certificates':certificate_ser.data,
                    'datasheet':datasheet_ser.data,
                }
                return Response(cont,status=status.HTTP_200_OK)
            catelouge=Catalouge.objects.all()
            ser=CatalougeSerializer(catelouge,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        except Exception as e:
            print("Error",e)
            return Response('somthing went wrong',status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk):
        try:
            print('data...',request.data)
            catelogue=Catalouge.objects.get(id=pk)
            ser=CatalougeSerializer(catelogue,data=request.data,partial=True)
            if ser.is_valid():
                catalouge=ser.save()
                image=request.FILES.getlist('images')
                datasheet=request.FILES.getlist('datasheet')
                certificate=request.FILES.getlist('certificate')
                print(image,datasheet,certificate)
                for i in range(len(image)):
                    CatelougeFile.objects.create(catalogue=catalouge,files=image[i])
                    print('image',image[i])

                for i in range(len(datasheet)):
                    CatelougeDataSheet.objects.create(catalogue=catalouge,datasheet=datasheet[i])
                    print('datasheet',datasheet[i])
                    
                for i in range(len(certificate)):
                    CatelougeCertificate.objects.create(catalogue=catalouge,files=certificate[i])
                    print('certificate',certificate[i])
                    
                UserLog.objects.create(user=request.user, transactions_reference=f"catalouge {ser.data['name']} has updated ")
                return Response(ser.data,status=status.HTTP_200_OK)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('errror',e)
            return Response('catelogue not found',status=status.HTTP_400_BAD_REQUEST)
        
        
class CatalougeDeleteAPI(APIView):    
       def delete(self, request,pk):
        try:
            catalouge=Catalouge.objects.get(id=pk)
            UserLog.objects.create(user=request.user, transactions_reference=f"Catalouge {catalouge.name} has deleted")
            catalouge.delete()
            return Response({'Catalouge has deleted'},status=status.HTTP_200_OK)
        except Catalouge.DoesNotExist:
            print('Catalouge does not exist')
            return Response('Catalouge does not exist',status=status.HTTP_404_NOT_FOUND)
        
        
class CatelogueImageDelete(APIView):
    def delete(self,request,pk):
        try:
            files=CatelougeFile.objects.get(id=pk)
            UserLog.objects.create(user=request.user, transactions_reference=f"Catalouge file has deleted from {files.catalogue}")
            files.delete()
            return Response('file has been deleted',status=status.HTTP_200_OK)
        except CatelougeFile.DoesNotExist:
            print('file does not exist')
            return Response('filee does not exist',status=status.HTTP_404_NOT_FOUND)
        
class CatelogueImageAdd(APIView):
    def post(self,request,pk):
        try:
            catalogue=Catalouge.objects.get(id=pk)
            ser=CatelougeFileSerializer(data=request.data)
            if ser.is_valid():
                ser.save(catalogue=catalogue)
            UserLog.objects.create(user=request.user, transactions_reference=f"Catalouge file has add to {catalogue.name}")
            return Response('file has been add',status=status.HTTP_200_OK)
        except Catalouge.DoesNotExist:
            print('file does not exist')
            return Response('filee does not exist',status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request,pk):
        try:
            catalogue=Catalouge.objects.get(id=pk)
            files=CatelougeFile.objects.filter(catalogue=catalogue)
            ser=CatelougeFileSerializer(files,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        except Catalouge.DoesNotExist:
            print('file does not exist')
            return Response('filee does not exist',status=status.HTTP_404_NOT_FOUND)
        
        
class CatelougeCertificateDelete(APIView):
    def delete(self, request,pk):
        try:
            files=CatelougeCertificate.objects.get(id=pk)
            UserLog.objects.create(user=request.user, transactions_reference=f"Catalouge file has deleted from {files.catalogue}")
            files.delete()
            return Response('file has been deleted',status=status.HTTP_200_OK)
        except CatelougeFile.DoesNotExist:
            print('file does not exist')
            return Response('filee does not exist',status=status.HTTP_404_NOT_FOUND)
        
        
class CatelougeCertificateAdd(APIView):
    def post(self,request,pk):
        try:
            catalogue=Catalouge.objects.get(id=pk)
            ser=CatelougeCertificateSerializer(data=request.data)
            if ser.is_valid():
                ser.save(catalogue=catalogue)
            UserLog.objects.create(user=request.user, transactions_reference=f"Catalouge file has add to {catalogue.name}")
            return Response('file has been add',status=status.HTTP_200_OK)
        except Catalouge.DoesNotExist:
            print('file does not exist')
            return Response('filee does not exist',status=status.HTTP_404_NOT_FOUND)
        
        
class CatelougeDataSheetDelete(APIView):
    
    def delete(self, request,pk):
        try:
            files=CatelougeDataSheet.objects.get(id=pk)
            UserLog.objects.create(user=request.user, transactions_reference=f"Catalouge file has deleted from {files.catalogue}")
            files.delete()
            return Response('file has been deleted',status=status.HTTP_200_OK)
        except CatelougeFile.DoesNotExist:
            print('file does not exist')
            return Response('filee does not exist',status=status.HTTP_404_NOT_FOUND)
        
class CatelougeDataSheetAdd(APIView):
    def post(self,request,pk):
        try:
            catalogue=Catalouge.objects.get(id=pk)
            datasheet=request.data
            print(';;;;;;;;;;;;',datasheet)
            print(';;;;;;;;;;;;',request.POST.get('datasheet'))
            ser=CatelougeDataSheetSerializer(data=request.FILES)
            if ser.is_valid():
                ser.save(catalogue=catalogue)
            UserLog.objects.create(user=request.user, transactions_reference=f"Catalouge file has add to {catalogue.name}")
            return Response('file has been add',status=status.HTTP_200_OK)
        except Catalouge.DoesNotExist:
            print('file does not exist')
            return Response('filee does not exist',status=status.HTTP_404_NOT_FOUND)
        
class InquiryAPI(APIView):
    def post(self, request):
        ser=InquiryHeaderSerializer(data=request.data)
        print('data....',request.data)
        try:
            if ser.is_valid():
                inq=ser.save(created_by=request.user)
                boq_number=request.POST.getlist('boq_number')
                boq_description=request.POST.getlist('boq_description')
                unit=request.POST.getlist('unit')
                quantity=request.POST.getlist('quantity')
                rate=request.POST.getlist('rate')
                total_price=request.POST.getlist('total_price')
                print(inq,boq_number,boq_description,quantity,rate,total_price)
                print('length of boq_number',len(boq_number))
                print('length of boq_description',len(boq_description))
                print('length of quantity',len(quantity))
                print('length of rate',len(rate))
                print('length of total_price',len(total_price))
                for i in range(len(boq_number)):
                    print(boq_number[i],boq_description[i],quantity[i],rate[i],total_price[i])
                    InquiryDetail.objects.create(
                        inquiryno=InquiryHeader.objects.get(id=inq.id),
                        boq_number=boq_number[i],
                        boq_description=boq_description[i],
                        unit=unit[i],
                        quantity=quantity[i],
                        rate=rate[i],
                        total_price=total_price[i]

                    )
                
                UserLog.objects.create(user=request.user, transactions_reference=f"inquiry {inq.client_reference_no} has created")
                return Response('inquiry created successfully',status=status.HTTP_201_CREATED)
            return Response(f'data is not valid {ser.errors}',status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('error ',e)
            print("Error..",ser.errors)
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def get(self, request,pk=None):
        if pk is not None:
            inquiry=InquiryHeader.objects.get(id=pk)
            inquiry_ser=InquiryHeaderSerializer1(inquiry)
            detail=InquiryDetail.objects.filter(inquiryno=inquiry)
            # detail_ser=InquiryDetailSerializer1(detail,many=True)
            detail_ser=InquiryDetailSerializer(detail,many=True)
            context={
                'inquiry':inquiry_ser.data,
                'detail':detail_ser.data,
            }
            return Response(context,status=status.HTTP_200_OK)

        inquiry=InquiryHeader.objects.all()
        ser=InquiryHeaderSerializer1(inquiry,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)
    
    
    def put(self, request,pk):
        print('data',request.data)
        print('data............',request.POST)
        boq_number=request.POST.getlist('boq_number')
        boq_description=request.POST.getlist('boq_description')
        unit=request.POST.getlist('unit')
        quantity=request.POST.getlist('quantity')
        rate=request.POST.getlist('rate')
        total_price=request.POST.getlist('total_price')
        print(boq_number,boq_description,quantity,rate,total_price)
        
        try:
            old_data=InquiryHeader.objects.get(id=pk) 
            ser=InquiryHeaderSerializer(old_data,data=request.data,partial=True)
            if ser.is_valid():
                print(boq_number,boq_description,quantity,rate,total_price)
                inq=ser.save()
                # detail=InquiryDetail.objects.filter(inquiryno=inq.id).delete()
                for i in range(len(boq_number)):
                    InquiryDetail.objects.create(
                        inquiryno=InquiryHeader.objects.get(id=inq.id),
                        boq_number=boq_number[i],
                        boq_description=boq_description[i],
                        unit=unit[i],
                        quantity=quantity[i],
                        rate=rate[i],
                        total_price=total_price[i]

                    )
                
                UserLog.objects.create(user=request.user, transactions_reference=f"inquiry {inq.client_reference_no} has updated")
                return Response('inquiry created successfully',status=status.HTTP_201_CREATED)
            return Response(f'data is not valid {ser.errors}',status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('error creating',e)
            print("Error..",ser.errors)
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class InquiryAPIDelete(APIView):
    def delete(self, request,pk):
        try:
            inq=InquiryHeader.objects.get(id=pk)
            UserLog.objects.create(user=request.user, transactions_reference=f"inquiry  {inq.client_reference_no} is deleted")
            inq.delete()
            return Response('inquiry has been deleted',status=status.HTTP_200_OK)
        except InquiryHeader.DoesNotExist:
            print('inquiry does not exist')
            return Response('inquiry does not exist',status=status.HTTP_404_NOT_FOUND)
        
class InquiryDetailsUpdateAPI(APIView):
    def put(self, request,pk):
        print('data....',request.data)
        inq_detail=InquiryDetail.objects.get(id=pk)
        ser=InquiryDetailSerializer(inq_detail,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            UserLog.objects.create(user=request.user, transactions_reference=f"inquiry detail of {inq_detail.inquiryno} is updated")
            return Response(ser.data,status=status.HTTP_200_OK)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class InquiryDetailsAddAPI(APIView):
    def post(self, request):
        print('data....',request.data)
        ser=InquiryDetailSerializer(data=request.data)
        if ser.is_valid():
            inq=ser.save()
            UserLog.objects.create(user=request.user, transactions_reference=f"inquiry detail of {inq.inquiryno} is added")
            return Response(ser.data,status=status.HTTP_200_OK)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    
class InquiryDetailsDeleteAPI(APIView):
    def delete(self,request,pk):
        try:
            inq_detail=InquiryDetail.objects.get(id=pk)
            UserLog.objects.create(user=request.user, transactions_reference=f"inquiry detail of  {inq_detail.inquiryno} is deleted")
            inq_detail.delete()
            return Response('inquiry has been deleted',status=status.HTTP_200_OK)
        except InquiryDetail.DoesNotExist:
            print('inquiry does not exist')
            return Response('inquiry does not exist',status=status.HTTP_404_NOT_FOUND)
               
                
class EstimatioResourceDetailAPI(APIView):
    def post(self, request):
        print('data received',request.data)
        header_ser=EstimatioResourceHeaderSerializer(data=request.data)
        if header_ser.is_valid():
            header=header_ser.save()
            item=request.POST.getlist('item')
            quantity=request.POST.getlist('quantity')
            # gross_total=request.POST.getlist('gross_total')
            # vat_amount=request.POST.getlist('vat_amount')
            estimation_rate=request.POST.getlist('estimation_rate')
            print(
                'item',item,
                'quantity',quantity,
                # 'gross_total',gross_total,
                # 'vat_amount',vat_amount,
                'estimation_rate',estimation_rate
            )
            
            for i in range(len(item)):
                EstimatioResourceDetail.objects.create(
                    estimation_res_header=EstimatioResourceHeader.objects.get(id=header.id),
                    item=Catalouge.objects.get(id=item[i]),
                    quantity=quantity[i],
                    # gross_total=gross_total[i],
                    # vat_amount=vat_amount[i],
                    estimation_rate=estimation_rate[i]
                )
            
            
            return Response('ok', status=status.HTTP_201_CREATED)
        print(header_ser.errors)
        return Response(header_ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request,pk=None):
        try:
            if pk is not None:
                esti_detail=EstimatioResourceDetail.objects.get(id=pk)
                ser=EstimatioResourceDetailSerializer(esti_detail)
                return Response(ser.data,status=status.HTTP_200_OK)
            esti_res_header=EstimatioResourceDetail.objects.all()
            ser=EstimatioResourceDetailSerializer(esti_res_header,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        except EstimatioResourceDetail.DoesNotExist:
            return Response('some error occurred',status=status.HTTP_404_NOT_FOUND)
        
        
        
class EstimationAPI(APIView):
    def post(self,request):
        print('data.....//////',request.data,'........//////')
        esti_header=EstimatioHeaderSerializer(data=request.data)
        if esti_header.is_valid():
            header=esti_header.save(created_by=request.user)
            print('header part is saved successfully')
            inquirydetail=request.data.getlist('inquirydetail')
            # estimation_number=request.data.getlist('estimation_number')
            vat_tax=request.data.getlist('vat_tax')
            estimation_rate=request.data.getlist('estimation_rate')
            salesprice=request.data.getlist('salesprice')
            markup=request.data.getlist('markup')
            markup_value=request.data.getlist('markup_value')
            gross_price=request.data.getlist('gross_price')
            taxable=request.data.getlist('taxable')
            # NetTotal=request.data.getlist('NetTotal')
            print('....//////////////')
            print(
                'inquirydetail',inquirydetail,
                # 'estimation_number',estimation_number,
                'vat_tax',vat_tax,
                'estimation_rate',estimation_rate,
                'salesprice',salesprice,
                'markup',markup,
                'markup_value',markup_value,
                'gross_price',gross_price,
                'taxable',taxable,
                # 'NetTotal',NetTotal
                
            )
            print('......./////////////////')
            for i in range(len(inquirydetail)):
                EstimatioDetail.objects.create(
                    inquirydetail=InquiryDetail.objects.get(id=inquirydetail[i]),
                    estimation_number=EstimatioHeader.objects.get(id=header.id),
                    vat_tax=Tax.objects.get(id=vat_tax[i]),
                    estimation_rate=estimation_rate[i],
                    salesprice=salesprice[i],
                    markup=markup[i],
                    markup_value=markup_value[i],
                    gross_price=gross_price[i],
                    taxable=taxable[i],
                    # NetTotal=NetTotal[i]
                )
            UserLog.objects.create(user=request.user, transactions_reference=f"Estimation is created")
            return Response({'message':'ok'},status=status.HTTP_200_OK)

        return Response(esti_header.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self,request,pk=None):
        try:
            if pk is not None:
                estimation=EstimatioHeader.objects.get(id=pk)
                ser=EstimatioHeaderSerializer1(estimation)
                estimation_details=EstimatioHeader.objects.prefetch_related('estimatiodetail_set').get(id=pk)
                estimation_details_ser=EstimatioDetailSerializer1(estimation_details.estimatiodetail_set.all(),many=True)
                context={   
                    'estimation_header':ser.data,
                    'estimation_details':estimation_details_ser.data,
                    
                }
                return Response(context,status=status.HTTP_200_OK)

            estimations=EstimatioHeader.objects.all()
            ser=EstimatioHeaderSerializer1(estimations,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        except Exception as e:
            print("Error",e)

    def put(self,request,pk):
        estimation=EstimatioHeader.objects.get(id=pk)
        ser=EstimatioHeaderSerializer(estimation,data=request.data)
        if ser.is_valid():
            ser.save()
            UserLog.objects.create(user=request.user, transactions_reference=f"Estimation {estimation.inquiry_no} is updated")
            return Response({'msg':'data updated successfully'},status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class EstimationDelete(APIView):
    def delete(self, request,pk):
        try:
            header=EstimatioHeader.objects.get(id=pk)
            UserLog.objects.create(user=request.user, transactions_reference=f"Estimation  is deleted")
            header.delete()
            return Response({'msg':'data deleted successfully'},status=status.HTTP_200_OK)
        except EstimatioHeader.DoesNotExist:
            return Response('estimation does not exist', status=status.HTTP_400_BAD_REQUEST)
        
        
        
class CatelogueSearchAPI(ListAPIView):
    queryset=Catalouge.objects.all()
    serializer_class=CatalougeSerializer
    # filter_backends=[SearchFilter,OrderingFilter]
    filter_backends=[SearchFilter]
    search_fields=['^name','^type','^category','^sub_category','^type_sub_category','^origin','^brand','^series','^model','^size','^specification','^list_price','^currency','^discount','^unit_of_measurement','^base_of_pricing']
    # odering_fields =['name']
           
        
class UserLogAPI(APIView):
    def get(self,request):
        userlog=UserLog.objects.all()
        ser=UserLogSerializer(userlog,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)
    
    
class EstimatioResourceDetailAPI(APIView):
    def get(self,request,pk):
        try:
            inq_detail=InquiryDetail.objects.get(id=pk)
            res_header=EstimatioResourceHeader.objects.filter(inquiry_detail=inq_detail.id).first()
            res_detail=EstimatioResourceDetail.objects.filter(estimation_res_header=res_header.id)
            res_detail_ser=EstimatioResourceDetailSerializer(res_detail,many=True)
            return Response(res_detail_ser.data,status=status.HTTP_200_OK)
        except InquiryDetail.DoesNotExist:
            return Response('inquiry id does not exit',status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk):
        try:
            inq_detail=InquiryDetail.objects.get(id=pk)
            res_header=EstimatioResourceHeader.objects.filter(inquiry_detail=inq_detail.id).first()
            res_header_ser=EstimatioResourceHeaderSerializer(res_header,data=request.data,partial=True)
            if res_header_ser.is_valid():
                header=res_header_ser.save()
                # estimation_res_header=request.data.getlist('estimation_res_header')
                item=request.data.getlist('item')
                quantity=request.data.getlist('quantity')
                estimation_rate=request.data.getlist('estimation_rate')

                res_detail=EstimatioResourceDetail.objects.filter(estimation_res_header=header.id).delete()
                for i in range(len(item)):
                    EstimatioResourceDetail.objects.create(
                        estimation_res_header=EstimatioResourceHeader.objects.get(id=header.id),
                        item=item[i],
                        quantity=quantity[i],
                        estimation_rate=estimation_rate[i]
                    )
                return Response(res_header_ser.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response('something went wrong',status=status.HTTP_400_BAD_REQUEST)
            



