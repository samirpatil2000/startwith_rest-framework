from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from account.models import Account
from blog.models import BlogPost
from blog.api.serializer import BlogPostSereliazer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication

@api_view(['GET',])
@permission_classes([IsAuthenticated])
def blog_api_detail(request,slug):
    try:
        blog_post=BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        sereliazer=BlogPostSereliazer(blog_post)
        return Response(sereliazer.data)

@api_view(['PUT',])
@permission_classes([IsAuthenticated])
def blog_api_update(request,slug):
    try:
        blog_post=BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data={

    }
    user=request.user
    if blog_post.author != user:
        return Response({'response':" You don't have permissions "})
    if request.method =='PUT':
        selerizer=BlogPostSereliazer(blog_post)
        if selerizer.is_valid():
            selerizer.save()
            data['success']='Updated Successfully'
            return Response(data=data)
        return Response(selerizer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
@permission_classes([IsAuthenticated])
def blog_api_delete(request,slug):
    try:
        blog_post=BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data={

    }
    if blog_post.author != request.user:
        return Response({'response':'You donot have permissions '})
    if request.method =='DELETE':
        operation=blog_post.delete()
        data={}
        if operation:
            data['success']='Delete Successfully'
            return Response(data=data)
        else:
            data['failure']='Delete Failed'

@api_view(['POST',])
@permission_classes([IsAuthenticated])
def blog_api_create(request,slug):
    account=request.user

    blog_post=BlogPost(author=account)

    if request.method == 'POST':
        serializer=BlogPostSereliazer(blog_post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class BlogApiListView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSereliazer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
