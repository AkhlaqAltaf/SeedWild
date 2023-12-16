
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', include('src.recommendation.urls', namespace='recommendation')),
    path('admin/', admin.site.urls),
]
