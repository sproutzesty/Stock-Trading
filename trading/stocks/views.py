from django.shortcuts import render
from .forms import TickerForm

def index(request):
    form = TickerForm()
    return render(request, 'stocks/index.html', {'form':form})