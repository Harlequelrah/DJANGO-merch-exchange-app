# from django.db import models
from django.db.models import Model as M
from django.db import models as m
from django.core.validators import MaxValueValidator, MinValueValidator
"""_summary_

 """

# Create your models here.
class Band(M):
  class Genre(m.TextChoices):
    HIP_HOP = 'HH'
    SYNTH_POP = 'SP'
    ALTERNATIVE_ROCK = 'AR'
    GOSPEL='GP'
  name=m.CharField(max_length=100)
  genre =m.CharField(choices=Genre.choices,max_length=25)
  biographie=m.CharField(max_length=1000)
  year_formed=m.IntegerField(validators=[
    MinValueValidator(1990),
    MaxValueValidator(2024)
    ]) # Django a aussi un DateField , mais il comprendrait aussi un mois et un jour, qui ne seraient pas utilisés dans ce cas.
  active=m.BooleanField(default=True)
  official_homepage=m.URLField(null=True,blank=True)








class Listing(M):
  class Type(m.TextChoices):
    DISQUE='DSQ'
    VETEMENT='VTM'
    AFFICHE='AFC'
    DIVERS='DVR'

  title=m.CharField(max_length=100)
  description=m.CharField(max_length=256 ,null=True)
  sold=m.BooleanField(default=False)
  year=m.IntegerField(null=True,validators=[MinValueValidator(2000)])
  types=m.CharField(choices=Type.choices,max_length=25)
