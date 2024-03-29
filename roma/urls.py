"""roma URL Configuration

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
from django.urls    import path
from roma.views     import roma, csv_write, user_guide, latex_code

#from django.conf                import settings
#from django.conf.urls.static    import static


urlpatterns = [
    path('', roma, name='index'),
    path('user_guide/', user_guide, name='user_guide'),
    path('csv-write/', csv_write, name = 'csv_write'),
    path('latex_code/', latex_code, name = 'latex_code'),
]

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
