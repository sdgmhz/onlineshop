from django.shortcuts import render

from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutUsPageView(TemplateView):
    template_name = 'pages/aboutus.html'

