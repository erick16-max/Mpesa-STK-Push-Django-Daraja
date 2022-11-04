from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django_daraja.mpesa.core import MpesaClient
from django.urls import reverse

def index(request):
    cl = MpesaClient()
    token = cl.access_token()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0716030958'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    print(token)
    return HttpResponse(response)

def stk_push_callback(request):
        data = request.body
        # You can do whatever you want with the notification received from MPESA here.
        return HttpResponse(data)