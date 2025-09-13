from django.db import models

class Candidate(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  politicalparty = models.CharField(max_length=255)

  userrating = models.FloatField(default=0.0)
  polarrating = models.FloatField(default=0.0)

  totalrating = models.FloatField(default=0.0)
  totalpolar = models.FloatField(default=0.0)
  numoratings = models.IntegerField(default=0)
  numopolars = models.IntegerField(default=0)

  politicalinterests = models.TextField()
  background = models.TextField()
  campaignhistory = models.TextField()
  lobbies = models.TextField()

  corpus = models.TextField()

  consensus = models.TextField()

  
  imageurl = models.URLField(max_length=200)

class Comment(models.Model):
  content = models.TextField()
  user_id = models.CharField(max_length=255)
  timedate = models.DateTimeField(auto_now_add=True)
  candidate_id = models.IntegerField()


# Whne you make changes to models.py, run the following commands to update the database:
# python manage.py makemigrations
# python manage.py migrate