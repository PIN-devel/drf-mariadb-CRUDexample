from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
# Create your views here.
# @api_view(['GET','POST'])
# def read_or_create(request):
#     if request.method == 'GET': # read
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles,many=True)
#         return Response(serializer.data)
        
#     else: # POST create
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

# @api_view(['PUT','DELETE'])
# def update_or_delete(request,id):
#     article = Article.objects.get(id=id)
#     if request.method == 'PUT': # update
#         serializer = ArticleSerializer(article,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     else: # DELETE delete
#         article.delete()
#         return Response({'status':'delete complete'})
    

