from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from django.core.cache import cache

class HomePageView(View):
    def get(self, request):
        # Increment visit counter
        visit_count = cache.get('visit_count', 0)
        cache.set('visit_count', visit_count + 1)

        # Render template with title and visit count
        return render(request, 'home.html', {'title': 'How many Dawgs have been Shawged?', 'visit_count': visit_count})