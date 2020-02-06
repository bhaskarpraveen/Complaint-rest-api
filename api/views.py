from django.shortcuts import render
from rest_framework import viewsets
from .models import Shop,Person,Online
from .serializers import ShopSerializer,PersonSerializer,OnlineSerializer
from rest_framework.decorators import action
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from complaintApi import settings
from twilio.rest import Client
import requests
# Create your views here.
url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=test&language=english&route=p&numbers=9999999999,888888888"
client =Client(settings.TWILIO_ACCOUNT_SID,settings.TWILIO_AUTH_TOKEN)
class ShopView(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    # @action(detail=True,methods=['GET'])
    # def checking(request):
    #     print(request)

class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
class OnlineView(viewsets.ModelViewSet):
    queryset = Online.objects.all()
    serializer_class = OnlineSerializer

def sendmessage(request):
    message = client.messages.create(
                     body="Welcome ! register your complaint here",
                     from_='+12014855521',
                     to='+918464877285' 
                 )
    return HttpResponse('Message sent')

@csrf_exempt
def test(request):
    print(request)
    print("called")
    return HttpResponse('Done')
