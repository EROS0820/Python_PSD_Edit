from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.

def dashboard(request):
	return render(request, 'dashboard.html')

def upload(request):
    context = {}
    if request.method == 'POST':
        leftsleev = request.FILES['leftsleev']
        rightsleev = request.FILES['rightsleev']
        lefthood = request.FILES['lefthood']
        righthood = request.FILES['righthood']
        front = request.FILES['front']
        fs = FileSystemStorage()
        name = fs.save('leftsleev', leftsleev)
        name = fs.save('rightsleev', rightsleev)
        name = fs.save('lefthood', lefthood)
        name = fs.save('righthood', righthood)
        name = fs.save('front', front)
        # context['url'] = fs.url(name)
    return render(request, 'dashboard.html', context)

