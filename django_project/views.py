from django.shortcuts import render, redirect
from .forms import RegisterForm,LoginForm,GiftsForm
from django.db.models import Q
from django.views import View
from .models import User, Gifts



class Home(View):
	def get(self, request):
		return render(request,'index.html',{'form':LoginForm()})
	def post(self, request):
		# FIXME: do not clear the forms on incorrect usernames and passwords
		form = LoginForm(request.POST)
		# check if the username exists in the databse
		username = request.POST["username"]
		currentUser = list(User.objects.filter(username=username))
		if(len(currentUser) == 0):
			#user doesn't exist, throw an error
			return render(request, 'index.html',{'form': LoginForm(), "error": "username does not exist"})
		else:
			# user exists
			print("inside else")
			password = request.POST["password"]
			currentPass = currentUser[0].password
			# if yes, then check if the password is valid 
			if(currentPass == password):
				# password is correct, save username to session storage
				print("password is correct")
				request.session['currentUser'] = request.POST["username"]
				request.session.save()
				return redirect("/users/")
			else:
				# password is incorrect
				print("inside else of if")
				new_form_values = request.POST.copy()
				new_form_values.update({"password":""})
				form = LoginForm(new_form_values)
				#remove password values from that
				return render(request, 'index.html',{'form': form, "error": "password is incorrect"})
	
class Signup(View):
	def get(self,request):
		return render(request, 'register.html', {'form':RegisterForm()})
	
	def post(self, request):
		#TODO:  hash the password
		form = RegisterForm(request.POST)
		print(request.POST)
		if form.is_valid():
			form.save()
		
		return redirect("/")
		# return render(request, 'register.html',{'form':RegisterForm()})
	
class UsersList(View):
	def get(self,request):
		currentUser = request.session.get("currentUser")
		usernames = list(User.objects.filter(~Q(username=currentUser)))
		print(usernames)
		return render(request, 'users.html',{"usernames":usernames})
	def post(self, request):
		#TODO: render the gifts page containing the gifts of the selected user
		user = request.POST["selected_user"]
		return redirect(f"/othersgifts/{user}")
	
class Gift(View):
	def get(self,request):
		form = GiftsForm()
		gifts1 = Gifts.objects.all()
		print(gifts1)
			
		return render(request, 'gifts.html', {'form': form, 'gifts': gifts1})
		# return render(request, 'gifts.html', {"form":GiftsForm()})
	def post(self, request):
		form = GiftsForm(request.POST)
		gifts1 = Gifts.objects.all()
		# TODO: get user name from session and pass it to reqest body
		print(gifts1)
		if form.is_valid():
			form.save()
		return render(request, 'gifts.html', {'form': GiftsForm(), 'gifts': gifts1})
		
class OtherUserGifts(View):
	def get(self,request, username):
		userObject = list(User.objects.filter(username=username))
		# get the gifts of the user
		user_gifts = Gifts.objects.filter(username=userObject[0])
		print(user_gifts)
		return render(request, 'othersgifts.html', {"username":username, "gifts": user_gifts}) # An empty list initially