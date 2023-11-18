import datetime
from django.views import View
# from django_project.models import Region,Input
from django.shortcuts import render
from .forms import TicketForm 
from .models import Input,Region
regions=list(Region.objects.all())

# class Home(View):
#     def get(self,request):
        
#         return render(request,'index.html',{"regions": regions})

#     def 

#     def post(self,request):
#         a = Region.objects.get(name=request.POST["location"])
        
#         times = datetime.datetime.strptime(request.POST['geetha'], '%Y-%m-%dT%H:%M')
        
#         ticketInfo = Input(time= times, address=request.POST["StreetAddress"],region= a, day = times.strftime("%A"))
        
        
#         ticketInfo.save()
        
#         return render(request, "index.html", {'regions': regions})

class Home(View):
	def get(self, request):
		return render(request,'index.html',{"form":TicketForm()})
	def post(self, request):
		currDate = datetime.datetime.strptime(request.POST['time'],'%Y-%m-%dT%H:%M')
		currDay = currDate.strftime('%A')
		
		requestCopy = request.POST.copy()
		requestCopy.update({'day':currDay})

		form = TicketForm(requestCopy)
		if form.is_valid():
			form.save()
		return render(request, 'index.html', {'regions':regions, 'form': TicketForm()})

    
class History(View):
    def get(self,request):
        return render(request, 'history.html', {'regions': regions, 'tickets': []})  # An empty list initially
    
    def post(self, request):
        region_name = request.POST["location"]
        day_of_week = request.POST["day"]
        b=list(Region.objects.filter(name=region_name))[0]
        tickets = Input.objects.filter(region=b, day=day_of_week)
        print(tickets)
        return render(request, 'history.html', {'regions': list(regions), 'tickets': list(tickets)})
        