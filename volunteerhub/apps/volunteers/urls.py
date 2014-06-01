from django.conf.urls import patterns, url
from .views import (OpportunityDetailView, ProjectListView,
                    ProjectDetailView, ProjectListJSONView,
                    ProjectDetailJSONView, OpportunityDetailJSONView,
                    DashboardView, ProfileUpdateView)

# custom views
urlpatterns = patterns(
    '',
    url(r'^projects/(?P<project_slug>[-\w]+)/opportunities/(?P<slug>[-\w]+).json',
        view=OpportunityDetailJSONView.as_view(),
        name="opportunity-detail-json"),

    url(r'^projects/(?P<project_slug>[-\w]+)/opportunities/(?P<slug>[-\w]+)/',
        view=OpportunityDetailView.as_view(),
        name="opportunity-detail"),

    url(r'^projects/(?P<slug>[-\w]+)/opportunities.json',
        view=ProjectDetailJSONView.as_view(),
        name="project-detail-json"),

    url(r'^projects/(?P<slug>[-\w]+)/opportunities/',
        view=ProjectDetailView.as_view(),
        name="project-detail"),

    url(r'^projects.json',
        view=ProjectListJSONView.as_view(),
        name="project-list-json"),

    url(r'^projects/',
        view=ProjectListView.as_view(),
        name="project-list"),

    url(r'dashboard/edit-profile/',
        view=ProfileUpdateView.as_view(),
        name="profile-update"),

    url(r'dashboard/',
        view=DashboardView.as_view(),
        name="dashboard"),

    url(r'^',
        view=ProjectListView.as_view(),
        name="homepage"),

)