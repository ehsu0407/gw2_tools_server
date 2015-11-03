from django.shortcuts import render_to_response

__author__ = 'Eddie'

def get_response(request):
    context = {}
    return render_to_response('app/home.html', context)
