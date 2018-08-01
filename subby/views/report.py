from django.views.generic import ListView, DetailView
from subby.models.report import Report
from django.shortcuts import render, redirect, get_object_or_404
from subby.decorators.loginrequiredmessage import message_login_required
from subby.models.sublet import Sublet

from django.contrib.auth import get_user_model
User = get_user_model()

@message_login_required
def create_report(request, user_id, sublet_id):
	
	if request.method == 'POST':
		if request.POST['issue'] and request.POST['description']:
			user = User.objects.get(id=user_id)
			sublet = Sublet.objects.get(id=sublet_id) 

			Report.objects.create_report(user=user,
							sublet=sublet,
							issue=request.POST['issue'],
							description=request.POST['description'],
							)

			return redirect('subby:SubletDetail',sublet_id)
	
	report_dict = {
		'user_id':user_id,
		'sublet_id': sublet_id,
		}
	return render(request, 'report/report_page.html', report_dict)