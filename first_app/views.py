from django.shortcuts import render
import datetime

def home(request):
    d = {
        'author': 'karim',
        'age': 21,
        'father': 'abdul',
        'Mother': 'sabnur',
        'brother': 'Alom vi',
        'lst': ['bangla', 'english', 'Math'],
        'val': 'rahim',

        'list': ['My', 'Name', 'is', 'rahim'],

        'valu': '',


        'nam': [
            {'name': 'zed', 'age': 19},
            {'name': 'amy', 'age': 22},
            {'name': 'joe', 'age': 31},
        ],


        'valu': '123456789',
        'some_list': 'joy is mad',
        'date': datetime.datetime.now(),


        'courses': [
            {
                'id': 1,
                'name': 'Math',
                'fee': 3000
                
            },
            {
                'id': 2,
                'name': 'English',
                'fee': 2000
                
            },
            {
                'id': 3,
                'name': 'Bangla',
                'fee': 1000
                
            },
        ]
    }

    return render(request, 'home.html', d)
