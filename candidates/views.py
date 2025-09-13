from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import feedparser
from random import randint 
from .models import Candidate
from .models import Comment 


def home(request):

  x = randint(0, Candidate.objects.count() - 1)
  featured_candidate = Candidate.objects.all()[x].firstname + " " + Candidate.objects.all()[x].lastname
  polarrating = Candidate.objects.all()[x].polarrating
  userrating = Candidate.objects.all()[x].userrating
  politicalparty = Candidate.objects.all()[x].politicalparty
  politicalinterests = Candidate.objects.all()[x].politicalinterests
  background = Candidate.objects.all()[x].background
  consensus = Candidate.objects.all()[x].consensus

  # News Content
  url = "https://news.google.com/rss/search?q=politics&hl=en-US&gl=US&ceid=US:en"
  feed = feedparser.parse(url)

  news = None 
  #template = loader.get_template('main.html')
  return render(request, 'main.html', {
        'home': home,
        'featured_candidate': featured_candidate,
        'news': news,
        'polarrating': polarrating,
        'userrating': userrating,
        'politicalparty': politicalparty,
        'politicalinterests': politicalinterests,
        'background': background,
        'consensus': consensus,

        "articles" : feed.entries[:5]

    })

def leftcandidates(request):
  candidates = Candidate.objects.filter(politicalparty="Democrat").values()

  #template = loader.get_template('main.html')
  return render(request, 'left.html', {
        'leftcandidates': leftcandidates,
        'candidates': candidates,
      
    })

def rightcandidates(request):
  candidates = Candidate.objects.filter(politicalparty="Republican").values()

  #template = loader.get_template('main.html')
  return render(request, 'right.html', {
        'rightcandidates': rightcandidates,
        'candidates': candidates,
      
    })

def candidate(request):
  x = 0
  firstlast = Candidate.objects.all()
  polarrating = Candidate.objects.all()[x].polarrating
  userrating = Candidate.objects.all()[x].userrating
  politicalparty = Candidate.objects.all()[x].politicalparty
  politicalinterests = Candidate.objects.all()[x].politicalinterests
  background = Candidate.objects.all()[x].background
  consensus = Candidate.objects.all()[x].consensus

  news = None 
  #template = loader.get_template('main.html')
  return render(request, 'candidate.html', {
        'candidate': candidate,

        'polarrating': polarrating,
        'userrating': userrating,
        'politicalparty': politicalparty,
        'politicalinterests': politicalinterests,
        'background': background,
        'consensus': consensus

    })

def chosen_candidate_right(request):
    if request.method == "POST":
        choice = request.POST.get("choice")
        candidate = Candidate.objects.filter(lastname=choice).values()[0]
        firstlast = candidate['firstname'] + " " + candidate['lastname']
        polarrating = candidate['polarrating']
        userrating = candidate['userrating']
        politicalparty = candidate['politicalparty']
        politicalinterests = candidate['politicalinterests']
        background = candidate['background']
        consensus = candidate['consensus']

        candidate_id = candidate['id']

        comments = Comment.objects.filter(candidate_id=candidate_id).values()


    return render(request, "candidate.html", {
        'chosen_candidate_right': chosen_candidate_right,

        'candidate_id': candidate_id,
        'candidate': firstlast,

        'user_id': "None",

        'polarrating': polarrating,
        'userrating': userrating,
        'politicalparty': politicalparty,
        'politicalinterests': politicalinterests,
        'background': background,
        'consensus': consensus,
        'comments': comments


        
    })

def chosen_candidate_left(request):
    if request.method == "POST":
        choice = request.POST.get("choice")
        candidate = Candidate.objects.filter(lastname=choice).values()[0]
        firstlast = candidate['firstname'] + " " + candidate['lastname']
        polarrating = candidate['polarrating']
        userrating = candidate['userrating']
        politicalparty = candidate['politicalparty']
        politicalinterests = candidate['politicalinterests']
        background = candidate['background']
        consensus = candidate['consensus']

        candidate_id = candidate['id']

        comments = Comment.objects.filter(candidate_id=candidate_id).values()

    return render(request, "candidate.html", {
        
        'chosen_candidate_left': chosen_candidate_left,

        'candidate_id': candidate_id,
        'candidate': firstlast,

        'user_id': "None",

        'polarrating': polarrating,
        'userrating': userrating,
        'politicalparty': politicalparty,
        'politicalinterests': politicalinterests,
        'background': background,
        'consensus': consensus,

        'comments': comments
    })

def submit_rating(request):
    if request.method == "POST":
        rating = request.POST.get("rating")  # comes in as a string
        candidate_id = request.POST.get("candidate_id")
        candidate = Candidate.objects.filter(id=candidate_id).values()[0]

        try:
            rating = float(rating)  # convert to decimal
            new_tot = candidate['totalrating'] + rating 
            new_num = candidate['numoratings'] + 1
            new_rating = new_tot / new_num
            Candidate.objects.all().filter(id=candidate_id).update(totalrating=new_tot, numoratings=new_num, userrating=new_rating)

        except (TypeError, ValueError):
            rating = None

        comments = Comment.objects.filter(candidate_id=candidate_id).values()
        firstlast = candidate['firstname'] + " " + candidate['lastname']

        polarrating = candidate['polarrating']
        userrating = candidate['userrating']
        politicalparty = candidate['politicalparty']
        politicalinterests = candidate['politicalinterests']
        background = candidate['background']
        consensus = candidate['consensus']
        
    return render(request, "candidate.html", {
        'submit_rating': submit_rating,

        'candidate_id': candidate_id,

        'candidate': firstlast,

        'user_id': "Anonymous",

        'polarrating': polarrating,
        'userrating': userrating,
        'politicalparty': politicalparty,
        'politicalinterests': politicalinterests,
        'background': background,
        'consensus': consensus,

        'comments': comments
    })

def submit_polarization(request):
    if request.method == "POST":
        rating = request.POST.get("polarrating")
        candidate_id = request.POST.get("candidate_id") # comes in as a string
        candidate = Candidate.objects.filter(id=candidate_id).values()[0]

        try:
            rating = float(rating)  # convert to decimal
            new_tot = candidate['totalpolar'] + rating 
            new_num = candidate['numopolars'] + 1
            new_rating = new_tot / new_num
            Candidate.objects.all().filter(id=candidate_id).update(totalpolar=new_tot, numopolars=new_num, polarrating=new_rating)


        except (TypeError, ValueError):
            rating = None
        comments = Comment.objects.filter(candidate_id=candidate_id).values()
        firstlast = candidate['firstname'] + " " + candidate['lastname']

        polarrating = candidate['polarrating']
        userrating = candidate['userrating']
        politicalparty = candidate['politicalparty']
        politicalinterests = candidate['politicalinterests']
        background = candidate['background']
        consensus = candidate['consensus']

    
    return render(request, "candidate.html", {
        'submit_polarization': submit_polarization,
        
        'candidate_id': candidate_id,

        'candidate': firstlast,

        'user_id': "Anonymous",

        'polarrating': polarrating,
        'userrating': userrating,
        'politicalparty': politicalparty,
        'politicalinterests': politicalinterests,
        'background': background,
        'consensus': consensus,

        'comments': comments
    })

def submit_comment(request):
    if request.method == "POST":
        comment = request.POST.get("comment") 
        candidate_id = request.POST.get("candidate_id")
        candidate = Candidate.objects.filter(id=candidate_id).values()[0]
        firstlast = candidate['firstname'] + " " + candidate['lastname']

        polarrating = candidate['polarrating']
        userrating = candidate['userrating']
        politicalparty = candidate['politicalparty']
        politicalinterests = candidate['politicalinterests']
        background = candidate['background']
        consensus = candidate['consensus']


        new_comment = Comment(content=comment , user_id = "Anonymous" , candidate_id = candidate_id )
        new_comment.save()


        comments = Comment.objects.filter(candidate_id=candidate_id).values()

    return render(request, "candidate.html", {
        'submit_comment': submit_comment,
        
        'candidate_id': candidate_id,

        'candidate': firstlast,

        'user_id': "Anonymous",

        'polarrating': polarrating,
        'userrating': userrating,
        'politicalparty': politicalparty,
        'politicalinterests': politicalinterests,
        'background': background,
        'consensus': consensus,

        'comments': comments
    })