from django.core.mail import EmailMessage

from .managers import MailingManager
from .models import Mailing, Client, Message
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,

    DeleteView)

from rest_framework.generics import ListAPIView
from django.urls import reverse_lazy
from .forms import MailingForm

from django.conf import settings

from django.http import HttpResponse
from django.views.generic.edit import FormView

from .tasks import send_mail_func

from .serializers import Mailing_serializer

class MailingListView(ListView):
    template_name = 'Message/mailing-list.html'
    paginate_by = 3
    ordering = 'id'
    context_object_name = 'mailing'
    model = Mailing

class MailingByKeyWord(ListView):
    template_name = 'Message/by-kword.html'

    context_object_name = 'mailing'

    def get_queryset(self):
        # recoge lo que está mandando
        kword = self.kwargs['nname']
        lista = Mailing.objects.filter(
            message_text__icontains=kword

        )
        return lista

class AddMailing(CreateView):
    template_name = 'Message/add_mailing.html'
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('Mailing_app:mailing-list')

    def form_valid(self, form):
        mailing = form.save(commit=False)
        mailing.save()
        return super(AddMailing, self).form_valid(form)



class SendCond(UpdateView):
    model = Mailing
    template_name = "Message/send_message_cond.html"
    form_class = MailingForm
    success_url = reverse_lazy('Mailing_app:mailing-list')
    context_object_name = 'mailing'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


    def form_valid(self,form):
        subject = str(form.cleaned_data['subject'])
        body = str(form.cleaned_data['message_text'])
        cc=form.cleaned_data['client_filter']
        print(cc.keys())

        if 'email' in cc.keys():
            #We get a list of email addresses from line
            email=cc['email']
            #print("emails from line", email)

            #here are
            client_emails = Client.objects.filter(
                    email__in=email).values_list('email', flat=True)
            send_to=list(client_emails)
            #print(f"clients emails: {send_to}")

            for message in email:
                if message in send_to:
                    mail = EmailMessage(subject, body, settings.DEFAULT_FROM_EMAIL, send_to, )
                    mail.send(fail_silently=False)
                    self.create_message_instance(message)
                    print(f"Message sent to {message}")
                else:
                    print(f"No Client with  this email {message}:")


        else:
            print("This mailing doesn't contain any mails")

        mailing = form.save(commit=False)
        mailing.save()
        return super(SendCond,self).form_valid(form)

    def create_message_instance(self,e):
            e_client_idd = int(Client.objects.filter(
            email__iexact=e).values_list('id', flat=True)[0])
            mailing_idd = int(self.kwargs['pk'])
            new_message = \
                Message(mailing_id=mailing_idd, sent=True, client_id=e_client_idd, )

            return new_message.save()

class ListSentMessages(ListView):
    template_name = 'Message/sent-messages.html'
    context_object_name = 'messages'
    model = Message
    paginate_by = 3

    def get_queryset(self):
        all_messages = Message.objects.filter(sent__exact=True)
        a = all_messages.count()
        print(a)
        return all_messages



#look here to improve the code
# https://docs.djangoproject.com/en/4.1/ref/models/instances/

class AllMailingAPIView(ListAPIView):
    serializer_class = Mailing_serializer

    def get_queryset(self):
        llist = list(Mailing.objects.all())

        a=Mailing.objects.values_list('subject', flat=True).get(pk=1)
        print(type(a))
        print(a)

        # for i in llist:
        #     print(i.message_text)
        return llist



class TestMailingListView(ListView):

    context_object_name = 'mailing'
    template_name = 'Message/testmailing.html'
    model = Mailing

    def get_queryset(self):

        return Mailing.objects.list_message_texts()

