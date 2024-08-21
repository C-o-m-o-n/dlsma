from django.shortcuts import render, HttpResponse
import requests

# Create your views here.

# data = {
#   "data": [
#     {
#       "access_token": "page_access_token",
#       "category": "Internet Company",
#       "category_list": [
#         {
#           "id": "2256",
#           "name": "Internet Company"
#         }
#       ],
#       "name": "Name of this Page",
#       "id": "page_id",
#       "tasks": [
#         "ANALYZE",
#         "ADVERTISE",
#         "MODERATE",
#         "CREATE_CONTENT"
#       ]
#     }
#   ]
# }

access_token = "EAAGWlcWyhqMBO7GFJs21i7KAkIQ69TcCG6XM0MMsUNrBGlLxSuZCe6lkjASyZC8XbSHCA9bqjaTdkcyTtQG7Tce5lJ5ZCqYELAQPBrkLNgOakQySg3AnXfg0UNqBRon2X6ZAGw0EPBUjaF1N99ZAZBPrVUsnrtwxeZAXSABdKoMsYwRxYkKFf1aSf7kRcbWIR8DuMwtULRXNAZDZD"

def get_facebook_pages(request):
    # access_token = request.user.social_auth.get(provider='facebook').extra_data['access_token']
    # url = f'https://graph.facebook.com/v12.0/me/accounts?access_token={access_token}'
    # response = requests.get(url)
    # print(response)
    # return requests.Response(response.json())
    return HttpResponse("Hello world")