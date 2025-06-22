from django.shortcuts import render
from .models import Section, SkillItem, FooterLink
from datetime import datetime

def homepage(request):
    sections = Section.objects.all().order_by('order').prefetch_related('images', 'skill_items', 'project_items')
    skills = SkillItem.objects.all()
    footer_links = FooterLink.objects.all()
    year = datetime.now().year

    context = {
        'sections': sections,
        'skills': skills,
        'footer_links': footer_links,
        'year': year,
    }
    return render(request, 'website/home.html', context)
