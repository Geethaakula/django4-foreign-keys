from django.shortcuts import render, redirect
from .forms import GiftsForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
from django.views import View
from django.contrib.auth.models import User
from .models import Gifts



class Home(View):
	def get(self, request):
		form = AuthenticationForm()
		return render(request,'index.html',{'form':form})
	def post(self, request):
		form = AuthenticationForm(request, request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if(user is not None):
				login(request, user)
				return redirect("/users/")
		else:
			print(form.errors)
			return render(request,'index.html',{'form':form, "errors": form.errors})
		

class Signup(View):
	def get(self,request):
		return render(request, 'register.html', {'form':UserCreationForm()})
	
	def post(self, request):
		
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			if(user is not None):
				login(request, user)
				return redirect('/')
		else:
			form = UserCreationForm()
		
		return render(request, 'register.html', {'form': form})
	
class UsersList(View):
	def get(self,request):
		usernames = list(User.objects.filter(~Q(username=request.user.username)).filter(~Q(username="admin")))
		print(usernames)
		return render(request, 'users.html',{"usernames":usernames})
	def post(self, request):
		user = request.POST["selected_user"]
		return redirect(f"/othersgifts/{user}")
	
class Gift(View):
	def get(self,request):
		form = GiftsForm()
		gifts1 = Gifts.objects.filter(username=request.user)
		print(gifts1)
		return render(request, 'gifts.html', {'form': form, 'gifts': gifts1})
		
	def post(self, request):
		request_copy = request.POST.copy()
		request_copy.update({"username": request.user})
		form = GiftsForm(request_copy)
		gifts1 = []
		if form.is_valid():
			temp_commit = form.save(commit=False)
			temp_commit.username = request.user
			temp_commit.save()
			gifts1 = Gifts.objects.filter(username=request.user)
		return render(request, 'gifts.html', {'form': GiftsForm(), 'gifts': gifts1})
		
class OtherUserGifts(View):
	def get(self,request, username):
		userObject = list(User.objects.filter(username=username))
		# get the gifts of the user
		user_gifts = Gifts.objects.filter(username=userObject[0])
		print(user_gifts)
		return render(request, 'othersgifts.html', {"username":username, "gifts": user_gifts}) # An empty list initially
	

class Logout(View):
	def get(self, request):
		logout(request)
		return redirect("/")

