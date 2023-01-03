from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january":"This works",
    "february":"Hot milf",
    "march":"Hacer ejercicio",
    "april":"love the turtle",
    "may":"learn to cook",
    "june":"dinosaur birthday",
    "july":"summer",
    "august":"summer yeah",
    "september":"independence day",
    "october":"halloween",
    "november":"revolution",
    "december":"turtle birthday"

}

def monthly_challenge_bynumber(request,month):
    months = list(monthly_challenges.keys())
    if(month) > len(months):
        return HttpResponseRedirect("/challenge/"+"notfound")
    forward_month = months[month-1]
    redirect_month = reverse("month_challenge",args=[forward_month]) #/challenge
    return HttpResponseRedirect(redirect_month)


def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("Month not available")


def month_list(request):
    list_items =""
    months = list(monthly_challenges.keys())
    for month in months:
        redirect_month = reverse("month_challenge",args=[month]) #/challenge
        list_items += f"<li><a href=\"{redirect_month.capitalize()}\">{month}</a></li>"
    
    response_data =f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
