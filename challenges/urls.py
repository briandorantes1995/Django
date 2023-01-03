from django.urls import path
from . import views

urlpatterns = [
    path("",views.month_list),
    path("<int:month>",views.monthly_challenge_bynumber),
    path("<str:month>",views.monthly_challenge,name="month_challenge")
]
