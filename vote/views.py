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
    if not s.has_available_elections():
        return render_to_response('vote/swipe.html', {'error_message': 'There are no available elections for this student.'}, context_instance=RequestContext(request))
