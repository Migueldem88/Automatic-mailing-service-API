from django.urls import path
from . import views


app_name ="Mailing_app"

urlpatterns = [
    path('mailing-list',
    views.MailingListView.as_view(),
    name='mailing-list'),

    path('by-kword/<nname>',
         views.MailingByKeyWord.as_view(),
         name='by-kword'),

    path('add-mailing',
         views.AddMailing.as_view(),
         name='add_mailing'),

    path('send-mail/<pk>/',
         views.SendCond.as_view(),
         name='see-mailing'),
    path('sent-messages',
    views.ListSentMessages.as_view(),
    name='sent-messages'),

    path('listdates/',
         views.AllMailingAPIView.as_view(),
         name="listdates"),
    path('testlist/',
         views.TestMailingListView.as_view(),
         name="testlist"),

    ]