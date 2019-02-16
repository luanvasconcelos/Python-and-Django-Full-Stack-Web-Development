from django.shortcuts import render

# Create your views here.
def help(request):
    helpdict ={'help_insert':'Help page'}
    return render(request, 'apptwo/help.html', context=helpdict)
