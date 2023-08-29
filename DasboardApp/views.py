from cgi import print_arguments
from cgitb import html
import email
from locale import currency
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import requests
from django.contrib.auth.models import User
import requests

from django.http import HttpResponseBadRequest, JsonResponse
from django.template.loader import render_to_string

import json
from logging import root
# from services import setToken, logout

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Stock, Class1, Category, Subcategory, Manufacturer, Model, Config, ConfigName
from django.core import serializers

from csv import DictReader
import csv
from .forms import CSVUploadForm
from .resources import StockResource
from tablib import Dataset
import codecs
import pandas as pd

from django.core.paginator import Paginator
# from bootstrap_pagination.templatetags.bootstrap_pagination import bootstrap_pagination

import random
import string

# Stock.objects.all().delete()
# print("Net Adapt Reserved stocks", Stock.objects.filter(Class = "Net Adapter-Lab", Category = "Net Adapter-Lab - vfg", Manufacturer = "Mellanox Technologies", Model = "ConnectX-6 VPI Adapter Card - MCX653106A-ECAT-SP", Substatus__icontains = "Reserved", Reservedby = "admin", Configname = "18").count())

# for i in Stock.objects.filter(Class = "Net Adapter-Lab", Category = "Net Adapter-Lab - vfg", Manufacturer = "Mellanox Technologies", Model = "ConnectX-6 VPI Adapter Card - MCX653106A-ECAT-SP", Substatus__icontains = "Reserved"):
#     print("i class:", i.Class)
#     print("i Reserved by", i.Reservedby)
#     print("i Config name", i.Configname)
# Reservedby = "admin", Configname = "Netadapter"

# marks = [82,31,31,78,90,31,120]
# print("Min Index:", marks.index(min(marks)))
# with open('Inventory.csv', mode="r", encoding='latin1') as csv_file:
#     # csv_reader = csv.DictReader(csv_file)
#     for row in csv.DictReader(csv_file):
#         if Stock.objects.filter(SSN=row['Serial number'], name=row['Name'], Name=row['Name']).exists():
#             # print("count", Stock.objects.filter(SSN=row['Serial number'], name=row['Name'], Name=row['Name']).count())
#             pass
#         else:
#             stock=Stock(name=row['Name'], Name=row['Name'], SSN=row['Serial number'], Class=row['Class'],
#                         DNUSAN=row['DNUSAN'], Shortdesc=row['Short description'],Category=row['Category'],Subcategory=row['Subcategory'],Manufacturer=row['Manufacturer'],
#                         Model=row['Model'],Status=row['Status(hardware_status)'],Substatus=row['Substatus'],Program=row['Program'],Project=row['Project'],
#                         PONo=row['PO number'],POlineNo=row['PO line number'],Assignto=row['Assigned to'],Ownedby=row['Owned by'],Managedby=row['Managed by'],
#                         HomeLoc=row['Home Location'],Location=row['Location'],LocDetails=row['Location Details'],Created=row['Created'],Createdby=row['Created by'],
#                         Updated=row['Updated'],Updatedby=row['Updgted by'],Costcent=row['Cost center'],Comments=row['Comments'],
#                         FinaType=row['Finance Type'],HardSuppG=row['Hardware Support Group'],HardSuppSer=row['Hardware Support Service'],LotNo=row['Lot Number'],
#                         Etag=row['Etag'])
#             stock.save()

# with open('Inventory.csv', mode="r", encoding='latin1') as csv_file:
#     # csv_reader = csv.DictReader(csv_file)
#     for row in csv.DictReader(csv_file):
#         if Class1.objects.filter(class_name = row['Class']).exists():
#             # print("Yes")
#             pass
#         elif Manufacturer.objects.filter(manufacturer_name = row['Manufacturer'] ).exists():
#             # print("Cat exist")
#             pass
#         else:
#             if row['Class']:
#                 stock_class=Class1.objects.create(class_name = row['Class'])
#                 print('Stock class:', stock_class.class_name)
#                 stock_class.save()
#             if row['Category']:
#                 category = Category.objects.create(category_name = row['Category'], class_name = stock_class )
#                 category.save()
#             if row['Subcategory']:
#                 subcategory = Category.objects.create(subcategory_name = row['Subcategory'], category_name = category )
#                 subcategory.save()
#             if row['Manufacturer']:
#                 manufacturer = Manufacturer.objects.create(manufacturer_name = row['Manufacturer'], class_name=stock_class, subcat_name = category )
#                 manufacturer.save()
#             if row['Model']:
#                 model = Model.objects.create(model_name = row['Model'], class_name=stock_class, subcat_name = category, manufacturer_name = manufacturer )
#                 model.save()

# def get_random_string(length):
#     # choose from all lowercase letter
#     letters = string.ascii_lowercase
#     result_str = ''.join(random.choice(letters) for i in range(length))
#     print("Random string of length", length, "is:", result_str)

# get_random_string(8)
# get_random_string(6)
# get_random_string(4)

# Stock.objects.all().delete()

# Stock.objects.all().filter(Class = 'Net Adapter-Lab', Substatus='Available').delete()
# for i in range(0,1):
    # stock=Stock.objects.create(name=get_random_string(6), Name =get_random_string(6),  SSN=get_random_string(6), Class='Net Adapter-Lab',
    #                 DNUSAN=get_random_string(6), Shortdesc=get_random_string(6),Category='Net Adapter-Lab - vfg', Subcategory='Net Adapte', Manufacturer='Mellanox Technologies',
    #                 Model='ConnectX-6 VPI Adapter Card - MCX653106A-ECAT-SP', Status='In Stock', Substatus='Available', Program='EGS-R',Project='JKL_RASP',
    #                 PONo=get_random_string(6),POlineNo=get_random_string(6),Assignto=get_random_string(6),Ownedby=get_random_string(6),Managedby=get_random_string(6),
    #                 HomeLoc=get_random_string(6),Location=get_random_string(6),LocDetails=get_random_string(6),Created=get_random_string(6),Createdby=get_random_string(6),
    #                 Updated=get_random_string(6),Updatedby=get_random_string(6),Costcent=get_random_string(6),Comments=get_random_string(6),
    #                 FinaType=get_random_string(6),HardSuppG=get_random_string(6),HardSuppSer=get_random_string(6),LotNo=get_random_string(6),
    #                 Etag=get_random_string(6))
    
    
    # stock=Stock.objects.create(name=str(i) + "Netadapter", Name =str(i)+"name" + "Netadapter", SSN = str(i) + "Netadapter", Class= "Net Adapter-Lab",
    #                 Category='Net Adapter-Lab - vfg', Manufacturer='Mellanox Technologies',
    #                 Model='ConnectX-6 VPI Adapter Card - MCX653106A-ECAT-SP', Status='In Stock', Substatus='Available', Type='Serialwise',
    #                 )
    # stock.save()
    # stock=Stock.objects.create(name=str(i) + "Power Supply", Name =str(i)+"name" + "Power Supply", SSN = str(i) + "Power Supply", Class= "Power Supply",
    #                 Category='Power - vfg', Manufacturer='DONGGUAN GUANGSHU ELECTRICAL TECHNOLOGY CO.,LTD',
    #                 Model='SERVER SMPS;SERVER,I1600W,1600W,2CH,90Vac~264Vac,+12 - G36234-019', Status='In Stock', Substatus='Available', Type='Serialwise'
    #                 )
    
    # stock.save()
    
    # stock=Stock.objects.create(name=str(i) + "MassStorage", Name =str(i)+"name" + "MassStorage", SSN = str(i) + "MassStorage", Class= "Mass Storage Device",
    #                 Category='MassStorage - vfg', Manufacturer='abcd2',
    #                 Model='abcd Optane M.2 Nvme SSD 118GB P1600X Series; MM# 99AGG3 - Mike', Status='In Stock', Substatus='Available', Type='Serialwise'
    #                 )
    
    # stock.save()
    
    # stock=Stock.objects.create(name=str(i) + "Memory", Name =str(i)+"name" + "Memory", SSN = str(i) + "Memory", Class= "Memory",
    #                 Category='Memory - vfg', Manufacturer='Memory2.4',
    #                 Model='abcd Optane Memory', Status='In Stock', Substatus='Available', Type='Serialwise'
    #                 )
    
    # stock.save()
    
    
    
    # stock=Stock.objects.create(name=str(i) + "Cables", Name =str(i)+"name" + "Cables", SSN = str(i) + "Cables", Class= "Cables",
    #                 Category='Cables - vfg', Manufacturer='Cables2',
    #                 Model='Cables Optane M.2', Status='In Stock', Substatus='Reserved',
    #                 )
    
    # stock.save()
    
    # stock=Stock.objects.create(name=str(i) + "Test Debug Card", Name =str(i)+"name" + "Test Debug Card", SSN = str(i) + "Test Debug Card", Class= "Test Debug Card",
    #                 Category='TestCard - vfg', Manufacturer='TestCard2.4',
    #                 Model='abcd Optane TestCard', Status='In Stock', Substatus='Reserved',
    #                 )
    
    # stock.save()
    
    
    # stock=Stock.objects.create(name=str(i) + "Type1Cables", Name =str(i)+"name" + "Type1Cables", SSN = str(i) + "Type1Cables", Class= "Cables",
    #                 Category='CablesType1 - vfg', Manufacturer='Type1Cables',
    #                 Model='Type1Cables Optane M.2', Status='In Stock', Substatus='Available', Type='Lotwise', Count='300'
    #                 )
    
    # stock.save()
    # stock=Stock.objects.create(name=str(i) + "Type2Cables", Name =str(i)+"name" + "Type2Cables", SSN = str(i) + "Type2Cables", Class= "Cables",
    #                 Category='CablesType2 - vfg', Manufacturer='Type2Cables',
    #                 Model='Type2Cables Optane M.2', Status='In Stock', Substatus='Available', Type='Lotwise', Count='440'
    #                 )
    
    # stock.save()
    # stock=Stock.objects.create(name=str(i) + "Type3Cables", Name =str(i)+"name" + "Type3Cables", SSN = str(i) + "Type3Cables", Class= "Cables",
    #                 Category='CablesType3 - vfg', Manufacturer='Type3Cables2',
    #                 Model='Type3Cables Optane M.2', Status='In Stock', Substatus='Available', Type='Lotwise', Count='120'
    #                 )
    
    # stock.save()
    
    
    # if Class1.objects.filter(class_name = str(i) + "Power Supply").exists():
    #     # print("Yes")
    #     continue
    # if Class1.objects.filter(class_name = str(int(i-1)) + "Power Supply").exists():
    #     # print("Yes")
    #     continue
    # stock_class=Class1.objects.create(class_name = str(i) + "Power Supply")
    # print('Stock class:', stock_class.class_name)
    # stock_class.save()
            
    # category = Category.objects.create(category_name = 'Power - vfg', class_name = stock_class )
    # category.save()
            
    # subcategory = Category.objects.create(subcategory_name = 'Power SubCat - vfg', category_name = category )
    # subcategory.save()
            
    # manufacturer = Manufacturer.objects.create(manufacturer_name = 'DONGGUAN GUANGSHU ELECTRICAL TECHNOLOGY CO.,LTD', class_name=stock_class, subcat_name = category )
    # manufacturer.save()
            
    # model = Model.objects.create(model_name = 'SERVER SMPS;SERVER,I1600W,1600W,2CH,90Vac~264Vac,+12 - G36234-019', class_name=stock_class, subcat_name = category, manufacturer_name = manufacturer )
    # model.save()
    
    # stock=Stock(name=get_random_string(6), Name =get_random_string(6),  SSN=get_random_string(6), Class='Net Adapter-Lab',
    #                 Category='Net Adapter-Lab - vfg', Manufacturer='Mellanox Technologies',
    #                 Model='ConnectX-6 VPI Adapter Card - MCX653106A-ECAT-SP', Substatus='Available')
    # stock.save()

# print("Stocks count is:", Stock.objects.all().count())
@login_required(login_url="/login/")
def index(request):

    # if request.GET.get('page'):
    #     my_data = Stock.objects.all()
    #     paginator = Paginator(my_data, int(Stock.objects.all().count()))
    #     page_number = request.GET.get('page')
    #     page_obj = paginator.get_page(page_number)
    #     return render(request, 'home/index.html', {'page_obj': page_obj})

    if request.method =='GET':

        my_data = Stock.objects.all()
        # paginator = Paginator(my_data, 10)
        # page_number = request.GET.get('page')
        # page_obj = paginator.get_page(page_number)

        # labels = ['Silicon', 'Mass Storage Device', 'Docking Add-on Board', 'Power Supply', 'Test Debug Card', 'Memory', 'Network Gear', 'Cables', 'Net Adapter-Lab']
        data = ['10','4','67','399','49','500','10','61','690']

        assignlab = ['HTHT9439HT0 - Mike', 'HT07HT6236 - vfg', 'HT063638HT - TURNER, GARY P', 'HT2HT74662 - MORGAN, RANDALL']
        assigndata = ['45', '22', '1607','8']

        classes = []
        Name = []
        SNo = []
        Dnusan = []
        category = []
        manufacturer = []
        model = []
        hardware_status = []
        Substatus = []
        Program = []
        Project = []
        PO_No = []
        PO_lineNo = []
        Assignto = []
        Ownedby = []

        Managedby = []
        HomeLoc = []
        Location = []
        LocDetail = []
        Created = []
        Createdby = []

        Updated = []
        Updatedby = []
        Costcenter = []
        Comments = []
        FinType = []
        HardSupp = []
        HardSuppService = []
        Etag = []
        # for i in Stock.objects.all():
        #     # print("Class is:", i.Class)
        #     if i.Class == "False":
        #         pass
        #     else:
        #         classes.append(i.Class)
        #         Name.append(i.Name)
        #         SNo.append(i.SSN)
        #         Dnusan.append(i.DNUSAN)
        #         category.append(i.Category)

        #         manufacturer.append(i.Manufacturer)
        #         model.append(i.Model)
        #         hardware_status.append(i.Status)
        #         Substatus.append(i.Substatus)
        #         Program.append(i.Program)
        #         Project.append(i.Project)
        #         PO_No.append(i.PONo)
        #         PO_lineNo.append(i.POlineNo)
        #         Assignto.append(i.Assignto)
        #         Ownedby.append(i.Ownedby)

        #         Managedby.append(i.Managedby)
        #         HomeLoc.append(i.HomeLoc)
        #         Location.append(i.Location)
        #         LocDetail.append(i.LocDetails)
        #         Created.append(i.Created)
        #         Createdby.append(i.Createdby)

        #         Updated.append(i.Updated)
        #         Updatedby.append(i.Updatedby)
        #         Costcenter.append(i.Costcent)
        #         Comments.append(i.Comments)
        #         FinType.append(i.FinaType)
        #         HardSupp.append(i.HardSuppG)
        #         HardSuppService.append(i.HardSuppSer)
        #         Etag.append(i.Etag)
        
        # alldata = []
        # for i in range(len(classes)):
        #     alldata.append([i+1, Name[i], SNo[i], Dnusan[i], classes[i], category[i],
        #                     manufacturer[i], model[i], hardware_status[i], Substatus[i], Program[i],
        #                     Project[i], PO_No[i], PO_lineNo[i], Assignto[i], Ownedby[i],
        #                     Managedby[i], HomeLoc[i], Location[i], LocDetail[i], Created[i],
        #                     Createdby[i], Updated[i], Updatedby[i], Costcenter[i], Comments[i],
        #                     FinType[i], HardSupp[i], HardSuppService[i], Etag[i]])


                
        # stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
        # for item in stockqueryset:
        #     labels.append(item.name)
        #     data.append(item.quantity)
        # sales = SaleBill.objects.order_by('-time')[:3]
        # purchases = PurchaseBill.objects.order_by('-time')[:3]


        # classes1 = []
        # for i in Stock.objects.all():
        #     # print("Class is:", i.Class)
        #     if i.Class == "False":
        #         pass
        #     else:
        #         classes1.append(i.Class)

        # print("Classes are:", set(classes1))

        #############For Bar graph
        # labels = []
        # stockval = [] 
        # stockin = []
        # stockout = []
        # stockpending = []
        # stockreserved = []

        # for i in set(classes1):
        #     labels.append(i)
        #     # print(f"Stock Available for {i}:", Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Available").count())
        #     stockval.append(Stock.objects.filter(Class__icontains = i).count())
        #     stockin.append(Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Available").count())
        #     stockout.append(Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Not Available").count())
        #     stockpending.append(Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Pending Retirement").count())
        #     stockreserved.append(Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Reserved").count())
#For Bar graph

        # for i in set(classes1):
        #     stockout.append(Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Not Available").count())
        # for i in set(classes1):
        #     stockpending.append(Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Pending Retirement").count())
        # for i in set(classes1):
        #     stockreserved.append(Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Reserved").count())
        
        
        
        # print("All Stock:",stockval, "Stockin:", stockin, "stockout:", stockout, "stockpending:", stockpending, "stockreserved:", stockreserved)

        model1 = Model.objects.all()
        manufacturer1 = Manufacturer.objects.all()
        context = {
            # 'labels'    : labels,
            'data'      : data,
            'assignlab' : assignlab,
            'assigndata' : assigndata,

            # 'alldata' : alldata,

            'segment': 'home',

            'model1': model1,
            'manufacturer1': manufacturer1,
            # 'page_obj': page_obj,
            'my_data': my_data
            # 'purchases' : purchases
        }
        return render(request, 'home/index.html', context)
    

        # html_template = loader.get_template('home/home.html')
        # return HttpResponse(html_template.render(context, request))
    
    if request.method =='POST':

        html_template = loader.get_template('home/index.html')
        return HttpResponse(html_template.render(context, request))
    
# Create Config
@login_required(login_url="/login/")
def CreateConfig(request):
    context = {'segment': 'index'}
    
    if request.method =='GET':
        classnames_all = Class1.objects.all()
        all_configs = ConfigName.objects.all()
        print("Class value from select:", request.GET.get('class', None))
        context = {
            'segment': 'createconfig',
            'allclassnames': classnames_all,
            'all_configs': all_configs

        }
        # return render(request, self.template_name, context)
        return render(request, 'home/createconfig.html', context)
    

        # html_template = loader.get_template('home/home.html')
        # return HttpResponse(html_template.render(context, request))
    
    if request.method =='POST':
        # print("Request user name:", request.user)
        classnames_all = Class1.objects.all()

        all_configs = ConfigName.objects.all()
        context = {
            'segment': 'createconfig',
            'allclassnames': classnames_all,
            'all_configs': all_configs
        }

        # print("Conf name:", request.POST.get('configname'))
        if request.POST.get('configname'):
            if ConfigName.objects.filter(name = request.POST.get('configname')):
                print("Config with same name exist")
                exit
            else:
                # config_name.save()
                print("Qua1 is:", request.POST.get('qua1'))
                if request.POST['selclass1'] != '--- Select Class ---' and request.POST['selcat1'] != '--- Select Category ---' and request.POST['selmanu1'] != '--- Select Manufacturer ---' and request.POST['selmodel1'] != '--- Select Model ---' and request.POST.get('qua1'):
                    config_name = ConfigName.objects.create(name = request.POST.get('configname'))
                    print("Request post class:", Class1.objects.get(id = request.POST['selclass1']).class_name)
                    print("Request post Category:", Category.objects.get(id = request.POST['selcat1']).category_name)
                    print("Request post Manufacturer:", Manufacturer.objects.get(id = request.POST['selmanu1']).manufacturer_name)
                    print("Request post Model:", Model.objects.get(id = request.POST['selmodel1']).model_name)
                    
                    if request.POST.get('selclass1') and request.POST.get('selcat1') and request.POST.get('selmanu1') and request.POST.get('selmodel1') and request.POST.get('qua1'):
                        print("Yes1")
                        config1 = Config.objects.create(name=config_name, Class=Class1.objects.get(id = request.POST['selclass1']).class_name, Category=Category.objects.get(id = request.POST['selcat1']).category_name,
                                                        Manufacturer=Manufacturer.objects.get(id = request.POST['selmanu1']).manufacturer_name, Model=Model.objects.get(id = request.POST['selmodel1']).model_name, quantity=request.POST.get('qua1') )
                        config1.save()
                    if request.POST.get('selclass2') and request.POST.get('selcat2') and request.POST.get('selmanu2') and request.POST.get('selmodel2') and request.POST.get('qua2'):
                        print("Yes2")
                        config1 = Config.objects.create(name=config_name, Class=Class1.objects.get(id = request.POST['selclass2']).class_name, Category=Category.objects.get(id = request.POST['selcat2']).category_name,
                                                        Manufacturer=Manufacturer.objects.get(id = request.POST['selmanu2']).manufacturer_name, Model=Model.objects.get(id = request.POST['selmodel2']).model_name, quantity=request.POST.get('qua2') )
                        config1.save()
                    if request.POST.get('selclass3') and request.POST.get('selcat3') and request.POST.get('selmanu3') and request.POST.get('selmodel3') and request.POST.get('qua3'):
                        print("Yes3")
                        config1 = Config.objects.create(name=config_name, Class=Class1.objects.get(id = request.POST['selclass3']).class_name, Category=Category.objects.get(id = request.POST['selcat3']).category_name,
                                                        Manufacturer=Manufacturer.objects.get(id = request.POST['selmanu3']).manufacturer_name, Model=Model.objects.get(id = request.POST['selmodel3']).model_name, quantity=request.POST.get('qua3') )
                        config1.save()
                    if request.POST.get('selclass4') and request.POST.get('selcat4') and request.POST.get('selmanu4') and request.POST.get('selmodel4') and request.POST.get('qua4'):
                        print("Yes4")
                        config1 = Config.objects.create(name=config_name, Class=Class1.objects.get(id = request.POST['selclass4']).class_name, Category=Category.objects.get(id = request.POST['selcat4']).category_name,
                                                        Manufacturer=Manufacturer.objects.get(id = request.POST['selmanu4']).manufacturer_name, Model=Model.objects.get(id = request.POST['selmodel4']).model_name, quantity=request.POST.get('qua4') )
                        config1.save()
                    if request.POST.get('selclass5') and request.POST.get('selcat5') and request.POST.get('selmanu5') and request.POST.get('selmodel5') and request.POST.get('qua5'):
                        print("Yes5")
                        config1 = Config.objects.create(name=config_name, Class=Class1.objects.get(id = request.POST['selclass5']).class_name, Category=Category.objects.get(id = request.POST['selcat5']).category_name,
                                                        Manufacturer=Manufacturer.objects.get(id = request.POST['selmanu5']).manufacturer_name, Model=Model.objects.get(id = request.POST['selmodel5']).model_name, quantity=request.POST.get('qua5') )
                        config1.save()
                    if request.POST.get('selclass6') and request.POST.get('selcat6') and request.POST.get('selmanu6') and request.POST.get('selmodel6') and request.POST.get('qua6'):
                        print("Yes6")
                        config1 = Config.objects.create(name=config_name, Class=Class1.objects.get(id = request.POST['selclass6']).class_name, Category=Category.objects.get(id = request.POST['selcat6']).category_name,
                                                        Manufacturer=Manufacturer.objects.get(id = request.POST['selmanu6']).manufacturer_name, Model=Model.objects.get(id = request.POST['selmodel6']).model_name, quantity=request.POST.get('qua6') )
                        config1.save()
        else:
            # for row 1
            # print("Request:", json.loads(request.body))
            if 'class1' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['class1'])

                conname = Class1.objects.get(id = json.loads(request.body)['class1'])
                cat_list1 = Category.objects.filter(class_name = conname)
                instances = serializers.serialize('json', cat_list1)
                print(conname, cat_list1)
                context['cat_list1'] = cat_list1
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'category1' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['category1'])

                conname = Category.objects.get(id = json.loads(request.body)['category1'])
                manu_list1 = Manufacturer.objects.filter(subcat_name = conname)
                instances = serializers.serialize('json', manu_list1)
                print(conname, manu_list1)
                context['manu_list1'] = manu_list1
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'manu1' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['manu1'])

                conname = Manufacturer.objects.get(id = json.loads(request.body)['manu1'])
                model_list1 = Model.objects.filter(manufacturer_name = conname)
                instances = serializers.serialize('json', model_list1)
                print(conname, model_list1)
                context['model_list1'] = model_list1
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            # 2nd row
            if 'class2' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['class2'])

                conname = Class1.objects.get(id = json.loads(request.body)['class2'])
                cat_list2 = Category.objects.filter(class_name = conname)
                instances = serializers.serialize('json', cat_list2)
                print(conname, cat_list2)
                context['cat_list2'] = cat_list2
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'category2' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['category2'])

                conname = Category.objects.get(id = json.loads(request.body)['category2'])
                manu_list2 = Manufacturer.objects.filter(subcat_name = conname)
                instances = serializers.serialize('json', manu_list2)
                print(conname, manu_list2)
                context['manu_list2'] = manu_list2
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'manu2' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['manu2'])

                conname = Manufacturer.objects.get(id = json.loads(request.body)['manu2'])
                model_list2 = Model.objects.filter(manufacturer_name = conname)
                instances = serializers.serialize('json', model_list2)
                print(conname, model_list2)
                context['model_list2'] = model_list2
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            # 3rd row
            if 'class3' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['class3'])

                conname = Class1.objects.get(id = json.loads(request.body)['class3'])
                cat_list3 = Category.objects.filter(class_name = conname)
                instances = serializers.serialize('json', cat_list3)
                print(conname, cat_list3)
                context['cat_list3'] = cat_list3
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'category3' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['category3'])

                conname = Category.objects.get(id= json.loads(request.body)['category3'])
                manu_list3 = Manufacturer.objects.filter(subcat_name = conname)
                instances = serializers.serialize('json', manu_list3)
                print(conname, manu_list3)
                context['manu_list3'] = manu_list3
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'manu3' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['manu3'])

                conname = Manufacturer.objects.get(id = json.loads(request.body)['manu3'])
                model_list3 = Model.objects.filter(manufacturer_name = conname)
                instances = serializers.serialize('json', model_list3)
                print(conname, model_list3)
                context['model_list3'] = model_list3
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            # 4th row
            if 'class4' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['class4'])

                conname = Class1.objects.get(id = json.loads(request.body)['class4'])
                cat_list4 = Category.objects.filter(class_name = conname)
                instances = serializers.serialize('json', cat_list4)
                print(conname, cat_list4)
                context['cat_list4'] = cat_list4
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'category4' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['category4'])

                conname = Category.objects.get(id= json.loads(request.body)['category4'])
                manu_list4 = Manufacturer.objects.filter(subcat_name = conname)
                instances = serializers.serialize('json', manu_list4)
                print(conname, manu_list4)
                context['manu_list4'] = manu_list4
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'manu4' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['manu4'])

                conname = Manufacturer.objects.get(id = json.loads(request.body)['manu4'])
                model_list4 = Model.objects.filter(manufacturer_name = conname)
                instances = serializers.serialize('json', model_list4)
                print(conname, model_list4)
                context['model_list4'] = model_list4
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            # 5th row
            if 'class5' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body))

                conname = Class1.objects.get(id = json.loads(request.body)['class5'])
                cat_list5 = Category.objects.filter(class_name = conname)
                instances = serializers.serialize('json', cat_list5)
                print(conname, cat_list5)
                context['cat_list5'] = cat_list5
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'category5' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['category5'])

                conname = Category.objects.get(id= json.loads(request.body)['category5'])
                manu_list5 = Manufacturer.objects.filter(subcat_name = conname)
                instances = serializers.serialize('json', manu_list5)
                print(conname, manu_list5)
                context['manu_list5'] = manu_list5
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'manu5' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['manu5'])

                conname = Manufacturer.objects.get(id = json.loads(request.body)['manu5'])
                model_list5 = Model.objects.filter(manufacturer_name = conname)
                instances = serializers.serialize('json', model_list5)
                print(conname, model_list5)
                context['model_list5'] = model_list5
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            # 6th row
            if 'class6' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body))

                conname = Class1.objects.get(id = json.loads(request.body)['class6'])
                cat_list6 = Category.objects.filter(class_name = conname)
                instances = serializers.serialize('json', cat_list6)
                print(conname, cat_list6)
                context['cat_list6'] = cat_list6
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'category6' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['category6'])

                conname = Category.objects.get(id= json.loads(request.body)['category6'])
                manu_list6 = Manufacturer.objects.filter(subcat_name = conname)
                instances = serializers.serialize('json', manu_list6)
                print(conname, manu_list6)
                context['manu_list6'] = manu_list6
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'manu6' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['manu6'])

                conname = Manufacturer.objects.get(id = json.loads(request.body)['manu6'])
                model_list6 = Model.objects.filter(manufacturer_name = conname)
                instances = serializers.serialize('json', model_list6)
                print(conname, model_list6)
                context['model_list6'] = model_list6
                return HttpResponse(instances, content_type='application/json')
            
            # For Config list select
            if 'selconfig' in json.loads(request.body):
                print("selconfig value from select:", json.loads(request.body)['selconfig'])

                configs = []

                allclass = []
                allcategory = []
                allmanu = []
                allmodel = []
                allquantity = []
                reservedby = []
                
                conname = ConfigName.objects.get(id = json.loads(request.body)['selconfig'])
                config3 = Config.objects.filter(name = conname)
                for j in config3:
                    allclass.append(j.Class)
                    allcategory.append(j.Category)
                    allmanu.append(j.Manufacturer)
                    allmodel.append(j.Model)
                    allquantity.append(j.quantity)
                    if Stock.objects.filter(Class = j.Class, Category = j.Category, Manufacturer = j.Manufacturer, Model = j.Model, Reservedby = request.user, Configname = conname).count() > 0:
                        reservedby.append(str(request.user))

                concontxt = {"allclass":allclass, 'allcategory':allcategory, 'allmanu':allmanu, 'allmodel':allmodel,
                                     'allquantity':allquantity}
                if len(reservedby) > 0:
                    concontxt['reservedby'] = reservedby[0]
                else:
                    concontxt['reservedby'] = " "
                # Stock.objects.filter(Class = "Net Adapter-Lab", Category = "Net Adapter-Lab - vfg", Manufacturer = "Mellanox Technologies", Model = "ConnectX-6 VPI Adapter Card - MCX653106A-ECAT-SP", Substatus__icontains = "Reserved", Reservedby = request.user, Configname = json.loads(request.body)['selconfig'])
                # print(allclass,allcategory,allmanu,allmodel,allquantity)
                return JsonResponse(concontxt)

        
        return render(request, 'home/createconfig.html', context)
        # html_template = loader.get_template('home/index.html')
        # return HttpResponse(html_template.render(context, request))

# ConfigScan
@login_required(login_url="/login/")
def ConfigScan(request):
    context = {'segment': 'index'}
    
    if request.method =='GET':
        classnames_all = Class1.objects.all()
        all_configs = ConfigName.objects.all()
        print("Class value from select:", request.GET.get('class', None))
        context = {
            'segment': 'configscan',
            'allclassnames': classnames_all,
            'all_configs': all_configs

        }
        # return render(request, self.template_name, context)
        return render(request, 'home/configscan.html', context)
    

        # html_template = loader.get_template('home/home.html')
        # return HttpResponse(html_template.render(context, request))
    
    if request.method =='POST':
        # print("Request user name:", request.user)
        classnames_all = Class1.objects.all()

        all_configs = ConfigName.objects.all()
        context = {
            'segment': 'configscan',
            'allclassnames': classnames_all,
            'all_configs': all_configs
        }

        # print("Conf name:", request.POST.get('configname'))
        if request.POST.get('configname'):
            if ConfigName.objects.filter(name = request.POST.get('configname')):
                print("Config with same name exist")
                exit
            else:
                # config_name.save()
                print("Qua1 is:", request.POST.get('qua1'))
                if request.POST['selclass1'] != '--- Select Class ---' and request.POST['selcat1'] != '--- Select Category ---' and request.POST['selmanu1'] != '--- Select Manufacturer ---' and request.POST['selmodel1'] != '--- Select Model ---' and request.POST.get('qua1'):
                    config_name = ConfigName.objects.create(name = request.POST.get('configname'))
                    print("Request post class:", Class1.objects.get(id = request.POST['selclass1']).class_name)
                    print("Request post Category:", Category.objects.get(id = request.POST['selcat1']).category_name)
                    print("Request post Manufacturer:", Manufacturer.objects.get(id = request.POST['selmanu1']).manufacturer_name)
                    print("Request post Model:", Model.objects.get(id = request.POST['selmodel1']).model_name)
                    
                    if request.POST.get('selclass1') and request.POST.get('selcat1') and request.POST.get('selmanu1') and request.POST.get('selmodel1') and request.POST.get('qua1'):
                        print("Yes1")
                        config1 = Config.objects.create(name=config_name, Class=Class1.objects.get(id = request.POST['selclass1']).class_name, Category=Category.objects.get(id = request.POST['selcat1']).category_name,
                                                        Manufacturer=Manufacturer.objects.get(id = request.POST['selmanu1']).manufacturer_name, Model=Model.objects.get(id = request.POST['selmodel1']).model_name, quantity=request.POST.get('qua1') )
                        config1.save()
                    if request.POST.get('selclass2') and request.POST.get('selcat2') and request.POST.get('selmanu2') and request.POST.get('selmodel2') and request.POST.get('qua2'):
                        print("Yes2")
                        config1 = Config.objects.create(name=config_name, Class=Class1.objects.get(id = request.POST['selclass2']).class_name, Category=Category.objects.get(id = request.POST['selcat2']).category_name,
                                                        Manufacturer=Manufacturer.objects.get(id = request.POST['selmanu2']).manufacturer_name, Model=Model.objects.get(id = request.POST['selmodel2']).model_name, quantity=request.POST.get('qua2') )
                        config1.save()
                    if request.POST.get('selclass3') and request.POST.get('selcat3') and request.POST.get('selmanu3') and request.POST.get('selmodel3') and request.POST.get('qua3'):
                        print("Yes3")
                        config1 = Config.objects.create(name=config_name, Class=Class1.objects.get(id = request.POST['selclass3']).class_name, Category=Category.objects.get(id = request.POST['selcat3']).category_name,
                                                        Manufacturer=Manufacturer.objects.get(id = request.POST['selmanu3']).manufacturer_name, Model=Model.objects.get(id = request.POST['selmodel3']).model_name, quantity=request.POST.get('qua3') )
                        config1.save()
                    if request.POST.get('selclass4') and request.POST.get('selcat4') and request.POST.get('selmanu4') and request.POST.get('selmodel4') and request.POST.get('qua4'):
                        print("Yes4")
                        config1 = Config.objects.create(name=config_name, Class=Class1.objects.get(id = request.POST['selclass4']).class_name, Category=Category.objects.get(id = request.POST['selcat4']).category_name,
                                                        Manufacturer=Manufacturer.objects.get(id = request.POST['selmanu4']).manufacturer_name, Model=Model.objects.get(id = request.POST['selmodel4']).model_name, quantity=request.POST.get('qua4') )
                        config1.save()
                    if request.POST.get('selclass5') and request.POST.get('selcat5') and request.POST.get('selmanu5') and request.POST.get('selmodel5') and request.POST.get('qua5'):
                        print("Yes5")
                        config1 = Config.objects.create(name=config_name, Class=Class1.objects.get(id = request.POST['selclass5']).class_name, Category=Category.objects.get(id = request.POST['selcat5']).category_name,
                                                        Manufacturer=Manufacturer.objects.get(id = request.POST['selmanu5']).manufacturer_name, Model=Model.objects.get(id = request.POST['selmodel5']).model_name, quantity=request.POST.get('qua5') )
                        config1.save()
                    if request.POST.get('selclass6') and request.POST.get('selcat6') and request.POST.get('selmanu6') and request.POST.get('selmodel6') and request.POST.get('qua6'):
                        print("Yes6")
                        config1 = Config.objects.create(name=config_name, Class=Class1.objects.get(id = request.POST['selclass6']).class_name, Category=Category.objects.get(id = request.POST['selcat6']).category_name,
                                                        Manufacturer=Manufacturer.objects.get(id = request.POST['selmanu6']).manufacturer_name, Model=Model.objects.get(id = request.POST['selmodel6']).model_name, quantity=request.POST.get('qua6') )
                        config1.save()
        else:
            # for row 1
            # print("Request:", json.loads(request.body))
            if 'class1' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['class1'])

                conname = Class1.objects.get(id = json.loads(request.body)['class1'])
                cat_list1 = Category.objects.filter(class_name = conname)
                instances = serializers.serialize('json', cat_list1)
                print(conname, cat_list1)
                context['cat_list1'] = cat_list1
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'category1' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['category1'])

                conname = Category.objects.get(id = json.loads(request.body)['category1'])
                manu_list1 = Manufacturer.objects.filter(subcat_name = conname)
                instances = serializers.serialize('json', manu_list1)
                print(conname, manu_list1)
                context['manu_list1'] = manu_list1
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'manu1' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['manu1'])

                conname = Manufacturer.objects.get(id = json.loads(request.body)['manu1'])
                model_list1 = Model.objects.filter(manufacturer_name = conname)
                instances = serializers.serialize('json', model_list1)
                print(conname, model_list1)
                context['model_list1'] = model_list1
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            # 2nd row
            if 'class2' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['class2'])

                conname = Class1.objects.get(id = json.loads(request.body)['class2'])
                cat_list2 = Category.objects.filter(class_name = conname)
                instances = serializers.serialize('json', cat_list2)
                print(conname, cat_list2)
                context['cat_list2'] = cat_list2
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'category2' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['category2'])

                conname = Category.objects.get(id = json.loads(request.body)['category2'])
                manu_list2 = Manufacturer.objects.filter(subcat_name = conname)
                instances = serializers.serialize('json', manu_list2)
                print(conname, manu_list2)
                context['manu_list2'] = manu_list2
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'manu2' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['manu2'])

                conname = Manufacturer.objects.get(id = json.loads(request.body)['manu2'])
                model_list2 = Model.objects.filter(manufacturer_name = conname)
                instances = serializers.serialize('json', model_list2)
                print(conname, model_list2)
                context['model_list2'] = model_list2
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            # 3rd row
            if 'class3' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['class3'])

                conname = Class1.objects.get(id = json.loads(request.body)['class3'])
                cat_list3 = Category.objects.filter(class_name = conname)
                instances = serializers.serialize('json', cat_list3)
                print(conname, cat_list3)
                context['cat_list3'] = cat_list3
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'category3' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['category3'])

                conname = Category.objects.get(id= json.loads(request.body)['category3'])
                manu_list3 = Manufacturer.objects.filter(subcat_name = conname)
                instances = serializers.serialize('json', manu_list3)
                print(conname, manu_list3)
                context['manu_list3'] = manu_list3
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'manu3' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['manu3'])

                conname = Manufacturer.objects.get(id = json.loads(request.body)['manu3'])
                model_list3 = Model.objects.filter(manufacturer_name = conname)
                instances = serializers.serialize('json', model_list3)
                print(conname, model_list3)
                context['model_list3'] = model_list3
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            # 4th row
            if 'class4' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['class4'])

                conname = Class1.objects.get(id = json.loads(request.body)['class4'])
                cat_list4 = Category.objects.filter(class_name = conname)
                instances = serializers.serialize('json', cat_list4)
                print(conname, cat_list4)
                context['cat_list4'] = cat_list4
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'category4' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['category4'])

                conname = Category.objects.get(id= json.loads(request.body)['category4'])
                manu_list4 = Manufacturer.objects.filter(subcat_name = conname)
                instances = serializers.serialize('json', manu_list4)
                print(conname, manu_list4)
                context['manu_list4'] = manu_list4
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'manu4' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['manu4'])

                conname = Manufacturer.objects.get(id = json.loads(request.body)['manu4'])
                model_list4 = Model.objects.filter(manufacturer_name = conname)
                instances = serializers.serialize('json', model_list4)
                print(conname, model_list4)
                context['model_list4'] = model_list4
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            # 5th row
            if 'class5' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body))

                conname = Class1.objects.get(id = json.loads(request.body)['class5'])
                cat_list5 = Category.objects.filter(class_name = conname)
                instances = serializers.serialize('json', cat_list5)
                print(conname, cat_list5)
                context['cat_list5'] = cat_list5
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'category5' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['category5'])

                conname = Category.objects.get(id= json.loads(request.body)['category5'])
                manu_list5 = Manufacturer.objects.filter(subcat_name = conname)
                instances = serializers.serialize('json', manu_list5)
                print(conname, manu_list5)
                context['manu_list5'] = manu_list5
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'manu5' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['manu5'])

                conname = Manufacturer.objects.get(id = json.loads(request.body)['manu5'])
                model_list5 = Model.objects.filter(manufacturer_name = conname)
                instances = serializers.serialize('json', model_list5)
                print(conname, model_list5)
                context['model_list5'] = model_list5
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            # 6th row
            if 'class6' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body))

                conname = Class1.objects.get(id = json.loads(request.body)['class6'])
                cat_list6 = Category.objects.filter(class_name = conname)
                instances = serializers.serialize('json', cat_list6)
                print(conname, cat_list6)
                context['cat_list6'] = cat_list6
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'category6' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['category6'])

                conname = Category.objects.get(id= json.loads(request.body)['category6'])
                manu_list6 = Manufacturer.objects.filter(subcat_name = conname)
                instances = serializers.serialize('json', manu_list6)
                print(conname, manu_list6)
                context['manu_list6'] = manu_list6
                # return JsonResponse({"cat_list1":instances})
                return HttpResponse(instances, content_type='application/json')
            
            if 'manu6' in json.loads(request.body):
                print("Class value from select:", json.loads(request.body)['manu6'])

                conname = Manufacturer.objects.get(id = json.loads(request.body)['manu6'])
                model_list6 = Model.objects.filter(manufacturer_name = conname)
                instances = serializers.serialize('json', model_list6)
                print(conname, model_list6)
                context['model_list6'] = model_list6
                return HttpResponse(instances, content_type='application/json')
            
            # For Config list select
            if 'selconfig' in json.loads(request.body):
                print("selconfig value from select:", json.loads(request.body)['selconfig'])

                configs = []
                concontxt = {}

                allclass = []
                allcategory = []
                allmanu = []
                allmodel = []
                allquantity = []
                reservedby = []
                ssn = []
                
                cout = 0
                conname = ConfigName.objects.get(id = json.loads(request.body)['selconfig'])
                config3 = Config.objects.filter(name = conname)
                for j in config3:
                    allclass.append(j.Class)
                    allcategory.append(j.Category)
                    allmanu.append(j.Manufacturer)
                    allmodel.append(j.Model)
                    allquantity.append(j.quantity)
                    if cout == 0:
                        if Stock.objects.filter(Class = j.Class, Category = j.Category, Manufacturer = j.Manufacturer, Model = j.Model, Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name).count() > 0:
                            reservedby.append(str(request.user))
                            cout+=1
                
                buildno = 0
                sss = []
                if len(allquantity) > 0:
                    if len(allquantity) == 1:
                        print("One")
                        # [:int(allquantity[0])]
                        for i in Stock.objects.filter(Class = allclass[0], Category = allcategory[0], Manufacturer = allmanu[0], Model = allmodel[0], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                        print("Length of SSS", len(sss))
                        buildno = len(sss)/int(allquantity[0])
                    if len(allquantity) == 2:
                        print("Two")
                        for i in Stock.objects.filter(Class = allclass[0], Category = allcategory[0], Manufacturer = allmanu[0], Model = allmodel[0], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                        print("Length of SSS", len(sss))
                        buildno = len(sss)/int(allquantity[0])
                        sss = []
                        for i in Stock.objects.filter(Class = allclass[1], Category = allcategory[1], Manufacturer = allmanu[1], Model = allmodel[1], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                    
                    if len(allquantity) == 3:
                        print("Two")
                        for i in Stock.objects.filter(Class = allclass[0], Category = allcategory[0], Manufacturer = allmanu[0], Model = allmodel[0], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                        buildno = len(sss)/int(allquantity[0])
                        sss = []
                        for i in Stock.objects.filter(Class = allclass[1], Category = allcategory[1], Manufacturer = allmanu[1], Model = allmodel[1], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                        sss = []
                        for i in Stock.objects.filter(Class = allclass[2], Category = allcategory[2], Manufacturer = allmanu[2], Model = allmodel[2], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                    
                    if len(allquantity) == 4:
                        print("Two")
                        for i in Stock.objects.filter(Class = allclass[0], Category = allcategory[0], Manufacturer = allmanu[0], Model = allmodel[0], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                        buildno = len(sss)/int(allquantity[0])
                        sss = []
                        for i in Stock.objects.filter(Class = allclass[1], Category = allcategory[1], Manufacturer = allmanu[1], Model = allmodel[1], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                        sss = []
                        for i in Stock.objects.filter(Class = allclass[2], Category = allcategory[2], Manufacturer = allmanu[2], Model = allmodel[2], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                        sss = []
                        for i in Stock.objects.filter(Class = allclass[3], Category = allcategory[3], Manufacturer = allmanu[3], Model = allmodel[3], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                    
                    if len(allquantity) == 5:
                        print("Two")
                        for i in Stock.objects.filter(Class = allclass[0], Category = allcategory[0], Manufacturer = allmanu[0], Model = allmodel[0], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                        buildno = len(sss)/int(allquantity[0])
                        sss = []
                        for i in Stock.objects.filter(Class = allclass[1], Category = allcategory[1], Manufacturer = allmanu[1], Model = allmodel[1], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                        sss = []
                        for i in Stock.objects.filter(Class = allclass[2], Category = allcategory[2], Manufacturer = allmanu[2], Model = allmodel[2], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                        sss = []
                        for i in Stock.objects.filter(Class = allclass[3], Category = allcategory[3], Manufacturer = allmanu[3], Model = allmodel[3], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                        sss = []
                        for i in Stock.objects.filter(Class = allclass[4], Category = allcategory[4], Manufacturer = allmanu[4], Model = allmodel[4], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                    
                    if len(allquantity) == 6:
                        print("Two")
                        for i in Stock.objects.filter(Class = allclass[0], Category = allcategory[0], Manufacturer = allmanu[0], Model = allmodel[0], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                        buildno = len(sss)/int(allquantity[0])
                        sss = []
                        for i in Stock.objects.filter(Class = allclass[1], Category = allcategory[1], Manufacturer = allmanu[1], Model = allmodel[1], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                        sss = []
                        for i in Stock.objects.filter(Class = allclass[2], Category = allcategory[2], Manufacturer = allmanu[2], Model = allmodel[2], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                        sss = []
                        for i in Stock.objects.filter(Class = allclass[3], Category = allcategory[3], Manufacturer = allmanu[3], Model = allmodel[3], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                        sss = []
                        for i in Stock.objects.filter(Class = allclass[4], Category = allcategory[4], Manufacturer = allmanu[4], Model = allmodel[4], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                        sss = []
                        for i in Stock.objects.filter(Class = allclass[5], Category = allcategory[5], Manufacturer = allmanu[5], Model = allmodel[5], Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name):
                            sss.append(i.SSN)
                        print(sss)
                        ssn.append(sss)
                    # for i in range(len(allquantity)):
                    #     # for o in range(0,int(allquantity[i])):
                    #     #     print("i,j",i,o)
                    #     for s in Stock.objects.filter(Class = j.Class, Category = j.Category, Manufacturer = j.Manufacturer, Model = j.Model, Reservedby = request.user, Configname = ConfigName.objects.get(id = json.loads(request.body)['selconfig']).name)[:int(allquantity[i])]:
                    #         sss.append(s.SSN)
                    #     ssn.append(sss)

                #         for i in Stock.objects.filter(Class = j.Class, Category = j.Category, Manufacturer = j.Manufacturer, Model = j.Model, Reservedby = request.user, Configname = json.loads(request.body)['selconfig']):
                #             ssn.append(i.SSN)
                print("SSN:", ssn)

                # for i in range(0,len(allquantity)):
                #     for j in range(0,int(allquantity[i])):
                #         print("i,j",i,j)
                #         for s in Stock.objects.filter(Class = j.Class, Category = j.Category, Manufacturer = j.Manufacturer, Model = j.Model, Reservedby = request.user, Configname = json.loads(request.body)['selconfig']):
                #            ssn.append([s.SSN])
                    # if Stock.objects.filter(Class = j.Class, Category = j.Category, Manufacturer = j.Manufacturer, Model = j.Model).count() > 0:
                    #     reservedby.append(str(request.user))

                    

                # Stock.objects.filter(Class = "Net Adapter-Lab", Category = "Net Adapter-Lab - vfg", Manufacturer = "Mellanox Technologies", Model = "ConnectX-6 VPI Adapter Card - MCX653106A-ECAT-SP", Substatus__icontains = "Reserved", Reservedby = request.user, Configname = json.loads(request.body)['selconfig'])
                print(allclass,allcategory,allmanu,allmodel,allquantity)
                return JsonResponse({"allclass":allclass, 'allcategory':allcategory, 'allmanu':allmanu, 'allmodel':allmodel,
                                     'allquantity':allquantity, "reservedby":reservedby, 'ssn':ssn, 'buildno': buildno})

        
        return render(request, 'home/configscan.html', context)
        # html_template = loader.get_template('home/index.html')
        # return HttpResponse(html_template.render(context, request))

# Upload file
@login_required(login_url="/login/")
def UploadFile(request):
    if request.method == 'POST':
        # stock_resource = StockResource()
        # dataset = Dataset()
        new_person = request.FILES.get('myfile')
        # df = pd.read_csv(new_person) # usecols = ['IQ','Scores']
        # df_columns = df.head
        # print("Columns:", df_columns)
        
        reader = csv.DictReader(codecs.iterdecode(new_person, 'utf-8'), delimiter=',')
        # # imported_data = dataset.load(new_person.read(),format='xlsx')
        headers = reader.fieldnames
        # print("reader keys are:", headers)
        all_fields = [f.name for f in Stock._meta.fields]
        # print("Stocks all fields:", all_fields)

        # equal_fields = [i for i, j in zip(all_fields, headers) if i == j]  # set(all_fields) & set(headers)
        equal_fields = set(all_fields) & set(headers)
        print("Stocks equal_fields:", equal_fields)
        # for row in reader:
        #     print("Data is:", row['Serial number'])
        # form = CSVUploadForm(request.POST, request.FILES)
        
        # if form.is_valid():
        #     with open(form.cleaned_data['csv_file'], mode="r", encoding='latin1') as csv_file:
        #     # csv_file = request.FILES['file']
        #     # csv_file = form.cleaned_data['csv_file']
        #     # decoded_file = csv_file.read().decode('utf-8')
        #     # csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
        #     # print("File is:", csv_file)
        #     # for row in csv_data:
        # for row in csv.DictReader(new_person):
        #     print("Row:", row)

        # stocks_row = []
        # for i in equal_fields:
        #     stocks_row.append(f"{i='row[{i}]'}")

        ##########################
        # name=''
        # Name=''
        # SSN=''
        # Class=''
        # DNUSAN=''
        # Shortdesc=''
        # Category=''
        # Subcategory=''
        # Manufacturer=''
        # Model=''
        # Status=''
        # Substatus=''
        # Program=''
        # Project=''
        # PONo=''
        # POlineNo=''
        # Assignto=''
        # Ownedby=''
        # Managedby=''
        # HomeLoc=''
        # Location=''
        # LocDetails=''
        # Created=''
        # Createdby=''
        # Updated=''
        # Updatedby=''
        # Costcent=''
        # Comments=''
        # FinaType=''
        # HardSuppG=''
        # HardSuppSer=''
        # LotNo=''
        # Etag=''
        ##########################
        
        # for j in equal_fields:
        #     if j == i:


        
        # for i in equal_fields:

        #     if i ==  
        
        for row in reader:
            
            # if row[] != ''
            # name=row['Name']
            # Name=row['Name'], SSN=row['SSN'], Class=row['Class'],
            #             Category=row['Category'],Manufacturer=row['Manufacturer'],
            #             Model=row['Model'],Status=row['Status'],Substatus=row['Substatus'],
            #             Type=row['Type']
            
            stock=Stock(name=row['Name'], Name=row['Name'], SSN=row['Serial number'], Class=row['Class'],
                                DNUSAN=row['DNUSAN'], Shortdesc=row['Short description'],Category=row['Category'],Subcategory=row['Subcategory'],Manufacturer=row['Manufacturer'],
                                Model=row['Model'],Status=row['Status(hardware_status)'],Substatus=row['Substatus'],Program=row['Program'],Project=row['Project'],
                                PONo=row['PO number'],POlineNo=row['PO line number'],Assignto=row['Assigned to'],Ownedby=row['Owned by'],Managedby=row['Managed by'],
                                HomeLoc=row['Home Location'],Location=row['Location'],LocDetails=row['Location Details'],Created=row['Created'],Createdby=row['Created by'],
                                Updated=row['Updated'],Updatedby=row['Updgted by'],Costcent=row['Cost center'],Comments=row['Comments'],
                                FinaType=row['Finance Type'],HardSuppG=row['Hardware Support Group'],HardSuppSer=row['Hardware Support Service'],LotNo=row['Lot Number'],
                                Etag=row['Etag'])
            stock.save()
            # stock=Stock(name=row['Name'], Name=row['Name'], SSN=row['SSN'], Class=row['Class'],
            #             Category=row['Category'],Manufacturer=row['Manufacturer'],
            #             Model=row['Model'],Status=row['Status'],Substatus=row['Substatus'],
            #             Type=row['Type'])
            # stock.save()

            # for i in range(len(equal_fields)):
            #     if Stock.objects.filter(equal_fields=row['SSN'], name=row['Name'], Name=row['Name']).exists():
            #         # print("count", Stock.objects.filter(SSN=row['Serial number'], name=row['Name'], Name=row['Name']).count())
            #         pass
            #     else:
            #         # stock=Stock(name=row['Name'], Name=row['Name'], SSN=row['SSN'], Class=row['Class'],
            #         #             DNUSAN=row['DNUSAN'], Shortdesc=row['Short description'],Category=row['Category'],Subcategory=row['Subcategory'],Manufacturer=row['Manufacturer'],
            #         #             Model=row['Model'],Status=row['Status(hardware_status)'],Substatus=row['Substatus'],Program=row['Program'],Project=row['Project'],
            #         #             PONo=row['PO number'],POlineNo=row['PO line number'],Assignto=row['Assigned to'],Ownedby=row['Owned by'],Managedby=row['Managed by'],
            #         #             HomeLoc=row['Home Location'],Location=row['Location'],LocDetails=row['Location Details'],Created=row['Created'],Createdby=row['Created by'],
            #         #             Updated=row['Updated'],Updatedby=row['Updgted by'],Costcent=row['Cost center'],Comments=row['Comments'],
            #         #             FinaType=row['Finance Type'],HardSuppG=row['Hardware Support Group'],HardSuppSer=row['Hardware Support Service'],LotNo=row['Lot Number'],
            #         #             Etag=row['Etag'])
            #         # stock.save()
            #         stock=Stock(name=row['Name'], Name=row['Name'], SSN=row['SSN'], Class=row['Class'],
            #                     Category=row['Category'],Manufacturer=row['Manufacturer'],
            #                     Model=row['Model'],Status=row['Status'],Substatus=row['Substatus'],
            #                     Type=row['Type'])
            #         stock.save()

        # for row in reader:
        #     if Stock.objects.filter(SSN=row['SSN'], name=row['Name'], Name=row['Name']).exists():
        #         # print("count", Stock.objects.filter(SSN=row['Serial number'], name=row['Name'], Name=row['Name']).count())
        #         pass
        #     else:
        #         # stock=Stock(name=row['Name'], Name=row['Name'], SSN=row['SSN'], Class=row['Class'],
        #         #             DNUSAN=row['DNUSAN'], Shortdesc=row['Short description'],Category=row['Category'],Subcategory=row['Subcategory'],Manufacturer=row['Manufacturer'],
        #         #             Model=row['Model'],Status=row['Status(hardware_status)'],Substatus=row['Substatus'],Program=row['Program'],Project=row['Project'],
        #         #             PONo=row['PO number'],POlineNo=row['PO line number'],Assignto=row['Assigned to'],Ownedby=row['Owned by'],Managedby=row['Managed by'],
        #         #             HomeLoc=row['Home Location'],Location=row['Location'],LocDetails=row['Location Details'],Created=row['Created'],Createdby=row['Created by'],
        #         #             Updated=row['Updated'],Updatedby=row['Updgted by'],Costcent=row['Cost center'],Comments=row['Comments'],
        #         #             FinaType=row['Finance Type'],HardSuppG=row['Hardware Support Group'],HardSuppSer=row['Hardware Support Service'],LotNo=row['Lot Number'],
        #         #             Etag=row['Etag'])
        #         # stock.save()
        #         stock=Stock(name=row['Name'], Name=row['Name'], SSN=row['SSN'], Class=row['Class'],
        #                     Category=row['Category'],Manufacturer=row['Manufacturer'],
        #                     Model=row['Model'],Status=row['Status'],Substatus=row['Substatus'],
        #                     Type=row['Type'])
        #         stock.save()

            if Class1.objects.filter(class_name = row['Class']).exists():
                # print("Yes")
                pass
            elif Manufacturer.objects.filter(manufacturer_name = row['Manufacturer'] ).exists():
                # print("Cat exist")
                pass
            else:
                if row['Class']:
                    stock_class=Class1.objects.create(class_name = row['Class'])
                    print('Stock class:', stock_class.class_name)
                    stock_class.save()
                if row['Category']:
                    category = Category.objects.create(category_name = row['Category'], class_name = stock_class )
                    category.save()
                # if row['Subcategory']:
                #     subcategory = Category.objects.create(subcategory_name = row['Subcategory'], category_name = category )
                #     subcategory.save()
                if row['Manufacturer']:
                    manufacturer = Manufacturer.objects.create(manufacturer_name = row['Manufacturer'], class_name=stock_class, subcat_name = category )
                    manufacturer.save()
                if row['Model']:
                    model = Model.objects.create(model_name = row['Model'], class_name=stock_class, subcat_name = category, manufacturer_name = manufacturer )
                    model.save()


                # Stock.objects.create(
                #     field1=row[0],
                #     field2=row[1],
                    
                # )
            
            # return HttpResponseRedirect('upload')  # Redirect to a success page
    else:
        form = CSVUploadForm()
    
    return render(request, 'home/upload.html')


@login_required(login_url="/login/")
def BuildConfig(request):
    context = {'segment': 'index'}
    if request.method =='GET':
        classnames_all = Class1.objects.all()

        all_configs = ConfigName.objects.all()
        print("Class value from select:", request.GET.get('class', None))
        context = {
            'segment': 'buildconfig',
            'allclassnames': classnames_all,
            'all_configs': all_configs

        }
        return render(request, 'home/buildconfig.html', context)
    
    if request.method =='POST':
        classnames_all = Class1.objects.all()
        all_configs = ConfigName.objects.all()
        context = {
            'segment': 'buildconfig',
            'allclassnames': classnames_all,
            'all_configs': all_configs
        }
        
        # For Config list select
        if 'selconfig' in json.loads(request.body):
            print("selconfig value from select:", json.loads(request.body)['selconfig'])

            configs = []
            concontxt = {}

            allclass = []
            allcategory = []
            allmanu = []
            allmodel = []
            allquantity = []

            
            conname = ConfigName.objects.get(id = json.loads(request.body)['selconfig'])
            config3 = Config.objects.filter(name = conname)
            for j in config3:
                # print("j",j.Model)
                allclass.append(j.Class)
                allcategory.append(j.Category)
                allmanu.append(j.Manufacturer)
                allmodel.append(j.Model)
                allquantity.append(j.quantity)
            
            print(allclass,allcategory,allmanu,allmodel,allquantity)
            return JsonResponse({"allclass":allclass, 'allcategory':allcategory, 'allmanu':allmanu, 'allmodel':allmodel,
                                    'allquantity':allquantity})
        

        # Get build data
        if 'buildno' in json.loads(request.body):
            buildcontext = {}
            print("buildno value from select:", json.loads(request.body)['buildno'])

            print("aclass value from select:", json.loads(request.body)['aclass'])
            print("acat value from select:", json.loads(request.body)['acat'])
            print("amanu value from select:", json.loads(request.body)['amanu'])
            print("amodel value from select:", json.loads(request.body)['amodel'])
            print("aqua value from select:", json.loads(request.body)['aqua'])

            configs = []
            concontxt = {}

            allclass = []
            allcategory = []
            allmanu = []
            allmodel = []
            allquantity = []

            row1 = 0
            row2 = 0
            row3 = 0
            row4 = 0
            row5 = 0
            row6 = 0
            rowsval = []
            count = 0
            if len(json.loads(request.body)['aclass']) == len(json.loads(request.body)['acat']):
                for (i,j,k,l) in zip(json.loads(request.body)['aclass'],json.loads(request.body)['acat'],json.loads(request.body)['amanu'],json.loads(request.body)['amodel']):
                    if count == 0:
                        # for i in 
                        # print("Stock count", Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count())
                        # row1.append(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count())
                        row1 = int(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l,Substatus__icontains = "Available").count())
                        rowsval.append(int(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l,Substatus__icontains = "Available").count()))
                        count+=1
                        continue

                    if count == 1:
                        # row2.append(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count())
                        row2 = int(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l,Substatus__icontains = "Available").count())
                        rowsval.append(int(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l,Substatus__icontains = "Available").count()))
                        count+=1
                        continue

                    if count == 2:
                        # row3.append(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count())
                        row3 = int(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l,Substatus__icontains = "Available").count())
                        rowsval.append(int(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l,Substatus__icontains = "Available").count()))
                        count+=1
                        continue

                    if count == 3:
                        # row4.append(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count())
                        row4 = int(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l,Substatus__icontains = "Available").count())
                        rowsval.append(int(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l,Substatus__icontains = "Available").count()))
                        count+=1
                        continue

                    if count == 4:
                        # row5.append(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count())
                        row5 = int(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l,Substatus__icontains = "Available").count())
                        rowsval.append(int(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l,Substatus__icontains = "Available").count()))
                        count+=1
                        continue

                    if count == 5:
                        # row6.append(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count())
                        row6 = int(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l,Substatus__icontains = "Available").count())
                        rowsval.append(int(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l,Substatus__icontains = "Available").count()))
                        continue

                count = 0      
                print("Count", count)
                print("Rows", int(row1), int(row2),int(row3),int(row4),int(row5),int(row6))
                

                nobuild = 0
                if row1:
                    if int(row1) == 0:
                        nobuild = 0
                        buildcontext['rows_val'] = [int(row1)]
                if row1 and row2:
                    if int(row1) == 0 or int(row2) == 0:
                        nobuild = 0
                        buildcontext['rows_val'] = [int(row1),int(row2)]
                if row1 and row2 and row3:
                    if int(row1) == 0 or int(row2) == 0 or int(row3) == 0:
                        print("3rd class:", row1,row2,row3)
                        nobuild = 0
                        buildcontext['rows_val'] = [int(row1),int(row2),int(row3)]
                if row1 and row2 and row3 and row4:
                    if int(row1) == 0 or int(row2) == 0 or int(row3) == 0 or int(row4) == 0:
                        nobuild = 0
                        buildcontext['rows_val'] = [int(row1),int(row2),int(row3),int(row4)]
                if row1 and row2 and row3 and row4 and row5:
                    if int(row1) == 0 or int(row2) == 0 or int(row3) == 0 or int(row4) == 0 or int(row5) == 0:
                        nobuild = 0
                        buildcontext['rows_val'] = [int(row1),int(row2),int(row3),int(row4),int(row5)]
                if row1 and row2 and row4 and row5 and row6:
                    if int(row1) == 0 or int(row2) == 0 or int(row3) == 0 or int(row4) == 0 or int(row5) == 0 or int(row6) == 0:
                        nobuild = 0
                        buildcontext['rows_val'] = [int(row1),int(row2),int(row3),int(row4),int(row5),int(row6)]

                rowsbuilds = []
                print("No of nobuild form zero", nobuild)
                if nobuild != None:
                    if row1:
                        nobuild = int(row1)/int(json.loads(request.body)['aqua'][0])
                        # nobuild = int(row1)
                        # print("Minimum... index", min(int(row1)))
                        buildcontext['rows_val'] = [int(row1)]
                    if row1 and row2:
                        # minindex = min(int(row1),int(row2)).__index__
                        # print("Minimum... index", min(int(row1),int(row2)).__index__())
                        
                        nobuild = min(int(int(row1)/int(int(json.loads(request.body)['aqua'][0]))),int(int(row2)/int(int(json.loads(request.body)['aqua'][1]))))
                        print("Row 1 2",nobuild)
                        buildcontext['rows_val'] = [int(row1),int(row2)]
                    if row1 and row2 and row3:
                        nobuild = min(int(int(row1)/int(int(json.loads(request.body)['aqua'][0]))),int(int(row2)/int(int(json.loads(request.body)['aqua'][1]))),int(int(row3)/int(int(json.loads(request.body)['aqua'][2]))))
                        print("Row 1 2 3",nobuild)
                        buildcontext['rows_val'] = [int(row1),int(row2),int(row3)]
                    if row1 and row2 and row3 and row4:
                        nobuild = min(int(int(row1)/int(int(json.loads(request.body)['aqua'][0]))),int(int(row2)/int(int(json.loads(request.body)['aqua'][1]))),int(int(row3)/int(int(json.loads(request.body)['aqua'][2]))),int(int(row4)/int(int(json.loads(request.body)['aqua'][3]))))
                        buildcontext['rows_val'] = [int(row1),int(row2),int(row3),int(row4)]
                    if row1 and row2 and row3 and row4 and row5:
                        nobuild = min(int(int(row1)/int(int(json.loads(request.body)['aqua'][0]))),int(int(row2)/int(int(json.loads(request.body)['aqua'][1]))),int(int(row3)/int(int(json.loads(request.body)['aqua'][2]))),int(int(row4)/int(int(json.loads(request.body)['aqua'][3]))),int(int(row5)/int(int(json.loads(request.body)['aqua'][4]))))
                        buildcontext['rows_val'] = [int(row1),int(row2),int(row3),int(row4),int(row5)]
                    if row1 and row2 and row4 and row5 and row6:
                        nobuild = min(int(int(row1)/int(int(json.loads(request.body)['aqua'][0]))),int(int(row2)/int(int(json.loads(request.body)['aqua'][1]))),int(int(row3)/int(int(json.loads(request.body)['aqua'][2]))),int(int(row4)/int(int(json.loads(request.body)['aqua'][3]))),int(int(row5)/int(int(json.loads(request.body)['aqua'][4]))),int(int(row6)/int(int(json.loads(request.body)['aqua'][5]))))
                        buildcontext['rows_val'] = [int(row1),int(row2),int(row3),int(row4),int(row5),int(row6)]

                no_of_builds = []
                count1 = 0
                buildcontext['build_status'] = "Red"
                if int(json.loads(request.body)['buildno']) > 0:
                    if len(json.loads(request.body)['aqua']) == 1:
                        print("One")
                        for i in range(len(json.loads(request.body)['aqua'])):
                            if int(row1) >= int(json.loads(request.body)['aqua'][0]):
                                print("Green1")
                                buildcontext['build_status'] = "Green"
                                no_of_builds = [[int(int(row1)/int(json.loads(request.body)['buildno']))]]

                        # if int(row1) >= json.loads(request.body)['aqua'][i]
                        
                    elif len(json.loads(request.body)['aqua']) == 2:
                        print("2")
                        for i in range(len(json.loads(request.body)['aqua'])):
                            if int(row1) >= int(json.loads(request.body)['aqua'][0]) and int(row2) >= int(json.loads(request.body)['aqua'][1]):
                                print("Green2")
                                buildcontext['build_status'] = "Green"
                                no_of_builds = [[int(int(row1)/int(json.loads(request.body)['buildno']))],  [int(row2)/int(json.loads(request.body)['buildno'])]]
                        # if int(row1) >= json.loads(request.body)['aqua'][i]
                    elif len(json.loads(request.body)['aqua']) == 3:
                        print("3")
                        for i in range(len(json.loads(request.body)['aqua'])):
                            if int(row1) >= int(json.loads(request.body)['aqua'][0]) and int(row2) >= int(json.loads(request.body)['aqua'][1]) and int(row3) >= int(json.loads(request.body)['aqua'][2]):
                                print("Green3")
                                buildcontext['build_status'] = "Green"
                                no_of_builds = [[int(int(row1)/int(json.loads(request.body)['buildno']))],  [int(row2)/int(json.loads(request.body)['buildno'])],  [int(row3)/int(json.loads(request.body)['buildno'])]]
                        # if int(row1) >= json.loads(request.body)['aqua'][i]
                    elif len(json.loads(request.body)['aqua']) == 4:
                        print("4")
                        for i in range(len(json.loads(request.body)['aqua'])):
                            if int(row1) >= int(json.loads(request.body)['aqua'][0]) and int(row2) >= int(json.loads(request.body)['aqua'][1]) and int(row3) >= int(json.loads(request.body)['aqua'][2]) and int(row4) >= int(json.loads(request.body)['aqua'][3]):
                                print("Green4")
                                buildcontext['build_status'] = "Green"
                                no_of_builds = int(int(row1)/int(json.loads(request.body)['buildno']) + int(row2)/int(json.loads(request.body)['buildno']) + int(row3)/int(json.loads(request.body)['buildno']) + int(row4)/int(json.loads(request.body)['buildno']))
                        # if int(row1) >= json.loads(request.body)['aqua'][i]
                    elif len(json.loads(request.body)['aqua']) == 5:
                        print("5")
                        for i in range(len(json.loads(request.body)['aqua'])):
                            if int(row1) >= int(json.loads(request.body)['aqua'][0]) and int(row2) >= int(json.loads(request.body)['aqua'][1]) and int(row3) >= int(json.loads(request.body)['aqua'][2]) and int(row4) >= int(json.loads(request.body)['aqua'][3]) and int(row5) >= int(json.loads(request.body)['aqua'][4]):
                                print("Green5")
                                buildcontext['build_status'] = "Green"
                                no_of_builds = int(int(row1)/int(json.loads(request.body)['buildno']) + int(row2)/int(json.loads(request.body)['buildno']) + int(row3)/int(json.loads(request.body)['buildno']) + int(row4)/int(json.loads(request.body)['buildno']) + int(row5)/int(json.loads(request.body)['buildno']))
                        # if int(row1) >= json.loads(request.body)['aqua'][i]
                    elif len(json.loads(request.body)['aqua']) == 6:
                        print("6")
                        for i in range(len(json.loads(request.body)['aqua'])):
                            if int(row1) >= int(json.loads(request.body)['aqua'][0]) and int(row2) >= int(json.loads(request.body)['aqua'][1]) and int(row3) >= int(json.loads(request.body)['aqua'][2]) and int(row4) >= int(json.loads(request.body)['aqua'][3]) and int(row5) >= int(json.loads(request.body)['aqua'][4]) and int(row6) >= int(json.loads(request.body)['aqua'][5]):
                                print("Green6")
                                buildcontext['build_status'] = "Green"
                                no_of_builds = int(int(row1)/int(json.loads(request.body)['buildno']) + int(row2)/int(json.loads(request.body)['buildno']) + int(row3)/int(json.loads(request.body)['buildno']) + int(row4)/int(json.loads(request.body)['buildno']) + int(row5)/int(json.loads(request.body)['buildno']) + int(row6)/int(json.loads(request.body)['buildno']))
                
                
                if int(json.loads(request.body)['buildno']) > 0:
                    if int(nobuild):
                        # if int(nobuild) == int(json.loads(request.body)['buildno']):
                        #     buildcontext['min_build'] = int(nobuild)
                        #     buildcontext['build_status'] = "Green"
                        if int(json.loads(request.body)['buildno']) > int(nobuild):
                            print("No.of.build", int(int(json.loads(request.body)['buildno'])/int(int(nobuild))))
                            if int(json.loads(request.body)['buildno']) > int(int(json.loads(request.body)['buildno'])/int(int(nobuild))):
                                buildcontext['no_build'] = int(nobuild)
                                buildcontext['build_status'] = "Red"
                            else:
                                buildcontext['no_build'] = int(nobuild)
                                buildcontext['build_status'] = "Green"
                        
                        # elif int(json.loads(request.body)['buildno']) < int(nobuild):
                        #     print("No.of.build < than", int(int(int(nobuild)))/int(json.loads(request.body)['buildno']))
                        #     if int(json.loads(request.body)['buildno']) > int(int(int(nobuild)))/int(json.loads(request.body)['buildno']):
                        #         buildcontext['no_build'] = int(nobuild)
                        #         buildcontext['build_status'] = "Red"
                        #     else:
                        #         buildcontext['no_build'] = int(nobuild)
                        #         buildcontext['build_status'] = "Green"
                        # else:
                        #     buildcontext['build_status'] = "Red"

                    else:
                        buildcontext['build_status'] = "Red"
                
                
                # if len(json.loads(request.body)['aqua']) > 1:
                #     if len(no_of_builds) == 0:
                #         buildcontext['build_status'] = "Red"
                    
                #     if no_of_builds != None:
                #         if len(no_of_builds) > 0:
                #             for i in no_of_builds:
                #                 if i == 0:
                #                     buildcontext['build_status'] = "Red"
                
                buildcontext['rowval'] = rowsval
                buildcontext['nobuild'] = int(nobuild)
                print("nobuild", int(nobuild))
                
                # print("Min val:", int(min(no_of_builds)[0]))
                print("build val:", int(json.loads(request.body)['buildno']))
                buildcontext['userbldval'] = int(json.loads(request.body)['buildno'])
                
                # min_build = []
                # if int(json.loads(request.body)['buildno']) > 0:
                #     if int(nobuild) > int(json.loads(request.body)['buildno']):
                #         if len(json.loads(request.body)['aqua']) >= 0:
                #             for i in json.loads(request.body)['aqua']:
                #                 # print("i",int(i))
                #                 # print("buildno", int(json.loads(request.body)['buildno']))
                #                 d = int(i)*int(json.loads(request.body)['buildno'])
                #                 # print("d",d)
                #                 # print("nobuild",int(nobuild/d))
                #                 # print("no build", int(nobuild)/int(d))
                #                 min_build.append(int(int(nobuild)/d))
                #                 # print("Minval",int(nobuild) / int(i)*int(json.loads(request.body)['buildno']))
                #                 # buildcontext['no_build'] = int(int(nobuild) / int(i)*int(json.loads(request.body)['buildno']))
                #         # buildcontext['no_build'] = int(int(nobuild) / int(json.loads(request.body)['buildno']))
                # # print("Min_build", min(min_build))

                
                # if min_build:
                #     buildcontext['min_build'] = min(min_build)
                #     if min(min_build) == 0:
                #         buildcontext['build_status'] = "Red"
                # else:
                #     buildcontext['min_build'] = 0
                #     print("nobuild", nobuild)


                # print("Rows val:", buildcontext['rows_val'], rowsval)
                print("Rows val:", rowsval)
                ask_val = []
                if len(json.loads(request.body)['aqua']) >= 0:
                    for i in json.loads(request.body)['aqua']:
                        ask_val.append(int(i)*int(json.loads(request.body)['buildno']))
                
                if int(json.loads(request.body)['buildno']) == 0:
                    buildcontext['build_status'] = "zero"

                buildcontext['ask_val'] = ask_val
                print("Context", buildcontext['build_status'], "No of builds:", type(no_of_builds))

                # print("Min Min", min(eval(i) for i in json.loads(request.body)['aqua']))
                buildcontext['can_build'] = int(int(nobuild)/int(min(eval(i) for i in json.loads(request.body)['aqua'])))

                print("Context", buildcontext)
                return JsonResponse(buildcontext)
                
        
        if 'reserve2' in json.loads(request.body):
            buildcontext = {"reserve":"reserve"}
            print("buildno reserve value from select:", json.loads(request.body)['bno'])
            print("aqua reserve value from select:", json.loads(request.body)['aqua'])
            
            configs = []
            concontxt = {}

            allclass = []
            allcategory = []
            allmanu = []
            allmodel = []
            allquantity = []

            row1 = ''
            row2 = ''
            row3 = ''
            row4 = ''
            row5 = ''
            row6 = ''

            count = 0
            if len(json.loads(request.body)['aclass']) == len(json.loads(request.body)['acat']):
                for (i,j,k,l) in zip(json.loads(request.body)['aclass'],json.loads(request.body)['acat'],json.loads(request.body)['amanu'],json.loads(request.body)['amodel']):
                    if count == 0:
                        # for i in 
                        print("Stock count", Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l , Substatus__icontains = "Available").count())
                        # print("Countloop", int(json.loads(request.body)['bno'])*int(json.loads(request.body)['aqua'][0]))
                        row1=(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l, Substatus__icontains = "Available").count())
                        # row1 = Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l)[:int(json.loads(request.body)['bno'])].update(Substatus = "Reserved")
                        stoks = Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l, Substatus__icontains = "Available")[:int(int(json.loads(request.body)['bno'])*int(json.loads(request.body)['aqua'][0]))]
                        # for i in range(int(json.loads(request.body)['bno'])):
                        #     # stoks[i].Substatus = "Reserved"
                        #     stoks[i].update(Substatus = "Reserved")
                        for i in stoks:
                            i.Substatus = "Reserved"
                            i.Reservedby = str(request.user)
                            i.Configname = ConfigName.objects.get(id = json.loads(request.body)['reserve2']).name
                            # i.Configname = json.loads(request.body)['reserve2']
                            i.save()
                            
                        
                        count+=1
                        continue

                    if count == 1:
                        row2=(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count())
                        # row2 = Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l)[:int(json.loads(request.body)['bno'])].update(Substatus = "Reserved")
                        stoks = Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l, Substatus__icontains = "Available")[:int(int(json.loads(request.body)['bno'])*int(json.loads(request.body)['aqua'][1]))]
                        # for i in range(int(json.loads(request.body)['bno'])):
                        #     # stoks[i].Substatus = "Reserved"
                        #     stoks[i].update(Substatus = "Reserved")
                        for i in stoks:
                            i.Substatus = "Reserved"
                            i.Reservedby = str(request.user)
                            i.Configname = ConfigName.objects.get(id = json.loads(request.body)['reserve2']).name
                            i.save()
                        count+=1
                        continue

                    if count == 2:
                        row3=(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count())
                        stoks = Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l, Substatus__icontains = "Available")[:int(int(json.loads(request.body)['bno'])*int(json.loads(request.body)['aqua'][2]))]
                        # for i in range(int(json.loads(request.body)['bno'])):
                        #     # stoks[i].Substatus = "Reserved"
                        #     stoks[i].update(Substatus = "Reserved")
                        for i in stoks:
                            i.Substatus = "Reserved"
                            i.Reservedby = str(request.user)
                            i.Configname = ConfigName.objects.get(id = json.loads(request.body)['reserve2']).name
                            i.save()
                        count+=1
                        continue

                    if count == 3:
                        row4=(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count())
                        # row4 = Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l)[:int(json.loads(request.body)['bno'])].update(Substatus = "Reserved")
                        stoks = Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l, Substatus__icontains = "Available")[:int(int(json.loads(request.body)['bno'])*int(json.loads(request.body)['aqua'][3]))]
                        # for i in range(int(json.loads(request.body)['bno'])):
                        #     # stoks[i].Substatus = "Reserved"
                        #     stoks[i].update(Substatus = "Reserved")
                        for i in stoks:
                            i.Substatus = "Reserved"
                            i.Reservedby = str(request.user)
                            i.Configname = ConfigName.objects.get(id = json.loads(request.body)['reserve2']).name
                            i.save()
                        count+=1
                        continue

                    if count == 4:
                        row5=(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count())
                        # row5 = Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l)[:int(json.loads(request.body)['bno'])].update(Substatus = "Reserved")
                        stoks = Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l, Substatus__icontains = "Available")[:int(int(json.loads(request.body)['bno'])*int(json.loads(request.body)['aqua'][4]))]
                        # for i in range(int(json.loads(request.body)['bno'])):
                        #     # stoks[i].Substatus = "Reserved"
                        #     stoks[i].update(Substatus = "Reserved")
                        for i in stoks:
                            i.Substatus = "Reserved"
                            i.Reservedby = str(request.user)
                            i.Configname = ConfigName.objects.get(id = json.loads(request.body)['reserve2']).name
                            i.save()
                        count+=1
                        continue

                    if count == 5:
                        row6=(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count())
                        # row6 = Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l)[:int(json.loads(request.body)['bno'])].update(Substatus = "Reserved")
                        stoks = Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l, Substatus__icontains = "Available")[:int(int(json.loads(request.body)['bno'])*int(json.loads(request.body)['aqua'][5]))]
                        # for i in range(int(json.loads(request.body)['bno'])):
                        #     # stoks[i].Substatus = "Reserved"
                        #     stoks[i].update(Substatus = "Reserved")
                        for i in stoks:
                            i.Substatus = "Reserved"
                            i.Reservedby = str(request.user)
                            i.Configname = ConfigName.objects.get(id = json.loads(request.body)['reserve2']).name
                            i.save()
                        continue

                count = 0      
                print("Count", count)
                print("Rows", row1, row2,row3,row4,row5,row6)
                

                nobuild = ''
                if row1:
                    nobuild = int(row1)
                    buildcontext['rows_val'] = [int(row1)]
                if row1 and row2:
                    nobuild = min(int(row1),int(row2))
                    buildcontext['rows_val'] = [int(row1),int(row2)]
                if row1 and row2 and row3:
                    nobuild = min(int(row1),int(row2),int(row3))
                    buildcontext['rows_val'] = [int(row1),int(row2),int(row3)]
                if row1 and row2 and row3 and row4:
                    nobuild = min(int(row1),int(row2),int(row3),int(row4))
                    buildcontext['rows_val'] = [int(row1),int(row2),int(row3),int(row4)]
                if row1 and row2 and row3 and row4 and row5:
                    nobuild = min(int(row1),int(row2),int(row3),int(row4),int(row5))
                    buildcontext['rows_val'] = [int(row1),int(row2),int(row3),int(row4),int(row5)]
                if row1 and row2 and row4 and row5 and row6:
                    nobuild = min(int(row1),int(row2),int(row3),int(row4),int(row5),int(row6))
                    buildcontext['rows_val'] = [int(row1),int(row2),int(row3),int(row4),int(row5),int(row6)]
                

                no_of_builds = []
                count1 = 0
                buildcontext['build_status'] = "Red"
                if int(json.loads(request.body)['bno']) > 0:
                    if len(json.loads(request.body)['aqua']) == 1:
                        print("One")
                        for i in range(len(json.loads(request.body)['aqua'])):
                            if int(row1) >= int(json.loads(request.body)['aqua'][0]):
                                print("Green1")
                                buildcontext['build_status'] = "Green"
                                no_of_builds = int(row1)/int(json.loads(request.body)['bno'])

                        # if int(row1) >= json.loads(request.body)['aqua'][i]
                        
                    elif len(json.loads(request.body)['aqua']) == 2:
                        print("2")
                        for i in range(len(json.loads(request.body)['aqua'])):
                            if int(row1) >= int(json.loads(request.body)['aqua'][0]) and int(row2) >= int(json.loads(request.body)['aqua'][1]):
                                print("Green2")
                                buildcontext['build_status'] = "Green"
                                no_of_builds = int(row1)/int(json.loads(request.body)['bno']) + int(row2)/int(json.loads(request.body)['bno'])
                        # if int(row1) >= json.loads(request.body)['aqua'][i]
                    elif len(json.loads(request.body)['aqua']) == 3:
                        print("3")
                        for i in range(len(json.loads(request.body)['aqua'])):
                            if int(row1) >= int(json.loads(request.body)['aqua'][0]) and int(row2) >= int(json.loads(request.body)['aqua'][1]) and int(row3) >= int(json.loads(request.body)['aqua'][2]):
                                print("Green3")
                                buildcontext['build_status'] = "Green"
                                no_of_builds = [[int(row1)/int(json.loads(request.body)['bno'])],  [int(row2)/int(json.loads(request.body)['bno'])],  [int(row3)/int(json.loads(request.body)['bno'])]]
                        # if int(row1) >= json.loads(request.body)['aqua'][i]
                    elif len(json.loads(request.body)['aqua']) == 4:
                        print("4")
                        for i in range(len(json.loads(request.body)['aqua'])):
                            if int(row1) >= int(json.loads(request.body)['aqua'][0]) and int(row2) >= int(json.loads(request.body)['aqua'][1]) and int(row3) >= int(json.loads(request.body)['aqua'][2]) and int(row4) >= int(json.loads(request.body)['aqua'][3]):
                                print("Green4")
                                buildcontext['build_status'] = "Green"
                                no_of_builds = int(row1)/int(json.loads(request.body)['bno']) + int(row2)/int(json.loads(request.body)['bno']) + int(row3)/int(json.loads(request.body)['bno']) + int(row4)/int(json.loads(request.body)['bno'])
                        # if int(row1) >= json.loads(request.body)['aqua'][i]
                    elif len(json.loads(request.body)['aqua']) == 5:
                        print("5")
                        for i in range(len(json.loads(request.body)['aqua'])):
                            if int(row1) >= int(json.loads(request.body)['aqua'][0]) and int(row2) >= int(json.loads(request.body)['aqua'][1]) and int(row3) >= int(json.loads(request.body)['aqua'][2]) and int(row4) >= int(json.loads(request.body)['aqua'][3]) and int(row5) >= int(json.loads(request.body)['aqua'][4]):
                                print("Green5")
                                buildcontext['build_status'] = "Green"
                                no_of_builds = int(row1)/int(json.loads(request.body)['bno']) + int(row2)/int(json.loads(request.body)['bno']) + int(row3)/int(json.loads(request.body)['bno']) + int(row4)/int(json.loads(request.body)['bno']) + int(row5)/int(json.loads(request.body)['bno'])
                        # if int(row1) >= json.loads(request.body)['aqua'][i]
                    elif len(json.loads(request.body)['aqua']) == 6:
                        print("6")
                        for i in range(len(json.loads(request.body)['aqua'])):
                            if int(row1) >= int(json.loads(request.body)['aqua'][0]) and int(row2) >= int(json.loads(request.body)['aqua'][1]) and int(row3) >= int(json.loads(request.body)['aqua'][2]) and int(row4) >= int(json.loads(request.body)['aqua'][3]) and int(row5) >= int(json.loads(request.body)['aqua'][4]) and int(row6) >= int(json.loads(request.body)['aqua'][5]):
                                print("Green6")
                                buildcontext['build_status'] = "Green"
                                no_of_builds = int(row1)/int(json.loads(request.body)['bno']) + int(row2)/int(json.loads(request.body)['bno']) + int(row3)/int(json.loads(request.body)['bno']) + int(row4)/int(json.loads(request.body)['bno']) + int(row5)/int(json.loads(request.body)['bno']) + int(row6)/int(json.loads(request.body)['bno'])
                
                
                
                if int(json.loads(request.body)['bno']) > 0:
                    if int(nobuild):
                        if int(nobuild) == int(json.loads(request.body)['bno']):
                            buildcontext['no_build'] = int(nobuild)
                            buildcontext['build_status'] = "Green"
                        if int(json.loads(request.body)['bno']) > int(nobuild):
                            print("No.of.build", int(json.loads(request.body)['bno'])/int(int(nobuild)))
                            if int(json.loads(request.body)['bno']) > int(json.loads(request.body)['bno'])/int(int(nobuild)):
                                buildcontext['no_build'] = int(nobuild)
                                buildcontext['build_status'] = "Red"
                            else:
                                buildcontext['no_build'] = int(nobuild)
                                buildcontext['build_status'] = "Green"
                        
                        if int(json.loads(request.body)['bno']) < int(nobuild):
                            print("No.of.build < than", int(int(int(nobuild)))/int(json.loads(request.body)['bno']))
                            if int(json.loads(request.body)['bno']) > int(int(int(nobuild)))/int(json.loads(request.body)['bno']):
                                buildcontext['no_build'] = int(nobuild)
                                buildcontext['build_status'] = "Red"
                            else:
                                buildcontext['no_build'] = int(nobuild)
                                buildcontext['build_status'] = "Green"

                    else:
                        buildcontext['build_status'] = "Red"
                if int(json.loads(request.body)['bno']) == 0:
                    buildcontext['build_status'] = "zero"
                # if len(no_of_builds) == 0:
                #     buildcontext['build_status'] = "Red"
                # if len(no_of_builds) > 0:
                #     for i in no_of_builds:
                #         if int(i) == 0:
                #             buildcontext['build_status'] = "Red"
                print("nobuild", nobuild)

                # print("Min val:", int(min(no_of_builds)[0]))
                print("build val:", int(json.loads(request.body)['bno']))
                buildcontext['ask_val'] = int(json.loads(request.body)['bno'])
                print("Context", buildcontext['build_status'], "No of builds:", no_of_builds)
                return JsonResponse(buildcontext)
        
        return render(request, 'home/buildconfig.html', context)




@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        print(load_template)
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        
        if load_template == 'dashboard.html':
            print("Dashboard template")

            if request.method =='GET':

                # labels = ['Silicon', 'Mass Storage Device', 'Docking Add-on Board', 'Power Supply', 'Test Debug Card', 'Memory', 'Network Gear', 'Cables', 'Net Adapter-Lab']
                data = ['10','4','67','399','49','500','10','61','690']

                assignlab = ['HTHT9439HT0 - Mike', 'HT07HT6236 - vfg', 'HT063638HT - TURNER, GARY P', 'HT2HT74662 - MORGAN, RANDALL']
                assigndata = ['45', '22', '1607','8']

                
                classes1 = []
                for i in Stock.objects.all():
                    # print("Class is:", i.Class)
                    if i.Class == "False":
                        pass
                    else:
                        classes1.append(i.Class)

                print("Classes are:", set(classes1))


                labels = []
                stockval = [] 
                stockin = []
                stockout = []
                stockpending = []
                stockreserved = []

                for i in set(classes1):
                    labels.append(i)
                    # print(f"Stock Available for {i}:", Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Available").count())
                    stockval.append(Stock.objects.filter(Class__icontains = i).count())
                    stockin.append(Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Available").count())
                    stockout.append(Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Not Available").count())
                    stockpending.append(Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Pending Retirement").count())
                    stockreserved.append(Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Reserved").count())

                # for i in set(classes1):
                #     stockout.append(Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Not Available").count())
                # for i in set(classes1):
                #     stockpending.append(Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Pending Retirement").count())
                # for i in set(classes1):
                #     stockreserved.append(Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Reserved").count())
                
                
                
                print("All Stock:",stockval, "Stockin:", stockin, "stockout:", stockout, "stockpending:", stockpending, "stockreserved:", stockreserved)

                model1 = Model.objects.all()
                manufacturer1 = Manufacturer.objects.all()
                context = {
                    'labels'    : labels,
                    'data'      : data,
                    'assignlab' : assignlab,
                    'assigndata' : assigndata,


                    "stockval":stockval,
                    "Stockin": stockin, 
                    "stockout": stockout, 
                    "stockpending": stockpending, 
                    "stockreserved": stockreserved,

                    'segment': 'dashboard',

                    'model1': model1,
                    'manufacturer1': manufacturer1
                    # 'purchases' : purchases
                }
                return render(request, 'home/dashboard.html', context)
            
    
                # html_template = loader.get_template('home/home.html')
                # return HttpResponse(html_template.render(context, request))
            
            if request.method =='POST':
                html_template = loader.get_template('home/dashboard.html')
                return HttpResponse(html_template.render(context, request))
        
        context['segment'] = load_template
        

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
