from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.utils.datastructures import MultiValueDictKeyError
from vote.models import *
import md5

# Create your views here.
def form(request):
    if request.POST == {} or request.POST['osis'] == '':
        return render_to_response('vote/swipe.html', context_instance=RequestContext(request))
    try:
        int(request.POST['osis'])
    except ValueError:
        return render_to_response('vote/swipe.html', {'error_message': 'Invalid input.'}, context_instance=RequestContext(request))
    try:
        student = Student.objects.get(osis_digest=md5.new(request.POST['osis']).hexdigest())
    except Student.DoesNotExist:
        return render_to_response('vote/swipe.html', {'error_message': 'Student does not exist.'}, context_instance=RequestContext(request))
    if not student.has_available_elections():
        return render_to_response('vote/swipe.html', {'error_message': 'You have already voted in all available elections.'}, context_instance=RequestContext(request))
    return render_to_response('vote/choose.html', {'osis_digest': student.osis_digest, 'elections': student.get_available_elections(), 'candidates': Candidate.objects.order_by('name')}, context_instance=RequestContext(request))

def vote(request):
    student = Student.objects.get(osis_digest=request.POST['osis_digest'])
    candidate_names = []
    for election in student.get_available_elections():
        try:
            choice_1_id = request.POST['election_' + str(election.id)]
        except MultiValueDictKeyError:
            continue
        try:
            choice_2_id = request.POST['election_' + str(election.id) + '_2']
        except MultiValueDictKeyError:
            choice_2_id = ''
        choice_1 = Candidate.objects.get(id=choice_1_id)
        candidate_names.append(choice_1.__unicode__())
        if choice_2_id != '' and choice_2_id != choice_1_id:
            choice_2 = Candidate.objects.get(id=choice_2_id)
            candidate_names.append(choice_2.__unicode__())
            v = Vote(student=student, election=election, choice_1=choice_1, choice_2=choice_2)
        else:
            v = Vote(student=student, election=election, choice_1=choice_1)
        v.save()
    return render_to_response('vote/vote.html', {'candidate_names': candidate_names})
