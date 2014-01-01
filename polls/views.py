from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from polls.models import Poll

# Create your views here.
"""
#Attempt 1
def index(request):
	return HttpResponse("Hello world.  Your're at the poll index.")
"""
"""
#Attempt 2
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.question for p in latest_poll_list])
    return HttpResponse(output)
"""
"""
#Attempt 3 - Using /templates/polls/index.html
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))
"""
#Attempt 4
def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	context = {'latest_poll_list': latest_poll_list}
	return render(request, 'polls/index.html', context)

"""
#Attempt 1
def detail(request, poll_id):
#	return HttpResponse("You're looking at poll %s." % poll_id)
"""
#Attempt 2
def detail(request, poll_id):
	try:
		poll = Poll.objects.get(pk = poll_id)
	except Poll.DoesNotExist:
		raise Http404
	return render(request, 'polls/detail.html', {'poll': poll})

"""
#Attempt 1
def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s." % poll_id)
"""
#Attempt 2
def results(request, poll_id):
	try:
		poll = Poll.objects.get(pk = poll_id)
	except Poll.DoesNotExist:
		raise Http404
	return render(request, 'polls/vote_results.html', {'poll': poll})

def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s" % poll_id)