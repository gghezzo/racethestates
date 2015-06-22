from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import raceDetail
from .forms import raceDetailForm
from django.shortcuts import redirect

# This is my view 
def race_list(request):
    races = raceDetail.objects.filter(raceDate__lte=timezone.now()).order_by('raceDate')
    return render(request, 'raceDetail/race_list.html', {'races':races})

