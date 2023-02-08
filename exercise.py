import os
import django
from datetime import datetime


os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"
django.setup()

from movies_app.models import *

#1
# birth_year_=datetime.now().year-50
# data_birth_year=Actor.objects.all()
# for d in data_birth_year:
#     if d.birth_year>birth_year_:
#         print(f"Get actor in the db who are younger than 50 years old: {d.name}")

#2
# data=Movie.objects.all()
# for d in data:
#     if d.duration_in_min<2.5 and d.release_year>2005:
#         print(f"{d.movie_name}")


