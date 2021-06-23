from django.urls import path, include
from rest_framework import routers
from api.views import SuperMarketViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'market', SuperMarketViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 