from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createconfig/', views.CreateConfig, name='createconfig'),
    path('buildconfig/', views.BuildConfig, name='buildconfig'),
    path('configscan/', views.ConfigScan, name='configscan'),
    path('upload/', views.UploadFile, name='upload'),

    re_path(r'^.*\.*', views.pages, name='pages'),
    

]




    # <div class="sidebar" data="blue">
    #   <div class="sidebar-wrapper" >
    #     <div class="logo">
    #       <a target="_blank" rel="sponsored noopener noreferrer"
    #          href="#" class="simple-text logo-mini" >
    #         Inventory_Next
    #       </a>
    #       <a 
    #          href="#" class="simple-text logo-normal">
            
    #       </a>
    #     </div>
    #     <!-- style="width: 168px;"style="margin-top: 25px;" -->
    #     <ul class="nav" >
    #     {% if request.user.is_authenticated %}
    #       <li class="{% if 'home' in segment %} active {% endif %}">
    #         <a href="/">
    #           <i class="tim-icons icon-tv-2"></i>
    #           <p>Home</p>
    #         </a>
    #       </li>

    #       <li class="{% if 'dashboard' in segment %} active {% endif %}">
    #         <a href="/dashboard.html">
    #           <i class="tim-icons icon-chart-pie-36"></i>
    #           <p>Dashboard</p>
    #         </a>
    #       </li>

    #       <li class="{% if 'myinv' in segment %} active {% endif %}">
    #         <a href="#">
    #           <i class="tim-icons icon-atom"></i>
    #           <p>My Inventory</p>
    #         </a>
    #       </li>

    #       <li class="{% if 'createconfig' in segment %} active {% endif %}">
    #         <a href="/createconfig/">
    #           <i class="tim-icons icon-single-02"></i>
    #           <p>Create Config</p>
    #         </a>
    #       </li>
    #       <li class="{% if 'buildconfig' in segment %} active {% endif %}">
    #         <a href="/buildconfig/">
    #           <i class="tim-icons icon-bank"></i>
    #           <p>Build Config</p>
    #         </a>
    #       </li>
    #       <li class="{% if 'reports' in segment %} active {% endif %}">
    #         <a href="#">
    #           <i class="tim-icons icon-credit-card"></i>
    #           <p>Reports</p>
    #         </a>
    #       </li>
    #       <li class="{% if 'integrations' in segment %} active {% endif %}">
    #         <a href="#">
    #           <i class="tim-icons icon-link-72"></i>
    #           <p>Integrations</p>
    #         </a>
    #       </li>
    #       <li class="{% if 'integrations' in segment %} active {% endif %}">
    #         <a href="#">
    #           <i class="tim-icons icon-settings"></i>
    #           <p>Tools</p>
    #         </a>
    #       </li>
    #       <h4 style="margin-left: 25px;">Saved reports</h4>
    #       <li class="{% if 'reports' in segment %} active {% endif %}">
    #         <a href="#">
    #           <i class="tim-icons icon-single-copy-04"></i>
    #           <p>Current Month</p>
    #         </a>
    #       </li>
    #       <li class="{% if 'integrations' in segment %} active {% endif %}">
    #         <a href="#">
    #           <i class="tim-icons icon-components"></i>
    #           <p>Last quarter</p>
    #         </a>
    #       </li>
    #       {% else %}
    #       <li class="active">
    #         <a target="_blank" 
    #            >
    #           <i class="tim-icons icon-spaceship"></i>
    #           <p>Login/Register</p>
    #         </a>
    #       </li>   
    #       {% endif %}
                    
    #     </ul>
        
    #   </div>
    # </div>
