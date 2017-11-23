from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from imgurpython import ImgurClient
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import History
from .serializers import HistorySerializer

client_id = '7107129cd0a4a00'
client_secret = '8400a4ead045a798b95bb3e0d86f913d8cf3e5bc'
access_token = '86375bf972c19219f89a3616bf29c47ac492d183'
refresh_token = 'df27297843576325e8b40e36725463006c3ea08f'
client = ImgurClient(client_id, client_secret, access_token, refresh_token)

def search(request, data):
    r = History.objects.create(search=data)
    r.save()
    items = client.gallery_search(data, advanced=None, sort='time', page=0)
    links = []

    for item in items:
        json = {
            "link": item.link,
            "title": item.title,
            "img-id": item.id,
            "views": item.views,
        }
        links.append(json)

        # value = request.GET.get('offset', '')
        # paginator = Paginator(links, value)
        # try:
        #     page = paginator.page[value]
        # except PageNotAnInteger:
        #     page = paginator.page[1]
        # except EmptyPage:
        #     page = paginator.page(paginator.num_page)
    
    return JsonResponse(links, safe=False)
    

def recent(request):
    
    a = History.objects.all()[:10]
    serializer = HistorySerializer(a, many=True)
    return JsonResponse(serializer.data, safe=False)    

    
