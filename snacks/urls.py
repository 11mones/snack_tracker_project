from django.contrib import admin
from django.urls import path
from .views import SnacksListView,SnackDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',SnacksListView.as_view(), name='things'),
    path('<pk>/',SnackDetailsView.as_view(), name='thing_details')
]
