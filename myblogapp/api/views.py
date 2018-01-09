from django.http import JsonResponse

from posts.models import (
    Post,
)


def posts_list(request):
    json_list = []
    for post in Post.objects.all():
        json_list.append(post.to_list())
    return JsonResponse(json_list, safe=False)


'''
def posts_list(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="blog.csv"'

    writer = csv.writer(response)
    writer.writerow([request.title, request.published, request.image, request.body])

    return response
'''
