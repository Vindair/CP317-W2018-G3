from django.views.generic import ListView, DetailView

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
	
	
	
	
	
	
	