from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

def index(request):

    bucket_names = [ "bucket1", "bucket2", "bucket3" ]

    template = loader.get_template("bucket_list/index.html")
    context = {
        'bucket_names': bucket_names,
    }

    return HttpResponse(template.render(context, request))
