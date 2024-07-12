from django.urls import path,include
from clientApp.views import *
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'client',clientViewset)
router.register(r'project',projectViewset)
router.register(r'user',userUserviewset)
urlpatterns = [
    path('',include(router.urls))
]

