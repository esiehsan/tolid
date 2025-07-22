from django.urls import path
from .views import homePageView, employeeListView, partListView, create_part



urlpatterns = [
    path('', homePageView, name='home'),
    path('employeelist/', employeeListView, name='employees'),
    path('parts/', partListView, name='parts'),
    path('create-part/', create_part, name='create_part'),
]