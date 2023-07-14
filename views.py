from django.shortcuts import render
from qrcode import*
data=None
# Create your views here.
def homepage(request):
    global data
    if request.method=='POST':
        data=request.POST['data']
        img=make(data)
        img.save('demo/static/images/test.png')
    else:
        pass
    return render(request,'home.html')
