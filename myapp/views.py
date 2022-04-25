from django.shortcuts import render
from . forms import ImageForm
from . models import Image
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageForm
        img = Image.objects.all()
    return render(request, 'myapp/home.html', {'img':img, 'form':form})
# Create your views here.
