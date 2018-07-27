from django.http import Http404

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.db import models
from django.views.generic import ListView, DetailView
from subby.models.favourite import Favourite
from subby.models.sublet import Sublet
from subby.models.image import SubletImage
from subby.decorators.loginrequiredmessage import message_login_required


class FavouritesLister(ListView):
    model = Favourite

    def index(self):

        all_favourites = Favourite.objects.filter(user=self.user)
        images = []
        for f in all_favourites:
            image = SubletImage.objects.filter(sublet=f.id)
            images.append(image[0].image.url)
        ctx = {'all_favourites': all_favourites, 'cover': images}
        return render(self, 'favourite/favourites_list.html', ctx)



class FavouriteMenuBar(ListView):
    def index(request):
        all_favourites = Favourite.objects.all()
        ctx = {'all_favourites': all_favourites}

        return render(request, 'favourite/listings.html', ctx)


@message_login_required
def favourite_sublet(request):

    if(request.GET.get('favbtn')):
        Favourite.objects.create_favourite(request.sublet.id, request.user.id)



