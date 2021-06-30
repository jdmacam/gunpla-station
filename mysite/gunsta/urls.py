from django.urls import path
# URLs for this specific app (homework assignments)

from . import views

urlpatterns = [
    path('', views.index)
]