from django.shortcuts import render
from app2.models import User
from app2.forms import NewUserForm
# Create your views here.
def users(request):
    # user_list = User.objects.order_by('first_name')
    # user_methods = ['First Name: ', 'Last Name: ', 'Email: ']
    # user_dict = {'user_list': user_list, 'user_methods':user_methods}
    # return render(request, 'app2/users.html',context=user_dict)
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Invalid form')
    return render(request, 'app2/users.html', {'form':form})

def index(request):
    return render(request,'app2/index.html', context=None)
