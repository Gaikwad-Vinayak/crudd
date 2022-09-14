"""CRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from core.forms import login
from django.conf.urls.static import static
from django.conf import settings
from core.views import librarymanagement_module_view
from core import views
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'users', librarymanagement_module_view)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.data,name='home'),
    path('listofdata/',views.show,name='listofdata'),
    path('update/<int:pk>/',views.update.as_view(),name='update'),
    path('delete/<int:pk>/delete/',views.delete.as_view(),name='delete'),
    path('accounts/login/',views.login.as_view(authentication_form=login), name='login'),
    path('accounts/logout/',views.logout, name='logout'),
    path('registration/', views.customerregistration.as_view(), name='customerregistration'),
    path('', include(router.urls)),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


