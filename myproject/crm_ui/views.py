# crm_ui/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from courses.models import Course
from crm_ui.NetworkHelper import NetworkHelper
from crm_ui.form import CourseForm
from django.shortcuts import redirect, render

NetworkHelper.set_token("53ef2716827d677a0970eceb63d77a08e8cdccc7")

class EntityListView(ListView):
    model = Course
    template_name = "crm_ui/list.html"

class EntityDetailView(DetailView):
    model = Course
    template_name = "crm_ui/detail.html"

class EntityCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = "crm_ui/form.html"
    success_url = reverse_lazy('entity_list')

class EntityUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "crm_ui/form.html"
    success_url = reverse_lazy('entity_list')

class EntityDeleteView(DeleteView):
    model = Course
    template_name = "crm_ui/confirm_delete.html"
    success_url = reverse_lazy('entity_list')


class ActivityListView(ListView):
    template_name = "activities/list.html"
    context_object_name = "activities"

    def get_queryset(self):
        return NetworkHelper.get_activities()

def activity_delete(request, pk):
    activity = None
    activities = NetworkHelper.get_activities()
    for a in activities:
        if a['id'] == pk:
            activity = a
            break

    if request.method == "POST":
        NetworkHelper.delete_activity(pk)
        return redirect('activity_list')

    return render(request, "activities/confirm_delete.html", {"object": activity})
    

class CommentListView(ListView):
    template_name = "comments/list.html"
    context_object_name = "comments"

    def get_queryset(self):
        return NetworkHelper.get_comments()

def comment_delete(request, pk):
    comment = None
    comments = NetworkHelper.get_comments()
    for c in comments:
        if c['id'] == int(pk):
            comment = c
            break

    if request.method == "POST":
        NetworkHelper.delete_comment(pk)
        return redirect('comment_list')

    return render(request, "comments/confirm_delete.html", {"object": comment})