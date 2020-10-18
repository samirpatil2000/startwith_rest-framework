from rest_framework import serializers
from blog.models import BlogPost


class BlogPostSereliazer(serializers.ModelSerializer):

    username=serializers.SerializerMethodField('get_username_form_author')
    class Meta:
        model=BlogPost
        fields=['title','body','image','date_published','username']

    def get_username_form_author(self,blog_post):
        username=blog_post.author.email
        return username
