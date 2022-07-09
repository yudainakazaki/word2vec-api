# all the endpoints come here
import json
from telnetlib import STATUS
from django.http import JsonResponse
from .models import W2V
from .serializers import W2VSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from getSimilarity import getSimilarity

@api_view(['GET', 'POST'])
# def w2v_list(request):

#     if request.method == 'GET':
#         w2vs = W2V.objects.all()
#         serializer = W2VSerializer(w2vs, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     if request.method == 'POST':
#         serializer = W2VSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

def returnSimilarity(request):
    if request.method == 'GET':
        data = json.loads(request.body.decode("utf-8"))
        w1 = data['word1']
        w2 = data['word2']
        res = getSimilarity(w1, w2)
        returnValue = {
            'similarity': res
        }
        return JsonResponse(returnValue, safe=False, status=status.HTTP_200_OK)
        
        