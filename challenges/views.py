from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect
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
        return HttpResponseRedirect("/challenges/"+"notfound")
    forward_month = months[month-1]
    return HttpResponseRedirect("/challenges/"+forward_month)


def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Month not available")

