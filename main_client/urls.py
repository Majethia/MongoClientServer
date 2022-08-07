from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('get_all_databases/', views.mongo_get_databases),
    path('get_all_collections/', views.mongo_get_collections),
    path('get_all_indexes/', views.mongo_get_all),
    path('edit/', views.edit_doc),
    path('add_doc/', views.add_doc),
    path('delete_doc/', views.delete_doc)

]
