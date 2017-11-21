from django.shortcuts import render
from django.http import HttpResponse
from imgurpython import ImgurClient

client_id = '7107129cd0a4a00'
client_secret = '8400a4ead045a798b95bb3e0d86f913d8cf3e5bc'
access_token = '86375bf972c19219f89a3616bf29c47ac492d183'
refresh_token = 'df27297843576325e8b40e36725463006c3ea08f'
client = ImgurClient(client_id, client_secret, access_token, refresh_token)

def search(request, data):
    items = client.gallery_search(data, advanced=any, sort='time', window='all', page=0)
    for item in items:
        return HttpResponse(item.link)