from django.shortcuts import render, redirect
from .models import TravelPlace
from django import forms
from django.contrib.auth.decorators import login_required
from .forms import VisitSubmissionForm
# Form for adding TravelPlace
from django.db.models import Count
from .models import TravelPlace, VisitSubmission
from .models import VisitSubmission
from django.contrib.auth.decorators import login_required
class TravelPlaceForm(forms.ModelForm):
    class Meta:
        model = TravelPlace
        fields = ['title', 'location', 'description']

def home(request):
    places = TravelPlace.objects.all().order_by('-added_on')
    return render(request, 'bucketlist/home.html', {'places': places})

def add_place(request):
    if request.method == 'POST':
        form = TravelPlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TravelPlaceForm()
    return render(request, 'bucketlist/add_place.html', {'form': form})
@login_required
def submit_visit(request):
    if request.method == 'POST':
        form = VisitSubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.user = request.user
            submission.save()
            return redirect('my_submissions')
    else:
        form = VisitSubmissionForm()
    return render(request, 'bucketlist/submit_visit.html', {'form': form})
@login_required
def my_submissions(request):
    submissions = VisitSubmission.objects.filter(user=request.user).select_related('place')
    return render(request, 'bucketlist/my_submissions.html', {'submissions': submissions})
def most_wanted_places(request):
    places = TravelPlace.objects.annotate(
        visit_count=Count('visitsubmission')
    ).order_by('-visit_count')

    return render(request, 'bucketlist/most_wanted.html', {'places': places})