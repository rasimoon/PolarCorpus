import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")  
django.setup()

from candidates.models import Candidate

''' Params for Candidate model:
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  politicalparty = models.CharField(max_length=255)

  userrating = models.FloatField()
  polarrating = models.FloatField()

  politicalinterests = models.TextField()
  background = models.TextField()
  campaignhistory = models.TextField()
  lobbies = models.TextField()

  corpus = models.TextField()

  consensus = models.TextField()

  
  imageurl = models.URLField(max_length=200)'''

firstname = "Kamala"
lastname = "Harris"
politicalparty = "Democrat"
userrating = 5.0
polarrating = 6.0
politicalinterests = "Middle Class Reform (progessive), Civil Rights (progressive), Environmentalism (moderate), Local Security (gun control), Healthcare (universal healthcare), Tax Reform (wealth tax)"
background = "Birthday: October 20, 1964 (age 60 years), Birthplace: Oakland, California, Education: U.C. Hastings (1989) - J.D., Vice President, Senator"
campaignhistory = "Presidential 2024 (Democrat - Loss), Vice Presidential 2020 (Democrat - Winner), Presidential 2020 (Democrat - Withdrawal), Senatorial 2016 (Democrat - Winner), Attorney General of California 2010 (Democrat - Winner)"
lobbies = "Future Forward USA, Asana, American Bridge 21st Century, Bloomberg LP, Evidence for Impact (DC), Democracy PAC, League of Conservation Voters, Laborers Union   "
corpus = "Books: 107 Days (2025), Smart on Crime (2009), Speeches: Presidential Debate (2024) "
consensus = "A classically progressive democrat, Kamala Harris put a strong emphasis on middle class evolution and reform, especially as a solution to the inflation crisis. Nonetheless, her questionable long-term solutions to major problems and seeming lack of prior action made her untrustworthy among the general population."
imageurl = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Kamala_Harris_Official_Portrait_2019.jpg/800px-Kamala_Harris_Official_Portrait_2019.jpg "


candidate = Candidate(firstname=firstname, lastname=lastname, politicalparty=politicalparty, userrating=userrating, polarrating=polarrating, politicalinterests=politicalinterests, background=background, campaignhistory=campaignhistory, lobbies=lobbies, corpus=corpus, consensus=consensus, imageurl=imageurl)

candidate.save()
print("Successfully saved candidate to database.")

# To update data...
# x = Candidate.objects.all().filter(firstname="Donald").update(lastname="Trump Jr.") or
# x = Candidate.objects.all()[index]
# x.y = "z"
# x.save()

# To delete data...
# x = Candidate.objects.all().filter(firstname="Donald").delete() or
# x = Candidate.objects.all()[index]
# x.delete()


print(Candidate.objects.all().values())  #Prints a list of all republican candidates, can be indexed like regular list