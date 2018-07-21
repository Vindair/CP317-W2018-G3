from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from subby.models.sublet101 import Sublet101
from django.shortcuts import get_object_or_404



class SubletDetail(DetailView):
	model = Sublet101

@login_required(login_url="/signup/")
def create_sublet101(request):
	if request.method == 'POST':
		sublet101.latitude = models.FloatField()
		sublet101.longitude = models.FloatField()
		sublet101.destination = models.CharField(max_length=250)
		sublet101.postal_code = models.CharField(max_length=7)
		sublet101.city = models.CharField(max_length=20)
		sublet101.created_at = models.DateTimeField(auto_now=True)
		sublet101.updated_at = models.DateTimeField(blank=True, null=True)
		sublet101.description = models.TextField()
		sublet101.title = models.CharField(max_length=50)
		sublet101.price = models.FloatField()
		sublet101.street_address = request.POST['street_address']
		sublet101.front_image = models.ImageField(upload_to='images/', null=True, blank=True)
		sublet101.user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	else:
		return render(request, 'sublet/create_sublet101.html')
