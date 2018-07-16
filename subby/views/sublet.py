from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from subby.models.sublet import Sublet
from django.shortcuts import get_object_or_404


class SubletList(ListView):
	model = Sublet
	paginate_by = 10
	# product = get_object_or_404(Sublet, pk=1)
	# product.delete()
	
	
	def get_context_data(self, **kwargs):
		ctx = super().get_context_data(**kwargs)
		print(ctx["sublet_list"])
		print(123)
		return ctx
	
	
	
	
class SubletDetail(DetailView):
	model = Sublet
	
	
	
@login_required(login_url="/signup/")
def create_sublet(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['street_address'] and request.POST['city'] and request.POST['postal_code'] and request.POST['price'] and request.POST['description'] and request.POST['lat'] and request.POST['lng']:
			sublet = Sublet()
			sublet.title = request.POST['title']
			sublet.street_address = request.POST['street_address']
			sublet.city = request.POST['city']
			sublet.postal_code = request.POST['postal_code']
			sublet.price = request.POST['price']
			sublet.description = request.POST['description']
			# sublet.front_image = request.FILES['image']
			sublet.latitude = request.POST['lat']
			sublet.longitude = request.POST['lng']
			sublet.user = request.user
			sublet.save()
			return redirect('subby:index')
		else:
			return render(request, 'sublet/create_sublet.html', {'error': 'All fields are required' })
	else:
		return render(request, 'sublet/create_sublet.html')

	
	