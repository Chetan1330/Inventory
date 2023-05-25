from django.shortcuts import render
from django.views.generic import View, TemplateView
from inventory.models import Stock, Class1, Category, Subcategory, Manufacturer, Model
from transactions.models import SaleBill, PurchaseBill

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
            alldata.append([i, Name[i], SNo[i], Dnusan[i], classes[i], category[i],
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
            "stockreserved": stockreserved
            # 'purchases' : purchases
        }
        return render(request, self.template_name, context)

class AboutView(TemplateView):
    template_name = "about.html"