from django.urls import path
from .views import PricingView, PaymentView
app_name="payment"

urlpatterns = [
     path('pricing/', PricingView.as_view(), name="pricing"),
     path('pricing/<slug>/', PaymentView.as_view(), name="payment"),
    
]