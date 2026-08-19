from django.http import HttpResponse
import pathlib
from django.shortcuts import render

from visits.models import PageVisit

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all() # qs = queryset
    page_qs = PageVisit.objects.filter(path=request.path)
    
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "queryset": qs,
        "page_visit_count": page_qs.count(),
        "total_visit_count": qs.count(),
        "percent": (page_qs.count() * 100.0) / qs.count()
    }
    path = request.path
    print("path", path)
    html_template = "home.html"
    
    PageVisit.objects.create(path=request.path)
    
    return render(request, html_template, my_context)