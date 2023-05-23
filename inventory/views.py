from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView, 
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Stock
from .forms import StockForm
from django_filters.views import FilterView
from .filters import StockFilter
from csv import DictReader
import csv

# Stock.objects.all().delete()


# with open('Inventory.csv', mode="r", encoding='latin1') as csv_file:
#     # csv_reader = csv.DictReader(csv_file)
#     for row in csv.DictReader(csv_file):
#         if Stock.objects.filter(SSN=row['Serial number']).exists() or Stock.objects.filter(name=row['Name']).exists() or Stock.objects.filter(Name=row['Name']).exists():
#             print("Yes")
#             # pass
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

# classes = []
# for i in Stock.objects.all():
#     # print("Class is:", i.Class)
#     classes.append(i.Class)

# print("Classes are:", set(classes))

# Assignto = []
# for i in Stock.objects.all():
#     # print("Class is:", i.Class)
#     # if i.Assignto == "HT07HT6236 - vfg":
#     Assignto.append(i.Assignto)

# print("Assigns are:", set(Assignto))

# count = {}

# for word in Assignto:
#     count[word] = count.get(word, 0) + 1
# print('Word Frequency')
# for key in count.keys():
#     print(key, count[key])


# with open('Inventory_data.csv') as file:
#     reader = csv.reader(file)
#     next(reader)  # Advance past the header

#     Stock.objects.all().delete()
#     # Genre.objects.all().delete()

    
    # for row in reader:
    #     print(row)

    #     if 
    #     # genre, _ = Genre.objects.get_or_create(name=row[-1])

    #     stock = Stock(name=row[1],
    #                 SSN=row[2],
    #                 )
    #     stock.save()

class StockListView(FilterView):
    filterset_class = StockFilter
    queryset = Stock.objects.filter(is_deleted=False)
    template_name = 'inventory.html'
    paginate_by = 10


class StockCreateView(SuccessMessageMixin, CreateView):                                 # createview class to add new stock, mixin used to display message
    model = Stock                                                                       # setting 'Stock' model as model
    form_class = StockForm                                                              # setting 'StockForm' form as form
    template_name = "edit_stock.html"                                                   # 'edit_stock.html' used as the template
    success_url = '/inventory'                                                          # redirects to 'inventory' page in the url after submitting the form
    success_message = "Stock has been created successfully"                             # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Stock'
        context["savebtn"] = 'Add to Inventory'
        return context       


class StockUpdateView(SuccessMessageMixin, UpdateView):                                 # updateview class to edit stock, mixin used to display message
    model = Stock                                                                       # setting 'Stock' model as model
    form_class = StockForm                                                              # setting 'StockForm' form as form
    template_name = "edit_stock.html"                                                   # 'edit_stock.html' used as the template
    success_url = '/inventory'                                                          # redirects to 'inventory' page in the url after submitting the form
    success_message = "Stock has been updated successfully"                             # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Stock'
        context["savebtn"] = 'Update Stock'
        context["delbtn"] = 'Delete Stock'
        return context


class StockDeleteView(View):                                                            # view class to delete stock
    template_name = "delete_stock.html"                                                 # 'delete_stock.html' used as the template
    success_message = "Stock has been deleted successfully"                             # displays message when form is submitted
    
    def get(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        return render(request, self.template_name, {'object' : stock})

    def post(self, request, pk):  
        stock = get_object_or_404(Stock, pk=pk)
        stock.is_deleted = True
        stock.save()                                               
        messages.success(request, self.success_message)
        return redirect('inventory')