import csv
from django.http import HttpResponse
# from django.http import JsonResponse

from posts.models import (
    Post,
)

'''
def posts_list(request):
    posts = [post.to_list() for post in Post.objects.order_by("id").all()]
    return JsonResponse(posts, safe=False)


'''
def posts_list(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="blog.csv"'

    posts = [post.to_list() for post in Post.objects.order_by("id").all()]
    writer = csv.writer(response)
    writer.writerow(posts)

    return response
