from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from subby.models.rating import Rating
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()


def list_user_rating(request):
    if request.method == 'POST':
        ratings = Rating.objects.filter(user_id=request.POST['listerid'])
        lister = User.objects.get(id=request.POST['listerid'])
        raters = []
        for rating in ratings:
            rater = User.objects.get(id=rating.user_id)
            raters.append(rater.email)
        return render(request, 'rating/rating_list.html', {'ratings': ratings, 'raters': raters, 'lister': lister})
    else:
        return render(request, 'sublet/sublet_detail.html')

@login_required(login_url="/signup/")
def write_review(request):
    if request.method == 'POST':
        if request.POST['rating'] and request.POST['comment']:
            print(request.POST['reviewedid'])
            Rating.objects.create_rating(float(request.POST['rating']), request.POST['comment'], request.user.id,
                                         request.POST['reviewedid'])
            ratings = Rating.objects.filter(user_id=request.POST['reviewedid'])
            lister = User.objects.get(id=request.POST['reviewedid'])
            raters = []
            for rating in ratings:
                rater = User.objects.get(id=rating.user_id)
                raters.append(rater.email)
            return render(request, 'rating/rating_list.html',
                          {'ratings': ratings,
                           'raters': raters,
                           'lister': lister,
                           'success': 'You have successfully left a review!'})
        else:
            ratings = Rating.objects.filter(user_id=request.POST['reviewedid'])
            lister = User.objects.get(id=request.POST['reviewedid'])
            raters = []
            for rating in ratings:
                rater = User.objects.get(id=rating.user_id)
                raters.append(rater.email)
            return render(request, 'rating/rating_list.html',
                          {'ratings': ratings,
                           'raters': raters,
                           'lister': lister,
                           'error': 'Please fill in all fields when leaving a review.'})
    else:
        return redirect('subby:RatingList')
