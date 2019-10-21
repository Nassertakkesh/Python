from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^logout$', views.logout),
    url(r'^login$', views.login),
    url(r'^book$', views.presuccess),
    url(r'^addbook$', views.addbook),
    url(r'^addbook$', views.addbook),
]






        #   <div class="control-group">
        #         <!-- Birth Date -->
        #         <label class="control-label"  for="birth_date">Birthdate</label>
        #         <div class="controls">
        #           <input type="date" id="birth_date" name="birth_date" placeholder="" class="input-xlarge">
        #         </div>
        #       </div>
       