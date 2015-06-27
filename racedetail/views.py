from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import raceDetail
from .forms import raceDetailForm
from django.shortcuts import redirect

# This is my view 
def race_list(request):
    races = raceDetail.objects.filter(raceDate__lte=timezone.now()).order_by('raceDate')
    return render(request, 'racedetail/race_list.html', {'races':races})

def race_prettymap(request):
    race = raceDetail.objects.filter(raceDate__lte=timezone.now()).order_by('raceDate')
    return render(request, 'racedetail/prettymap.html', {'race':race})

def race_detail(request):
    race = get_object_or_404(raceDetail, pk=pk)
    return render(request, 'racedetail/race_detail.html', {'race': race})

def race_new(request):
    if request.method == "POST":
        form = raceDetailForm(request.POST)
        if form.is_valid():
            race = form.save(commit=False)
            race.runnerName = request.user
            race.save()
            race.publish()
            return redirect('racedetail.views.race_detail', pk=race.pk)
    else:
        form = raceDetailForm()
    return render(request, 'racedetail/race_edit.html', {'form': form})

def race_edit(request, pk):
    race = get_object_or_404(raceDetail, pk=pk) # Not sure what the second race should be? Post? 
    if request.method == "POST":
        form = raceDetailForm(request.POST, instance=race)
        if form.is_valid():
            race = form.save(commit=False)
            race.runnerName = request.user
            race.save()
            race.publish()
            return redirect('racedetail.views.race_detail', pk=race.pk)
    else:
        form = raceDetailForm(instance=race)
    return render(request, 'racedetail/race_edit.html', {'form': form})


