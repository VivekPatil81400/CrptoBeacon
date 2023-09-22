from django.urls import path
from . import views

urlpatterns = [
    path('alerts/', views.get_all_alerts, name="get_all_alerts"),
    path('alert/<int:pk>/', views.get_alert, name="get_alert"),
    path('create_alert/', views.create_alert, name="create_alert"),
    path('update_alert/<int:pk>/', views.update_alert, name="update_alert"),
    path('delete_alert/<int:pk>/', views.delete_alert, name="delete_alert"),
]

# {
#     "name": "Tether",
#     "low_amount": 0.5,
#     "high_amount": 1.5,
#     "percentage_change": 0.25
# }