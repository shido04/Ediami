from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.base import View
from django.conf import settings
from courses.models import Pricing



# Create your views here.
class PricingView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'payments/pricing.html', context)

class PaymentView(View):
    def get(self, request, slug,*args, **kwargs):
        pricing = get_object_or_404(Pricing, slug=slug)

       

        context={
            'pricing_tier':pricing,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        }
        
        return render(request, 'payments/checkout.html', context)

       