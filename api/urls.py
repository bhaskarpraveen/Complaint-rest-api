from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Shops',views.ShopView)
router.register('Persons',views.PersonView)
router.register('Online',views.OnlineView)

urlpatterns = [
    path('sms',views.test),
    path('send',views.sendmessage),
    path('',include(router.urls))

]