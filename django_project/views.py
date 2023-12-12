from django.shortcuts import render, redirect
from .forms import GiftsForm, AuthForm, RegisterForm
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, logout, authenticate
from .helpers import login, logout, authenticate
from django.db.models import Q
from django.views import View
# from django.contrib.auth.models import User
from .models import Gifts, MyUser



class Home(View):
	def get(self, request):
		form = AuthForm()
		return render(request,'index.html',{'form':form})
	def post(self, request):
		form = AuthForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			response = authenticate(request, username=username, password=password)
			user = response["user"]
			if(user is not None):
				request.session.set_expiry(300)
				login(request, user)
				return redirect("/users/")
		else:
			print("inside errors")
		
		return render(request,'index.html',{'form':form, "errors": "Username and password do not match"})
		

class Signup(View):
	def get(self,request):
		return render(request, 'register.html', {'form':RegisterForm()})
	
	def post(self, request):
		
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			response = authenticate(request, username=username, password=password)
			user = response["user"]
			if(user is not None):
				login(request, user)
				return redirect('/')
		else:
			form = RegisterForm()
		
		return render(request, 'register.html', {'form': form})
	
class UsersList(View):
	def get(self,request):
		if(request.session.get("username") == ""):
			return redirect("/error")
		else:
			usernames = list(MyUser.objects.filter(~Q(username=request.session.get("username"))).filter(~Q(username="admin")))
			
			return render(request, 'users.html',{"usernames":usernames})
	def post(self, request):
		user = request.POST["selected_user"]
		return redirect(f"/othersgifts/{user}")
	
class Gift(View):
	def get(self,request):
		form = GiftsForm()
		if(request.session.get("username") == ""):
			return redirect("/error")
		else:
			user = list(MyUser.objects.filter(username=request.session.get("username")))[0]
			gifts1 = Gifts.objects.filter(username=user)
			return render(request, 'gifts.html', {'form': form, 'gifts': gifts1})
		
	def post(self, request):
		user = list(MyUser.objects.filter(username=request.session.get("username")))[0]
		request_copy = request.POST.copy()
		request_copy.update({"username": user})
		form = GiftsForm(request_copy)
		gifts1 = []
		if form.is_valid():
			temp_commit = form.save(commit=False)
			temp_commit.username = user
			temp_commit.save()
			gifts1 = Gifts.objects.filter(username=user)
		return render(request, 'gifts.html', {'form': GiftsForm(), 'gifts': gifts1})
		
class OtherUserGifts(View):
	def get(self,request, username):
		userObject = list(MyUser.objects.filter(username=username))
		# get the gifts of the user
		user_gifts = Gifts.objects.filter(username=userObject[0])
		return render(request, 'othersgifts.html', {"username":username, "gifts": user_gifts}) # An empty list initially
	

class Logout(View):
	def get(self, request):
		logout(request)
		return redirect("/")

class Error(View):
	def get(self, request):
		return render(request, "error.html")