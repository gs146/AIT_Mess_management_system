from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import user

from django.contrib.auth.models import User,auth
from django.contrib import messages

from .models import select_food, mon, tue,wed, thu, fri,sat


def select_food(request):
    if request.method == "POST":
        mon_breakfast = request.POST.get('mon_breakfast')
        mon_lunch = request.POST.get('mon_lunch')
        mon_snacks = request.POST.get('mon_snacks')
        mon_dinner = request.POST.get('mon_dinner')
        print("mon:",mon_breakfast)
        print(mon_lunch)
        print(mon_snacks)
        print(mon_dinner) 


        tue_breakfast = request.POST.get('tue_breakfast')
        tue_lunch = request.POST.get('tue_lunch')
        tue_snacks = request.POST.get('tue_snacks')
        tue_dinner = request.POST.get('tue_dinner')
        print("tue:",tue_breakfast)
        print(tue_lunch)
        print(tue_snacks)
        print(tue_dinner) 

        wed_breakfast = request.POST.get('wed_breakfast')
        wed_lunch = request.POST.get('wed_lunch')
        wed_snacks = request.POST.get('wed_snacks')
        wed_dinner = request.POST.get('wed_dinner')
        print("wed:",wed_breakfast)
        print(wed_lunch)
        print(wed_snacks)
        print(wed_dinner)       

   
        thu_breakfast = request.POST.get('thu_breakfast')
        thu_lunch = request.POST.get('thu_lunch')
        thu_snacks = request.POST.get('thu_snacks')
        thu_dinner = request.POST.get('thu_dinner')
        print("thu:",thu_breakfast)
        print(thu_lunch)
        print(thu_snacks)
        print(thu_dinner) 

        fri_breakfast = request.POST.get('fri_breakfast')
        fri_lunch = request.POST.get('fri_lunch')
        fri_snacks = request.POST.get('fri_snacks')
        fri_dinner = request.POST.get('fri_dinner')
        print("fri:",fri_breakfast)
        print(fri_lunch)
        print(fri_snacks)
        print(fri_dinner)
        
        sat_breakfast = request.POST.get('sat_breakfast')
        sat_lunch = request.POST.get('sat_lunch')
        sat_snacks = request.POST.get('sat_snacks')
        sat_dinner = request.POST.get('sat_dinner')
        print("sat:",sat_breakfast)
        print(sat_lunch)
        print(sat_snacks)
        print(sat_dinner) 

                    
    return redirect('/mj/')


# Create your views here.
def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        
        user = auth.authenticate(request, username = name, password= password)
        print(user)
        if user is not None:
            auth.login(request, user)
            print("done")
            return render(request, 'select_food.html')
            
        else:            
            print("firdt")
            messages.info(request, "Invalid credentials")
            return redirect('login')

    else:
        print("second")
        return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email_id = request.POST['email_id']
        password = request.POST['password']

        user = User.objects.create_user(username = name, email = email_id, password = password)
        user.save()
        print(name)
        # return HttpResponse("Hello, world. You're at the polls index.")
        return render(request, 'select_food.html')
    else:
        return render(request, 'register.html')
    


def logout(request):
    auth.logout(request)
    return redirect('/mj' )







