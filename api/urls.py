from django.conf.urls import include, url

#Django Rest Framework
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from fuelup.api import views

#REST API routes
router = routers.DefaultRouter()
#router.register(r'forumposts', views.ForumpostViewSet) #use this for viewset approach
router.register(r'fillup', views.FillupViewSet)
router.register(r'vehicle', views.VehicleViewSet)
router.register(r'users', views.UserViewSet)

#REST API
urlpatterns = [
    url(r'^', include(router.urls)),

    #class-based view approach
    #url(r'^$', views.api_root), #needed if you use all class-based views and want them to show up in the landing page for the browsable api
    url(r'^fillup/$', views.FillupList.as_view(), name='fillup-list'),
    url(r'^fillup/(?P<pk>[0-9]+)/$', views.FillupDetail.as_view(), name='fillup-detail'),
]