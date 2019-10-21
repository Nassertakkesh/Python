from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^logout$', views.logout),
    url(r'^login$', views.login),
    url(r'^post$', views.post),
    url(r'^thewall$', views.thewall),
    url(r'^delete$', views.delete),
    url(r'^presuccess$', views.presuccess),
    url(r'^comment$', views.comment),

]