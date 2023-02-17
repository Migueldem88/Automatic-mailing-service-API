from django.urls import path
from . import views


app_name ="Client_app"

urlpatterns = [
    path('',
        views.StartView.as_view(),
        name='start'),
    path('list-all-clients',
        views.ListAllClients.as_view(),
        name='list-all-clients'),
    path('add-Client/',
         views.ClientCreateView.as_view(),
        name='client_add'),
    path('update-client/<pk>/',
         views.ClientUpdView.as_view(),
         name='update-client'),
    path('delete-client/<pk>',
         views.ClientDelView.as_view(),
         name='delete-client'),
    path('client-by-kword/<nname>',
         views.ClientbyKword.as_view(),
         name='client-by-kword'),
]