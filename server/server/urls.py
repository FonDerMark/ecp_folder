from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^rest/', include('rest.urls')),
]
