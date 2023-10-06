from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.
def index(request): 
    return render(request,'pages/home.html')
def contact(request):
    return render(request, 'pages/contact.html')
def index1(request): 
    return render(request,'page/khoahoc.html')
def register (request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Bạn đã đăng kí thành công tài khoản !!!" )
            return HttpResponseRedirect('/')
        messages.error(request, "Đăng ký không thành công. Thông tin không hợp lệ !!!")
    return render(request, 'pages/register.html',{'form': form})
def error_404(request, exception):
    return render(request, '', exception)
def error_500(request):
    return render(request, '')


