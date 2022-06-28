from django.contrib import admin
from django.urls import path, include

from DjangoGramm.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('DjangoGramm.urls')),
]

handler404 = pageNotFound