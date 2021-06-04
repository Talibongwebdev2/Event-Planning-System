from django.conf.urls import url, include
from django.contrib import admin
from CEList import views 






urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),
    url('admin/', admin.site.urls),    
    url(r'^CEList/cId$', views.custom_view, name='custom_view'),    
    url(r'^CEList/(\d+)/$', views.events_page, name='events_page'),    
    url(r'^CEList/bId$', views.booking_view, name='booking_view'),]
    

