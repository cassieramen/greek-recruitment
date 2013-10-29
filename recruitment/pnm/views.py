from django.shortcuts import render
from django.http import Http404

from models import PNM

def index(request):
  allPNMs = PNM.objects.all()
  context = {'allPNMs':allPNMs}
  return render(request,'pnm/index.html', context)

def detail(request, pnmId):
  try:
    pnm = PNM.objects.get(pk=pnmId)
  except PNM.DoesNotExist:
    raise Http404
  return render(request, 'pnm/detail.html',{'pnm':pnm})
