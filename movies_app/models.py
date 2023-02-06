from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name= models.CharField(db_column='movie_name',max_length=126,
                                 null=False,blank=False , db_index=True)
    duration_in_min=models.FloatField(db_column='duration',null=False)
    release_year=models.IntegerField(
        db_column='year',null=False,
        validators=[MinValueValidator(1900),MaxValueValidator(2050)])
    pic_url=models.URLField(max_length=512,db_column='pic_url',null=True,blank=True )

    def __str__(self):
        return self.movie_name
    class Meta:
        db_table='movies'

class Rating(models.Model):

    movie=models.ForeignKey("Movie",on_delete=models.RESTRICT)
    rating=models.SmallIntegerField(db_column='rating',null=False, blank=False,
                                    validators=[MinValueValidator(1),MaxValueValidator(11)])
    def __str__(self):
        return str(self.rating)

    class Meta:
        db_table='ratings'
