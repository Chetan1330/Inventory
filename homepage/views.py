from django.shortcuts import render
from django.views.generic import View, TemplateView
from inventory.models import Stock, Class1, Category, Subcategory, Manufacturer, Model, Config, ConfigName
from transactions.models import SaleBill, PurchaseBill
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse, HttpResponse
from django.core import serializers

# print(f"Stock Available for:", Stock.objects.filter(Class__icontains = "Memory").count())

# print("Stock Available:", Stock.objects.filter(Class__icontains = "Test Debug Card", Substatus__icontains = "Available").count())
# print("Stock Not Available:", Stock.objects.filter(Substatus__icontains = "Not Available").count())
# print("Stock Pending Retirement:", Stock.objects.filter(Substatus__icontains = "Pending Retirement").count())
# print("Stock Reserved:", Stock.objects.filter(Class__icontains = "Test Debug Card", Substatus__icontains = "Reserved").count())


# classes = []
# for i in Stock.objects.all():
#     # print("Class is:", i.Class)
#     if i.Class == "False":
#         pass
#     else:
#         classes.append(i.Class)

# print("Classes are:", set(classes))

# stockin = []
# stockout = []
# stockpending = []
# stockreserved = []

# for i in set(classes):
#     # print(f"Stock Available for {i}:", Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Available").count())
#     stockin.append(Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Available").count())
#     stockout.append(Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Not Available").count())
#     stockpending.append(Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Pending Retirement").count())
#     stockreserved.append(Stock.objects.filter(Class__icontains = i, Substatus__icontains = "Reserved").count())

# print("Stockin:", stockin, "stockout:", stockout, "stockpending:", stockpending, "stockreserved:", stockreserved)

# for i in Stock.objects.filter(Substatus = "Not Available"):
#     print("Class is:", i)
    # if i.Class == "False":
    #     pass
    # else:
    #     classes.append(i.Class)
    #     Name.append(i.Name)
    #     SNo.append(i.SSN)
    #     Dnusan.append(i.DNUSAN)
    #     category.append(i.Category)


# Class1.objects.all().delete()
# Category.objects.all().delete()
# Subcategory.objects.all().delete()
# Manufacturer.objects.all().delete()
# Model.objects.all().delete()
# classes = []
# Name = []
# SNo = []
# Dnusan = []
# category = []
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

# print("Classes are:", set(classes))
# print("Lenghts are:", len(Name),len(SNo),len(Dnusan),len(classes),len(category))
# stoclass = Class1.objects.all().get(class_name = "Test Debug Card")
# stocat = stoclass.Categories.all()
# # manu = stocat.manufacturer.all()
# for i in stocat:
    
#     data1 = i.manufacturer.all()
#     for j in data1:
#         print("Yes", j)


# class HomeView(View):
#     template_name = "home.html"
#     def get(self, request):        
#         labels = []
#         data = []        
#         stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
#         for item in stockqueryset:
#             labels.append(item.name)
#             data.append(item.quantity)
#         sales = SaleBill.objects.order_by('-time')[:3]
#         purchases = PurchaseBill.objects.order_by('-time')[:3]
#         context = {
#             'labels'    : labels,
#             'data'      : data,
#             'sales'     : sales,
#             'purchases' : purchases
#         }
#         return render(request, self.template_name, context)

# class HomeView(View):
#     template_name = "home.html"
#     def get(self, request):
#         labels = ['Silicon', 'Mass Storage Device', 'Docking Add-on Board', 'Power Supply', 'Test Debug Card', 'Memory', 'Network Gear', 'Cables', 'Net Adapter-Lab']
#         data = ['10','4','67','399','49','500','10','61','690']

#         assignlab = ['HTHT9439HT0 - Mike', 'HT07HT6236 - vfg', 'HT063638HT - TURNER, GARY P', 'HT2HT74662 - MORGAN, RANDALL']
#         assigndata = ['45', '22', '1607','8']

#         classes = []
#         Name = []
#         SNo = []
#         Dnusan = []
#         category = []
#         for i in Stock.objects.all():
#             # print("Class is:", i.Class)
#             if i.Class == "False":
#                 pass
#             else:
#                 classes.append(i.Class)
#                 Name.append(i.Name)
#                 SNo.append(i.SSN)
#                 Dnusan.append(i.DNUSAN)
#                 category.append(i.Category)
                
#         # stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
#         # for item in stockqueryset:
#         #     labels.append(item.name)
#         #     data.append(item.quantity)
#         # sales = SaleBill.objects.order_by('-time')[:3]
#         # purchases = PurchaseBill.objects.order_by('-time')[:3]
#         context = {
#             'labels'    : labels,
#             'data'      : data,
#             'assignlab' : assignlab,
#             'assigndata' : assigndata,

#             'classes': classes,
#             'Name' : Name,
#             'SNo' : SNo,
#             'Dnusan' : Dnusan,
#             'category'     : category,
#             # 'purchases' : purchases
#         }
#         return render(request, self.template_name, context)

class HomeView(View):
    template_name = "home.html"
    def get(self, request):
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
        for i in Stock.objects.all():
            # print("Class is:", i.Class)
            if i.Class == "False":
                pass
            else:
                classes.append(i.Class)
                Name.append(i.Name)
                SNo.append(i.SSN)
                Dnusan.append(i.DNUSAN)
                category.append(i.Category)

                manufacturer.append(i.Manufacturer)
                model.append(i.Model)
                hardware_status.append(i.Status)
                Substatus.append(i.Substatus)
                Program.append(i.Program)
                Project.append(i.Project)
                PO_No.append(i.PONo)
                PO_lineNo.append(i.POlineNo)
                Assignto.append(i.Assignto)
                Ownedby.append(i.Ownedby)

                Managedby.append(i.Managedby)
                HomeLoc.append(i.HomeLoc)
                Location.append(i.Location)
                LocDetail.append(i.LocDetails)
                Created.append(i.Created)
                Createdby.append(i.Createdby)

                Updated.append(i.Updated)
                Updatedby.append(i.Updatedby)
                Costcenter.append(i.Costcent)
                Comments.append(i.Comments)
                FinType.append(i.FinaType)
                HardSupp.append(i.HardSuppG)
                HardSuppService.append(i.HardSuppSer)
                Etag.append(i.Etag)
        
        alldata = []
        for i in range(len(classes)):
            alldata.append([i+1, Name[i], SNo[i], Dnusan[i], classes[i], category[i],
                            manufacturer[i], model[i], hardware_status[i], Substatus[i], Program[i],
                            Project[i], PO_No[i], PO_lineNo[i], Assignto[i], Ownedby[i],
                            Managedby[i], HomeLoc[i], Location[i], LocDetail[i], Created[i],
                            Createdby[i], Updated[i], Updatedby[i], Costcenter[i], Comments[i],
                            FinType[i], HardSupp[i], HardSuppService[i], Etag[i]])
                
        # stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
        # for item in stockqueryset:
        #     labels.append(item.name)
        #     data.append(item.quantity)
        # sales = SaleBill.objects.order_by('-time')[:3]
        # purchases = PurchaseBill.objects.order_by('-time')[:3]


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

            'alldata' : alldata,

            "stockval":stockval,
            "Stockin": stockin, 
            "stockout": stockout, 
            "stockpending": stockpending, 
            "stockreserved": stockreserved,

            'segment': 'home',

            'model1': model1,
            'manufacturer1': manufacturer1
            # 'purchases' : purchases
        }
        return render(request, self.template_name, context)

# Config.objects.all().delete()
# ConfigName.objects.all().delete()
confignames = []
for i in ConfigName.objects.all():
    print("Config data:", i.id)
    # cobj = Config.objects.all().get(name = i)
    # for i in cobj:

    #     print("Cobj:",i)
    confignames.append(i.name)

conname = ConfigName.objects.get(id = 1)
config3 = Config.objects.filter(name = conname)
for i in config3:
    print("i",i.Model)
# print(conname,config3)


# for i in confignames:
#     for j in Config.objects.all():
#         print(i)
#         print(j.name.name)
#         # if  i == j.name:
#         #     print(j.Class)
#         #     print(j.Model)


class CreateConfigView(View):
    template_name = "createconfig.html"

    classnames_all = Class1.objects.all()
    # all_configs = Config.objects.all()
    # for i in all_configs:
    #     print("All config:", i.name)


    
    # configs = []
    # concontxt = {}
    # for i in all_configs:
    #     concontxt = {}
    #     # print("All config:", i.id)
    #     concontxt['Configname'] = i.name
    #     conname = ConfigName.objects.get(id = i.id)
    #     config3 = Config.objects.filter(name = conname)
    #     for j in config3:
    #         # print("j",j.Model)
    #         concontxt['class'] = j.Class
    #         concontxt['category'] = j.Category
    #         concontxt['manufacturer'] = j.Manufacturer
    #         concontxt['model'] = j.Model
    #         concontxt['quantity'] = j.quantity
    #     configs.append(concontxt)
    # print("Config:", configs)
    # print("Config:", configs[0]['category'])

    # classes = []
    # for i in Class1.objects.all():
    #     # print("Class is:", i.Class)
    #     if i.Class == "False":
    #         pass
    #     else:
    #         classes.append(i.Class)

    # print("Classes are:", set(classes))
    
    def get(self, request):
        all_configs = ConfigName.objects.all()
        print("Class value from select:", request.GET.get('class', None))
        context = {
            'segment': 'createconfig',
            'allclassnames': self.classnames_all,
            'all_configs': all_configs

        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        all_configs = ConfigName.objects.all()
        context = {
            'segment': 'createconfig',
            'allclassnames': self.classnames_all,
            'all_configs': all_configs
        }

        

        # config_name = request.POST.get('configname')
        # Selclass1 = request.POST.get('selclass1')
        # Selclass2 = request.POST.get('selclass2')
        # Selclass3 = request.POST.get('selclass3')
        # Selclass4 = request.POST.get('selclass4')
        # Selclass5 = request.POST.get('selclass5')
        # Selclass6 = request.POST.get('selclass6')

        # print("Post request",config_name, Selclass1, Selclass2, Selclass3, Selclass4, Selclass5, Selclass6)
        if request.POST.get('configname'):
            if ConfigName.objects.filter(name = request.POST.get('configname')):
                print("Config with same name exist")
                exit
            else:
                config_name = ConfigName.objects.create(name = request.POST.get('configname'))
                # config_name.save()
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
            print("Request:", json.loads(request.body))
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
                # return JsonResponse({"cat_list1":instances})
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

                # for i in all_configs:
                #     concontxt = {}
                #     # print("All config:", i.id)
                #     concontxt['Configname'] = i.name
                conname = ConfigName.objects.get(id = json.loads(request.body)['selconfig'])
                config3 = Config.objects.filter(name = conname)
                for j in config3:
                    # print("j",j.Model)
                    allclass.append(j.Class)
                    allcategory.append(j.Category)
                    allmanu.append(j.Manufacturer)
                    allmodel.append(j.Model)
                    allquantity.append(j.quantity)
            #         concontxt['class'] = j.Class
            #         concontxt['category'] = j.Category
            #         concontxt['manufacturer'] = j.Manufacturer
            #         concontxt['model'] = j.Model
            #         concontxt['quantity'] = j.quantity
            #         configs.append(concontxt)
            #         concontxt = {}
            # print("Config:", configs)
            # print("Config:", configs[0]['category'])
            # for i in configs:
            #     print(i['class'])
                print(allclass,allcategory,allmanu,allmodel,allquantity)
                return JsonResponse({"allclass":allclass, 'allcategory':allcategory, 'allmanu':allmanu, 'allmodel':allmodel,
                                     'allquantity':allquantity})

                # conname = Class1.objects.get(id = json.loads(request.body)['class6'])
                # cat_list6 = Category.objects.filter(class_name = conname)
                # instances = serializers.serialize('json', cat_list6)
                # print(conname, cat_list6)
                # context['cat_list6'] = cat_list6
                # # return JsonResponse({"cat_list1":instances})
                # return HttpResponse(instances, content_type='application/json')
        
        return render(request, self.template_name, context)
    


class BuildConfigView(View):
    template_name = "buildconfig.html"

    classnames_all = Class1.objects.all()
    # all_configs = Config.objects.all()
    # for i in all_configs:
    #     print("All config:", i.name)


    
    # configs = []
    # concontxt = {}
    # for i in all_configs:
    #     concontxt = {}
    #     # print("All config:", i.id)
    #     concontxt['Configname'] = i.name
    #     conname = ConfigName.objects.get(id = i.id)
    #     config3 = Config.objects.filter(name = conname)
    #     for j in config3:
    #         # print("j",j.Model)
    #         concontxt['class'] = j.Class
    #         concontxt['category'] = j.Category
    #         concontxt['manufacturer'] = j.Manufacturer
    #         concontxt['model'] = j.Model
    #         concontxt['quantity'] = j.quantity
    #     configs.append(concontxt)
    # print("Config:", configs)
    # print("Config:", configs[0]['category'])

    # classes = []
    # for i in Class1.objects.all():
    #     # print("Class is:", i.Class)
    #     if i.Class == "False":
    #         pass
    #     else:
    #         classes.append(i.Class)

    # print("Classes are:", set(classes))
    
    def get(self, request):
        all_configs = ConfigName.objects.all()
        print("Class value from select:", request.GET.get('class', None))
        context = {
            'segment': 'buildconfig',
            'allclassnames': self.classnames_all,
            'all_configs': all_configs

        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        all_configs = ConfigName.objects.all()
        context = {
            'segment': 'buildconfig',
            'allclassnames': self.classnames_all,
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

            # for i in all_configs:
            #     concontxt = {}
            #     # print("All config:", i.id)
            #     concontxt['Configname'] = i.name
            conname = ConfigName.objects.get(id = json.loads(request.body)['selconfig'])
            config3 = Config.objects.filter(name = conname)
            for j in config3:
                # print("j",j.Model)
                allclass.append(j.Class)
                allcategory.append(j.Category)
                allmanu.append(j.Manufacturer)
                allmodel.append(j.Model)
                allquantity.append(j.quantity)
            #         concontxt['class'] = j.Class
            #         concontxt['category'] = j.Category
            #         concontxt['manufacturer'] = j.Manufacturer
            #         concontxt['model'] = j.Model
            #         concontxt['quantity'] = j.quantity
            #         configs.append(concontxt)
            #         concontxt = {}
            # print("Config:", configs)
            # print("Config:", configs[0]['category'])
            # for i in configs:
            #     print(i['class'])
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
                        # print("Stock count", Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count())
                        # row1.append(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count())
                        row1 = Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count()
                        count+=1
                        continue

                    if count == 1:
                        # row2.append(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count())
                        row2 = Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count()
                        count+=1
                        continue

                    if count == 2:
                        # row3.append(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count())
                        row3 = Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count()
                        count+=1
                        continue

                    if count == 3:
                        # row4.append(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count())
                        row4 = Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count()
                        count+=1
                        continue

                    if count == 4:
                        # row5.append(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count())
                        row5 = Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count()
                        count+=1
                        continue

                    if count == 5:
                        # row6.append(Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count())
                        row6 = Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l).count()
                        continue

                count = 0      
                print("Count", count)
                print("Rows", row1, row2,row3,row4,row5,row6)


                count1 = 0
                
                if len(json.loads(request.body)['aqua']) == 1:
                    print("One")
                    for i in range(len(json.loads(request.body)['aqua'])):
                        if int(row1) >= int(json.loads(request.body)['aqua'][0]):
                            print("Green1")
                            buildcontext['build_status'] = "Green"
                    # if int(row1) >= json.loads(request.body)['aqua'][i]
                    
                if len(json.loads(request.body)['aqua']) == 2:
                    print("2")
                    for i in range(len(json.loads(request.body)['aqua'])):
                        if int(row1) >= int(json.loads(request.body)['aqua'][0]) and int(row2) >= int(json.loads(request.body)['aqua'][1]):
                            print("Green1")
                            buildcontext['build_status'] = "Green"
                    # if int(row1) >= json.loads(request.body)['aqua'][i]
                if len(json.loads(request.body)['aqua']) == 3:
                    print("3")
                    for i in range(len(json.loads(request.body)['aqua'])):
                        if int(row1) >= int(json.loads(request.body)['aqua'][0]) and int(row2) >= int(json.loads(request.body)['aqua'][1]) and int(row3) >= int(json.loads(request.body)['aqua'][2]):
                            print("Green1")
                            buildcontext['build_status'] = "Green"
                    # if int(row1) >= json.loads(request.body)['aqua'][i]
                if len(json.loads(request.body)['aqua']) == 4:
                    print("4")
                    for i in range(len(json.loads(request.body)['aqua'])):
                        if int(row1) >= int(json.loads(request.body)['aqua'][0]) and int(row2) >= int(json.loads(request.body)['aqua'][1]) and int(row3) >= int(json.loads(request.body)['aqua'][2]) and int(row4) >= int(json.loads(request.body)['aqua'][3]):
                            print("Green1")
                            buildcontext['build_status'] = "Green"
                    # if int(row1) >= json.loads(request.body)['aqua'][i]
                if len(json.loads(request.body)['aqua']) == 5:
                    print("5")
                    for i in range(len(json.loads(request.body)['aqua'])):
                        if int(row1) >= int(json.loads(request.body)['aqua'][0]) and int(row2) >= int(json.loads(request.body)['aqua'][1]) and int(row3) >= int(json.loads(request.body)['aqua'][2]) and int(row4) >= int(json.loads(request.body)['aqua'][3]) and int(row5) >= int(json.loads(request.body)['aqua'][4]):
                            print("Green1")
                            buildcontext['build_status'] = "Green"
                    # if int(row1) >= json.loads(request.body)['aqua'][i]
                if len(json.loads(request.body)['aqua']) == 6:
                    print("6")
                    for i in range(len(json.loads(request.body)['aqua'])):
                        if int(row1) >= int(json.loads(request.body)['aqua'][0]) and int(row2) >= int(json.loads(request.body)['aqua'][1]) and int(row3) >= int(json.loads(request.body)['aqua'][2]) and int(row4) >= int(json.loads(request.body)['aqua'][3]) and int(row5) >= int(json.loads(request.body)['aqua'][4]) and int(row6) >= int(json.loads(request.body)['aqua'][5]):
                            print("Green6")
                            buildcontext['build_status'] = "Green"
                else:
                    print("Status Red can't build")
                    buildcontext['build_status'] = "Red"

                return JsonResponse(buildcontext)
                
                    # if int(row1) >= json.loads(request.body)['aqua'][i]

                #    for j in Stock.objects.filter(Class = i, Category = j, Manufacturer = k, Model = l):
                #        print("J", j)
            # for i in all_configs:
            #     concontxt = {}
            #     # print("All config:", i.id)
            #     concontxt['Configname'] = i.name
            # conname = ConfigName.objects.get(id = json.loads(request.body)['buildno'])
            # config3 = Config.objects.filter(name = conname)
            # for j in config3:
            #     # print("j",j.Model)
            #     allclass.append(j.Class)
            #     allcategory.append(j.Category)
            #     allmanu.append(j.Manufacturer)
            #     allmodel.append(j.Model)
            #     allquantity.append(j.quantity)
            # #         concontxt['class'] = j.Class
            # #         concontxt['category'] = j.Category
            # #         concontxt['manufacturer'] = j.Manufacturer
            # #         concontxt['model'] = j.Model
            # #         concontxt['quantity'] = j.quantity
            # #         configs.append(concontxt)
            # #         concontxt = {}
            # # print("Config:", configs)
            # # print("Config:", configs[0]['category'])
            # # for i in configs:
            # #     print(i['class'])
            # print(allclass,allcategory,allmanu,allmodel,allquantity)
            # return JsonResponse({"allclass":allclass, 'allcategory':allcategory, 'allmanu':allmanu, 'allmodel':allmodel,
            #                         'allquantity':allquantity})
        
        return render(request, self.template_name, context)
    

class SelclassView(View):
    template_name = "createconfig.html"

    confignames_all = Class1.objects.all()
    # classes = []
    # for i in Class1.objects.all():
    #     # print("Class is:", i.Class)
    #     if i.Class == "False":
    #         pass
    #     else:
    #         classes.append(i.Class)

    # print("Classes are:", set(classes))
    
    def get(self, request):
        
        print("Class value from select:", request.GET.get('class', None))
        context = {
            'segment': 'createconfig',
            'allconfignames': self.confignames_all

        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        # config_name = request.POST.get('configname')
        # Selclass1 = request.POST.get('selclass1')
        # Selclass2 = request.POST.get('selclass2')
        # Selclass3 = request.POST.get('selclass3')
        # Selclass4 = request.POST.get('selclass4')
        # Selclass5 = request.POST.get('selclass5')
        # Selclass6 = request.POST.get('selclass6')

        # print("Post request",config_name, Selclass1, Selclass2, Selclass3, Selclass4, Selclass5, Selclass6)
        if request.POST.get('configname'):
            context = {
                'segment': 'createconfig'
            }
            return render(request, self.template_name, context)
        
        context = {
            'segment': 'createconfig'
        }
        return render(request, self.template_name, context)


class AboutView(TemplateView):
    template_name = "about.html"