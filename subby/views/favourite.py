from django.http import Http404

from django.http import HttpResponse, Http404 
from django.shortcuts import render, get_object_or_404,redirect
from django.db import models
from django.views.generic import ListView, DetailView
from subby.models.favourite import Favourite
from subby.models.sublet import Sublet
from subby.models.image import SubletImage
from subby.decorators.loginrequiredmessage import message_login_required




	
@message_login_required
def FavouriteLister(request, user_id):
	fav_list = Favourite.objects.filter(user=request.user)
	
	image_dict = {}
	image_list = []
	for fav in fav_list:
		images = SubletImage.objects.filter(sublet=fav.sublet)
		image_dict = images[0]
		image_list.append(images[0])
	fav_dict = {
		'fav_list':fav_list,
		'image_dict':image_dict,
		'image_list':image_list,
	}
	return render(request, 'favourite/favourite_list.html', fav_dict)
    



class FavouriteMenuBar(ListView):
    def index(request):
        all_favourites = Favourite.objects.all()
        ctx = {'all_favourites': all_favourites}

        return render(request, 'favourite/listings.html', ctx)


# Favourites a sublet if not favourited, unfavourites a sublet if already favourited (deletes it from db)
def fav_unfav_sublet(request):

    current_user = request.user
    next = request.POST.get('next', '/')
    # Check if sublet exists
    try:
        sublet = get_object_or_404(Sublet, id=request.POST['subletid'])
    except(KeyError, Sublet.DoesNotExist):
        #return redirect('subby:SubletDetail', {'sublet': sublet, 'error': "Sublet does not exist."})
        return redirect(next, id=sublet.get_sublet_id())
    else:
        #If it exists check to see if this favourite already exists
        if(Favourite.objects.filter(user=current_user, sublet=sublet).count() > 0): #Remove favourite
            Favourite.objects.remove_favourite(sublet, current_user)
        else: #Add favourite
            Favourite.objects.create_favourite(sublet, current_user)
        return redirect(next, id=sublet.get_sublet_id())



