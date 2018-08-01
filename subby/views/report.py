from django.views.generic import ListView, DetailView
from subby.models.report import Report
from django.shortcuts import render, redirect, get_object_or_404





def create_report(request, user_id, sublet_id):
	
	return render(request, 'report/report_page.html')