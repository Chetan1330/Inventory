from django.shortcuts import render
from django.views.generic import View, TemplateView
from inventory.models import Stock
from transactions.models import SaleBill, PurchaseBill


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

class HomeView(View):
    template_name = "home.html"
    def get(self, request):
        labels = ['Silicon', 'Mass Storage Device', 'Docking Add-on Board', 'Power Supply', 'Test Debug Card', 'Memory', 'Network Gear', 'Cables', 'Net Adapter-Lab']
        data = ['10','4','67','399','49','500','10','61','690']

        assignlab = ['HTHT9439HT0 - Mike', 'HT07HT6236 - vfg', 'HT063638HT - TURNER, GARY P', 'HT2HT74662 - MORGAN, RANDALL']
        assigndata = ['45', '22', '1607','8']
        # stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
        # for item in stockqueryset:
        #     labels.append(item.name)
        #     data.append(item.quantity)
        # sales = SaleBill.objects.order_by('-time')[:3]
        # purchases = PurchaseBill.objects.order_by('-time')[:3]
        context = {
            'labels'    : labels,
            'data'      : data,
            'assignlab' : assignlab,
            'assigndata' : assigndata,
            # 'sales'     : sales,
            # 'purchases' : purchases
        }
        return render(request, self.template_name, context)

class AboutView(TemplateView):
    template_name = "about.html"