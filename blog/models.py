import random
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver



# Create your models here.
def upload_location(instance, filename):
	file_path = f'blog/{str(instance.author.id)}/{str(instance.title)}-{filename}'
	return file_path


def default_title():
	n=random.randrange(10,99)
	return f'blog{n}'

class BlogPost(models.Model):
	title 					= models.CharField(max_length=50, default=default_title,null=False, blank=False)
	body 					= models.TextField(max_length=5000, default='This is the body',null=True, blank=True)
	image		 			= models.ImageField(upload_to=upload_location, null=True, blank=True)
	date_published 			= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated 			= models.DateTimeField(auto_now=True, verbose_name="date updated")
	author 					= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	slug 					= models.SlugField(blank=True, unique=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog_detail',kwargs={'slug':self.slug})



""" if blog post is deleted then it will delete image also from database"""
@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


""" Here we are creating slug if their is on slug """
# TODO slugify is user fro creating slug

def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(f'{instance.author.username} - {instance.title}')

pre_save.connect(pre_save_blog_post_receiver, sender=BlogPost)