from traffiq.forms import TrafficForm
from traffiq.models import TrafficReport

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils.timesince import timesince

import json
from django.utils import timezone


@csrf_exempt
def report(request):
    if request.method == 'POST':
        form = TrafficForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Ok')
        else:
            errors = '\n'.join(form.errors)
            return HttpResponseBadRequest(errors)
    else:
        return HttpResponseBadRequest("only POST requests")


def map(request):
    markers = [','.join(
        (rep.latitude, rep.longitude, rep.response)
        )for rep in TrafficReport.objects.all()]
    markers = [
        {
            'latitude': rep.latitude,
            'longitude': rep.longitude,
            'response': rep.response
        }
        for rep in TrafficReport.objects.all()
    ]
    markers = json.dumps(markers)
    #markers = TrafficReport.objects.all()
    return render(request, 'map.html', {'markers': markers})


def get_markers(request):
    six_hrs_ago = timezone.now() - timezone.timedelta(hours=1)
    markers = [
        {
            'latitude': rep.latitude,
            'longitude': rep.longitude,
            'last_latitude': rep.last_latitude,
            'last_longitude': rep.last_longitude,
            'response': rep.response,
            'since': timesince(rep.when)
        }
        for rep in TrafficReport.objects.filter(when__gte=six_hrs_ago)
    ]
    return HttpResponse(json.dumps(markers), content_type="application/json")
