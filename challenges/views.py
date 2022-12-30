from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
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
    return HttpResponse(month)


def monthly_challenge(request,month):
    challenge_text = None
    if month.lower() == "january":
        challenge_text = "This works"
    elif month.lower() == "february":
        challenge_text = "Hot milf"
    elif month.lower() == "march":
        challenge_text = "Hacer ejercicio"
    else:
        return HttpResponseNotFound("This month doesnt exist")
    return HttpResponse(challenge_text)

