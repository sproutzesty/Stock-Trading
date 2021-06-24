from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TickerForm
from .tiingo import get_meta_data, get_price_data
from rest_framework.veiws import APIView
from rest_framework.response import Response


def index(request):
    if request.method == 'POST':
        form = TickerForm(request.POST)
        if form.is_valid():
            ticker = request.POST['ticker']
            print("there was an no error in index request")
            return HttpResponseRedirect(ticker) 
    else:
        form = TickerForm()
        print("there was an error in index request")
        return render(request, "stocks/index.html", {"form":form})

class HelloView(APIView):
    def get(self, request):
        content={'message': 'Hello World'}
        return Response(content)

def ticker(request, tid):
    context= {}
    context ['ticker'] = tid
    context['meta'] = get_meta_data(tid)
    context['price'] = get_price_data(tid)
    print("there was an error in ticker request")
    return render(request, "stocks/ticker.html", context)
