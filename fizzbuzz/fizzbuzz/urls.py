from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from app.views import FizzBuzzViewSet

router = DefaultRouter()
router.register(r'fizzbuzz', FizzBuzzViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^', include(router.urls)),
]
