import json
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.views import View
from .models import Datasets, CompanyGrowth, Chating, Resister
from datetime import datetime
from django.contrib.auth import login , authenticate, logout
from django.contrib.auth.models import User
from django.db.models import Sum
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
import random

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        total = Datasets.objects.all().count()
        print("total dtata", total)
        energy = Datasets.objects.filter(sector='Energy').count()
        environment = Datasets.objects.filter(sector='Environment').count()
        manufacturing = Datasets.objects.filter(sector="Manufacturing").count()
        financial = Datasets.objects.filter(sector="Financial services").count()
        data = {'total':total, 'energy':energy, 'environment':environment,
            'manufacturing':manufacturing, 'financial':financial}
        return render(request, 'dashboard.html', data)
        

def main(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        return render(request, 'upload.html')

def valuation(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        return render(request, 'upload_finance.html')

def charts(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        total = Datasets.objects.all().count()
        energy = Datasets.objects.filter(sector='Energy').count()
        environment = Datasets.objects.filter(sector='Environment').count()
        manufacturing = Datasets.objects.filter(sector="Manufacturing").count()
        financial = Datasets.objects.filter(sector="Financial services").count()
        data = {'total':total, 'energy':energy, 'environment':environment,
            'manufacturing':manufacturing, 'financial':financial}
        return render (request, 'charts.html', data)

def finance_admin(request):
    if request.user.is_anonymous:
        return redirect('login')    
    else:
        total = Datasets.objects.all().count()
        energy = Datasets.objects.filter(sector='Energy').count()
        environment = Datasets.objects.filter(sector='Environment').count()
        manufacturing = Datasets.objects.filter(sector="Manufacturing").count()
        financial = Datasets.objects.filter(sector="Financial services").count()
        comapny = CompanyGrowth.objects.filter(year=2022).values()
        data = CompanyGrowth.objects.values('profit')
        total = data.aggregate(Sum('profit'))['profit__sum']
        # print(data)
        data = CompanyGrowth.objects.all().values()
        data = {'total':total, 'energy':energy, 'environment':environment,
            'manufacturing':manufacturing, 'financial':financial, 
            'company':comapny,  'data':data}
        # data = {'company':comapny, 'total':total, 'data':data}
        return render(request, 'finance_admin.html', data)
    
def finance_matric_admin(request):
    if request.user.is_anonymous:
        return redirect('login')    
    else:
        return render(request, 'finance_matric_admin.html')

def finance(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        total = Datasets.objects.all().count()
        energy = Datasets.objects.filter(sector='Energy').count()
        environment = Datasets.objects.filter(sector='Environment').count()
        manufacturing = Datasets.objects.filter(sector="Manufacturing").count()
        financial = Datasets.objects.filter(sector="Financial services").count()
        comapny = CompanyGrowth.objects.filter(year=2022).values()
        data = CompanyGrowth.objects.values('profit')
        total = data.aggregate(Sum('profit'))['profit__sum']
        # print(data)
        data = CompanyGrowth.objects.all().values()
        data = {'total':total, 'energy':energy, 'environment':environment,
            'manufacturing':manufacturing, 'financial':financial, 
            'company':comapny,  'data':data}
        # data = {'company':comapny, 'total':total, 'data':data}
        return render(request, 'finance.html', data)

# def loginuser(request):
#     return render(request, 'login.html')

class UploadJsonView(View):
    def post(self, request, *args, **kwargs):
        try:
            
            uploaded_file = request.FILES['json_file']
            data = json.load(uploaded_file)

            for item in data:
                
                    end_year= item['end_year']
                    if end_year =="":
                        end_year = None
                    intensity=item['intensity']
                    if intensity == "":
                        intensity = None
                    sector=item['sector']
                    topic=item['topic']
                    insight=item['insight']
                    url=item['url']
                    region=item['region']
                    start_year=item['start_year']
                    if start_year=="":
                        start_year = None
                    impact=item['impact']
                    if impact == "":
                        impact = None
                    added=item['added']
                    try:
                        parsed_date = datetime.strptime(added, "%B, %d %Y %H:%M:%S")
                        added = parsed_date.strftime("%Y-%m-%d %H:%M:%S")
                    except:
                        added = None
                    published=item['published']
                    try:
                        parsed_date = datetime.strptime(published, "%B, %d %Y %H:%M:%S")
                        published = parsed_date.strftime("%Y-%m-%d %H:%M:%S")
                    except:
                        published = None
                    country=item['country']
                    relevance=item['relevance']
                    if relevance == "":
                        relevance = None
                    pestle=item['pestle']
                    source=item['source']
                    title=item['title']
                    likelihood=item['likelihood']
                    if likelihood == "":
                        likelihood = None

                    Datasets.objects.create( end_year=end_year, intensity=intensity,
                                              sector=sector, topic=topic, insight=insight,
                                              url=url, region=region, start_year=start_year,
                                              impact=impact, added=added, published=published,
                                              country=country, relevance=relevance, pestle=pestle,
                                              source=source, title=title, likelihood=likelihood
                )

            return JsonResponse({'message': 'Data uploaded successfully'}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)



class UploadFJsonView(View):
    def post(self, request, *args, **kwargs):
        try:
            uploaded_file = request.FILES['json_file']
            data = json.load(uploaded_file)

            for item in data['data']:  # Access the 'data' key in the JSON

                year = int(item['year'])
                growth = float(item['growth'])  # Assuming growth can be a float
                expenses = int(item['expenses'])
                profit = int(item['profit'])

                # Assuming CompanyGrowth is your model
                CompanyGrowth.objects.create(year=year, growth=growth, expences=expenses, profit=profit)

            return JsonResponse({'message': 'Data uploaded successfully'}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)



# def CreateUser(request):
#     if request.method == 'POST':
#         user_types = request.POST.get('user_types')
#         full_name = request.POST.get('full_name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')
        
#         # Check if email already exists
#         if User.objects.filter(email=email).exists():
#             messages.error(request, 'Email already exists.')
#             return redirect('CreateUser')
        
#         # Check if passwords match
#         if password != confirm_password:
#             messages.error(request, 'Passwords do not match.')
#             return redirect('CreateUser')
        
#         # Create the user with email as username
#         user = User.objects.create_user(username=email, email=email, password=password)
#         user.full_name = full_name
#         user.phone = phone
#         user.save()
        
#         # Assign user to group based on User_Type
#         group_name = user_types.lower()  # Convert to lowercase for consistency
#         group, created = Group.objects.get_or_create(name=group_name)
#         user.groups.add(group)
        
#         messages.success(request, 'Account created successfully. Please login.')
#         return redirect('loginuser')  # Redirect to the login page
#     else:
#         return render(request, 'registration.html')


def CreateUser(request):
    if request.method == 'POST':
        user_types = request.POST.get('user_types')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        user = User.objects.create_user(username=email, email=email, password=password)
        user.full_name = full_name
        user.phone = phone
        user.save()
        
        # Assign user to group based on User_Type
        group_name = user_types.lower()  # Convert to lowercase for consistency
        group, created = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)
        # email = request.POST.get('email')
        
        # Check if email already exists
        # if User.objects.filter(email=email).exists():
        #     messages.error(request, 'Email already exists.')
        #     return redirect('CreateUser')
        
        # Generate OTP
        otp = random.randint(100000, 999999)
        otp_expiry = timezone.now() + timedelta(minutes=5)  # OTP expires in 5 minutes
        
        # Send OTP to user's email
        send_mail(
            'Your OTP',
            f'Your OTP is {otp}. It is valid for 5 minutes.',
            '3goodarvind@gmail.com',  # Replace with your actual sender email
            [email],
            fail_silently=False,
        )
        
        # Save the user data and OTP in the session to access it in the OTP verification view
        request.session['user_data'] = {
            'email': email,
            # Include other necessary fields like full_name, phone, password, user_types
            'otp': otp,
            'otp_expiry': otp_expiry.isoformat(),
        }
        
        messages.info(request, 'OTP sent to your email. Please verify to continue.')
        
        # Redirect to OTP verification page
        return HttpResponseRedirect('verify-otp')
    else:
        return render(request, 'registration.html')



def loginuser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name__iexact='ceo').exists():  # Case-insensitive comparison
                return redirect('/')  # Redirect to the index page
            elif user.groups.filter(name__iexact='operational').exists():
                return redirect('/oprational_admin')
            elif user.groups.filter(name__iexact='financial').exists():  # Corrected group name
                return redirect('/finance_admin')
            elif user.groups.filter(name__iexact='sales_marketing').exists():
                return redirect('/marketing_admin')
            else:
                messages.error(request, 'You do not belong to any user group.')
                return redirect('/login')
        else:
            messages.error(request, 'Username and Password are incorrect.')
            return redirect('loginuser')  
    else:
        return render(request, 'login.html')


def CustomLogout(request):
    logout(request)
    return redirect('/')

def Finance_Matrics(request):
    comapny = CompanyGrowth.objects.filter(year=2022).values()
    data = CompanyGrowth.objects.values('profit')
    total = data.aggregate(Sum('profit'))['profit__sum']
    print(data)
    data = CompanyGrowth.objects.all().values()
    growth = CompanyGrowth.objects.values_list('growth', flat=True)
    data_json = json.dumps(list(growth))
    print(data_json)
    data = {'company':comapny, 'total':total, 'data':data, "data_json":data_json}
    return render (request, 'Financial_Dashboard.html', data)

def Oprational(request):
    total = Datasets.objects.all().count()
    energy = Datasets.objects.filter(sector='Energy').count()
    environment = Datasets.objects.filter(sector='Environment').count()
    manufacturing = Datasets.objects.filter(sector="Manufacturing").count()
    financial = Datasets.objects.filter(sector="Financial services").count()
    comapny = CompanyGrowth.objects.filter(year=2022).values()
    data = CompanyGrowth.objects.values('profit')
    total = data.aggregate(Sum('profit'))['profit__sum']
    print(data)
    data = CompanyGrowth.objects.all().values()
    growth = CompanyGrowth.objects.values_list('profit', flat=True)
    year = CompanyGrowth.objects.values_list('year', flat=True)
    data_json = json.dumps(list(growth))
    year = json.dumps(list(year))
    print(data_json)
    data = {'company':comapny, 'total':total, 'data':data,
            'energy':energy, 'environment':environment,
            'manufacturing':manufacturing, 'financial':financial, "data_json":data_json, 'year':year}
    
    return render(request, 'Oprational.html', data)

def Oprational_admin(request):
    total = Datasets.objects.all().count()
    energy = Datasets.objects.filter(sector='Energy').count()
    environment = Datasets.objects.filter(sector='Environment').count()
    manufacturing = Datasets.objects.filter(sector="Manufacturing").count()
    financial = Datasets.objects.filter(sector="Financial services").count()
    comapny = CompanyGrowth.objects.filter(year=2022).values()
    data = CompanyGrowth.objects.values('profit')
    total = data.aggregate(Sum('profit'))['profit__sum']
    print(data)
    data = CompanyGrowth.objects.all().values()
    growth = CompanyGrowth.objects.values_list('profit', flat=True)
    year = CompanyGrowth.objects.values_list('year', flat=True)
    data_json = json.dumps(list(growth))
    year = json.dumps(list(year))
    print(data_json)
    data = {'company':comapny, 'total':total, 'data':data,
            'energy':energy, 'environment':environment,
            'manufacturing':manufacturing, 'financial':financial, "data_json":data_json, 'year':year}
    
    return render(request, 'operational_admin.html', data)


def Marketing(request):
    return render(request, 'Marketing.html')

def marketing_admin(request):
    return render(request, 'marketing_admin.html')

def ChatRoom(request, pid):
    pid = pid
    User = get_user_model()
    users = User.objects.all()
    if request.method =="POST":
        sender = request.user.username
        recever = pid
        file = request.POST.get('file')
        chat = request.POST.get('chat')
        chatdata = Chating(sender=sender, recever=recever,file=file, chat=chat)
        chatdata.save()
        return HttpResponseRedirect(recever)
    recever = pid
    sender = request.user.username
    chatval = Chating.objects.filter(Q(sender=sender, recever=recever) | Q(sender=recever, recever=sender))
    # print(chatval)
    data = {'users':users, 'recever':recever, 'chatval':chatval}
    return render(request, 'chatroom.html', data)


def ChatRoomapp(request):
    User = get_user_model()
    users = User.objects.all()
    data = {'users':users}
    return render(request, 'chatroom.html', data)


# def verify_otp(request):
#     if request.method == 'POST':
#         user_otp = request.POST.get('otp')
#         stored_data = request.session.get('user_data')

#         if stored_data:
#             stored_otp = stored_data.get('otp')
#             otp_expiry = datetime.fromisoformat(stored_data.get('otp_expiry'))
#             current_time = timezone.now()

#             if current_time > otp_expiry:
#                 messages.error(request, 'OTP has expired. Please try again.')
#                 # Optionally, clear the stored OTP to prevent retries
#                 del request.session['user_data']
#                 return redirect('CreateUser')

#             if user_otp == stored_otp:
#                 # OTP is correct and not expired, proceed with user creation or next step
#                 messages.success(request, 'OTP verified successfully.')
                
#                 # Here, you would typically create the user account or complete the registration process
#                 # For this example, we will just redirect to a success page or similar
#                 return redirect('/')
#             else:
#                 messages.error(request, 'Invalid OTP. Please try again.')

#         else:
#             messages.error(request, 'OTP verification failed. Please start over.')
#             return HttpResponse("OTP verification failed. Please start over.")

#     else:
#         return render(request, 'verify_otp.html')

def verify_otp(request):
    if request.method=="POST":
        return redirect("/")
        essages.error(request, 'Login Now.')
    else:
        return render(request,'verify_otp.html')