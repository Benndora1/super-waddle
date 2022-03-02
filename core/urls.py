from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static                      # used for static files

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('', include('apps.homepage.urls')),
    path('inventory/', include('apps.inventory.urls')),
    path('transactions/', include('apps.transactions.urls')),
]

admin.site.site_title = "Inventory Admin Page"