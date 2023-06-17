from django.urls import include, path
from rest_framework import routers

from api.views import CompanyViewSets
router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSets)


urlpatterns = [
    path('', include(router.urls))
]
