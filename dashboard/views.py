from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
import redis

__cache = redis.StrictRedis(host='127.0.0.1', port=6379)


@login_required
@require_http_methods('GET')
def check_login(request):
    return render(request, template_name='index.html')


@login_required
@require_http_methods('GET')
def bus_stations(request):
    str_ = __cache.get('BUS_STATIC').decode('utf-8')
    if not str_:
        return HttpResponseBadRequest()
    return HttpResponse(str_, content_type='application/json')


@login_required
@require_http_methods('GET')
def bus_realtime(request):
    str_ = __cache.get('BUS_REALTIME').decode('utf-8')
    if not str_:
        return HttpResponseBadRequest()
    return HttpResponse(str_, content_type='application/json')


@login_required
@require_http_methods('GET')
def bike_realtime(request):
    str_ = __cache.get('BIKE_REALTIME').decode('utf-8')
    if not str_:
        return HttpResponseBadRequest()
    return HttpResponse(str_, content_type='application/json')