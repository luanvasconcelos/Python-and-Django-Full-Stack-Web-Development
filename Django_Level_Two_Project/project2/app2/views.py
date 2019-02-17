from django.shortcuts import render
from app2.models import User
from django.http import HttpResponse
# Create your views here.
def users(request):
    user_list = User.objects.order_by('first_name')
    user_methods = ['First Name: ', 'Last Name: ', 'Email: ']
    user_dict = {'user_list': user_list, 'user_methods':user_methods}
    return render(request, 'app2/users.html',context=user_dict)

def index(request):
    return render(request,'app2/index.html', context=None)
