from django.shortcuts import render,redirect
import requests

def index(request):
    username = request.GET.get('username')
    if username == '':
        error = 'Please enter a username'
        return render(request, 'index.html',{'error':error})
    data = requests.get(f'https://api.github.com/users/{username}').json()
    if data.get('message') == 'Not Found':
        error = 'User not found'
        return render(request, 'index.html',{'error':error})
    context = {
        'data':data,
        'followers':requests.get(f'https://api.github.com/users/{username}/followers').json(),
        'following':requests.get(f'https://api.github.com/users/{username}/following').json(),
        'repos':requests.get(f'https://api.github.com/users/{username}/repos').json(),
        'username':username
    }
    return render(request,'index.html',context)

