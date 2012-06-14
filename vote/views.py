from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from vote.models import *

# Create your views here.
def form(request):
    if request.POST == {} or request.POST['osis'] == '':
        return render_to_response('vote/swipe.html', context_instance=RequestContext(request))
    try:
        s = Student.objects.get(osis=request.POST['osis'])
    except Student.DoesNotExist:
        return render_to_response('vote/swipe.html', {'error_message': 'Student does not exist.'}, context_instance=RequestContext(request))
    candidates = Candidate.objects.filter(grade=s.grade)
    if Vote.objects.filter(student=s).count() > 0:
        return render_to_response('vote/swipe.html', {'error_message': 'You have already voted.'}, context_instance=RequestContext(request))
    return render_to_response('vote/showchoices.html', {'candidates': candidates}, context_instance=RequestContext(request))
