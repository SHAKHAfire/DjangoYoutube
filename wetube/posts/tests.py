from django.test import TestCase

# Create your tests here.
from models import PostComment



for i in PostComment.objects.all():
    if i.pk == 49:
        i.delete()
        print('deleted')