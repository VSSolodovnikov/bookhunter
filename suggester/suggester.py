from tastypie.resources import ModelResource
from suggester.models import BookSuggester
from django.http import HttpResponse

class suggester(ModelResource):
    class Meta:
        queryset = BookSuggester.objects.all()
        resource_name = 'suggest'

    def get_object_list(self, request):
        if 'q' in request.GET and request.GET['q']:
            q = request.GET['q']
            books = BookSuggester.objects.filter(name__icontains=q)
            return books
        else:
            return HttpResponse('Please submit a search term.')

#        return super(suggester, self).get_object_list(request).filter(isbn=request.GET['letter'])