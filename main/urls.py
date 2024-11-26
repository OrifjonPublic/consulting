from django.urls import path
from . import views as v

app_name = 'main'

urlpatterns = [
    path('', v.HomeView.as_view(), name='home'),
    path('detail/<int:id>/', v.Detail.as_view(), name='detail')
]
