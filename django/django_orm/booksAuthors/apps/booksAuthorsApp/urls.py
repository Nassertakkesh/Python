from django.conf.urls import url

from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^reset$', views.reset),
    url(r'^add_authors$', views.add_authors),
    url(r'^add_books$', views.add_books),
    url(r'^books$', views.books),
    url(r'^authors$', views.authors),
    url(r'^books/addingauthor$', views.addingauthor),
    url(r'^authors/addingbook$', views.addingbook),
    url(r'^authors/(?P<authid>\d+)$', views.authors_page), 
    url(r'^books/(?P<bookid>\d+)$', views.book_page),
      

]