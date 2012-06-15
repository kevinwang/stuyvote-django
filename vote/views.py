from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.utils.datastructures import MultiValueDictKeyError
from vote.models import *

# Create your views here.
def form(request):
    if request.POST == {} or request.POST['osis'] == '':
        return render_to_response('vote/swipe.html', context_instance=RequestContext(request))
    try:
        int(request.POST['osis'])
    except ValueError:
        return render_to_response('vote/swipe.html', {'error_message': 'Invalid input.'}, context_instance=RequestContext(request))
    try:
        student = Student.objects.get(osis=request.POST['osis'])
    except Student.DoesNotExist:
        return render_to_response('vote/swipe.html', {'error_message': 'Student does not exist.'}, context_instance=RequestContext(request))
    if not student.has_available_elections():
        return render_to_response('vote/swipe.html', {'error_message': 'You have already voted in all available elections.'}, context_instance=RequestContext(request))
    return render_to_response('vote/choose.html', {'osis': student.osis, 'elections': student.get_available_elections(), 'candidates': Candidate.objects.all()}, context_instance=RequestContext(request))

def vote(request):
    student = Student.objects.get(osis=request.POST['osis'])
    candidate_names = []
    for election in student.get_available_elections():
        try:
            candidate_id = request.POST['election_' + str(election.id)]
        except MultiValueDictKeyError:
            continue
        if candidate_id != '':
            candidate = Candidate.objects.get(id=candidate_id)
            candidate_names.append(candidate.__unicode__())
            v = Vote(student=student, election=election, choice_1=candidate)
            v.save()
    return render_to_response('vote/vote.html', {'candidate_names': candidate_names})
