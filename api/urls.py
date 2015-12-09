from django.conf.urls import include, url

#Django Rest Framework
from rest_framework import routers
from fuelup.api import views
from rest_framework.urlpatterns import format_suffix_patterns

#REST API routes
router = routers.DefaultRouter()
# router.register(r'fillups', views.FillupViewSet)
# router.register(r'vehicles', views.VehicleViewSet)
# router.register(r'users', views.UserViewSet)

#REST API
urlpatterns = [
    url(r'^', include(router.urls)),

    #class-based view approach
    #url(r'^$', views.api_root), #needed if you use all class-based views and want them to show up in the landing page for the browsable api
    url(r'^session/', views.Session.as_view()),
    url(r'^fillups/$', views.FillupList.as_view(), name='fillup-list'),
    url(r'^fillups/(?P<pk>[0-9]+)/$', views.FillupDetail.as_view(), name='fillup-detail'),
    url(r'^vehicles/$', views.VehicleList.as_view(), name='vehicle-list'),
    # url(r'^vehicles/(?P<pk>[0-9]+)/$', views.VehicleDetail.as_view(), name='vehicle-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
]