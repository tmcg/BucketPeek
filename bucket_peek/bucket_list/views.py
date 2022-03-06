from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

import boto3
from botocore.exceptions import ClientError

def index(request):
    s3 = boto3.resource('s3')
    bucket_names = [b.name for b in s3.buckets.all()]

    template = loader.get_template("bucket_list/index.html")
    context = {
        'bucket_names': bucket_names,
    }

    return HttpResponse(template.render(context, request))

def bucket(request, name):
    s3 = boto3.resource("s3")
    bucket = s3.Bucket(name)
    versioning = bucket.Versioning()

    try:
        lifecycle_rules = len(bucket.LifecycleConfiguration().rules)
    except ClientError:
        lifecycle_rules = 0

    template = loader.get_template("bucket_list/bucket.html")
    context = {
        'bucket_name': bucket.name,
        'versioning_status': versioning.status,
        'lifecycle_rules': lifecycle_rules,
    }

    return HttpResponse(template.render(context, request))
