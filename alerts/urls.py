from django.urls import path
from . import views

urlpatterns = [
    path('alerts/', views.get_all_alerts, name="get_all_alerts"),
    path('alert/<int:pk>/', views.get_alert, name="get_alert"),
    path('create_alert/', views.create_alert, name="create_alert"),
    path('update_alert/<int:pk>/', views.update_alert, name="update_alert"),
    path('delete_alert/<int:pk>/', views.delete_alert, name="delete_alert"),


    path('get_cyrptocurrency_names/', views.get_cyrptocurrency_names, name="get_cyrptocurrency_names"),
    path('get_crypto_data/<str:name>', views.get_crypto_data, name="get_crypto_data"),
]