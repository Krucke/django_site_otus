from django.urls import path

from base.views import Home


urlpatterns = [
    path('', Home.as_view())
]