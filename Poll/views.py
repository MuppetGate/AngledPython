# Create your views here.

from django.http import HttpResponse, Http404
from Poll.models import Poll
from django.shortcuts import render
from jsonview.decorators import json_view


def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)


def jsonIndex(request):
    return render(request, 'polls/jsonIndex.html')

def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', {'poll': poll})


# Does the same as the one above, except the result is
# going to be returned as a JSON string.
@json_view
def detailJson(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return poll.convert_to_dict()


def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)


def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)