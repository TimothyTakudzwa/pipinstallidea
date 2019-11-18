from django.shortcuts import render


posts = [{
    'author': 'Timothy Ngorima',
    'title' : 'Using Flask WTF',
    'content' : 'Hey there mirai timbotaura nezve flask',
    'date_posted' : 'AUgust 24 1995',
}, 
{
    'author': 'Tafara Ngorima',
    'title' : 'Using Flask WTF',
    'content' : 'Hey there mirai timbotaura nezve flask',
    'date_posted' : 'AUgust 24 1995',
}, 
{
    'author': 'Batsirai Ngorima',
    'title' : 'Using Flask WTF',
    'content' : 'Hey there mirai timbotaura nezve flask',
    'date_posted' : 'AUgust 24 1995',
}]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')