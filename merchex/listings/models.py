# from django.db import models
from django.db.models import Model as M
from django.db import models as m
# from django.db.models import Field
# from django.db.models import field as F

# Create your models here.
class Band(M):
  name=m.CharField(max_length=100)

class Listing(M):
    title=m.CharField(max_length=100)
