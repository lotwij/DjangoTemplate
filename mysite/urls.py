"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

###################### ZELF WIJZIGEN/TOEVOEGEN START
from django.conf.urls import include, url
from django.contrib import admin
from myapp import views as views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index')
 #   url(r'^products.html/$', views.products, name='products'),

]

urlpatterns += staticfiles_urlpatterns()

###################### ZELF WIJZIGEN/TOEVOEGEN EIND
