from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import TickerForm
from .tiingo import get_meta_data

def index(request):
    if request.method == 'POST':
        form = TickerForm(request.POST)
        if form.is_valid():
            ticker = request.POST['ticker']
            return HttpResponseRedirect(ticker)
    else:
        form = TickerForm()
    return render(request, "stocks/index.html", {"form":form})

def ticker(request, tid):
    context = {}
    context['ticker'] = tid
    context['meta'] = get_meta_data(tid)
    return render(request, "stocks/ticker.html", context)