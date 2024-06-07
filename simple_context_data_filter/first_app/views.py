from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    # context
    data = {
        'author': 'Rahim', 
        'age': 21, 
        'lst' : [1,2,3,4,5,6,7,8,9],
        'dob' : datetime.datetime.now(),
        'value' : "",
        'description' : 'This is a Description of Python.',
        'courses' : [
            {
                'id' : 1,
                'courseName' : 'Python',
                'fee' : 12000,
            },
            {
                'id' : 2,
                'courseName' : 'SavaScript',
                'fee' : 5000,
            },
            {
                'id' : 3,
                'courseName' : 'HTML',
                'fee' : 700,
            },
            {
                'id' : 4,
                'courseName' : 'CSS',
                'fee' : 500,
            },
            {
                'id' : 5,
                'courseName' : 'C##',
                'fee' : 1000,
            },
            {
                'id' : 6,
                'courseName' : 'Django',
                'fee' : 10000,
            },
        ]
        }

    return render(request, 'first_app/home.html', context=data)
