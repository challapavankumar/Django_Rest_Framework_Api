#third party imports
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import PostSerializers
from .models import Post
class Testview(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,*args,**kwargs):
        res=Post.objects.all()
        post=res.first()
        serializers=PostSerializers(post)
        return Response(serializers.data)
    def post(self,request,*args,**kwargs):
        serializers=PostSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
class PostView(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):
        serializer_class = PostSerializers
        queryset = Post.objects.all()
        def get(self,request,*args,**kwargs):
            return self.list(request,*args,**kwargs)
        def post(self,request,*args,**kwargs):
            return self.create(request,*args,**kwargs)
class PostCreateView(mixins.ListModelMixin,generics.CreateAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()