from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from .helper import *

def dashboard(request):
	args = {'dashboard': dashboard}
	return render(request, 'mso/dashboard.html', args)

# New MSO
def new_mso(request):
	args = {}
	if request.method == 'POST':
		new_mso = Mso()

		new_mso.requested_by=request.POST['requested_by']
		new_mso.section = request.POST['section']
		new_mso.department_head = request.POST['department_head']
		new_mso.location = request.POST['location']
		new_mso.description_of_service = request.POST['description_of_service']
		new_mso.actual_work_descripition = request.POST['actual_work_descripition']
		new_mso.date_started = request.POST['date_started']
		new_mso.date_completed = request.POST['date_completed']
		new_mso.work_compleated_by = request.POST.getlist('work_compleated_by')

		vals = {
			'{{mso_no}}': str(int(str(Mso.objects.latest('pk')))+1).zfill(4),
			'{{tReq}}': str(datetime.utcnow()).split(' ')[1].split('.')[0],
			'{{time_comp}}': str(datetime.utcnow()).split(' ')[1].split('.')[0],
			'{{req_by}}': request.POST['requested_by'],
			'{{section}}': request.POST['section'],
			'{{dep_head}}': request.POST['department_head'],
			'{{location}}': request.POST['location'],
			'{{des_service}}': request.POST['description_of_service'],
			'{{act_work_desc}}': request.POST['actual_work_descripition'],
			'{{req_date}}': request.POST['date_started'],
			'{{date_comp}}': request.POST['date_completed'],
			'{{wrk_comp_by}}': str(request.POST.getlist('work_compleated_by')),
		}

		new_mso.g_drive_id = g_drive_mso(vals)
		# new_mso.posted_by = request.user
		# new_mso.posted_by_name = helper.get_full_name(request.user)

		# Commit to Database
		new_mso.save()

		args['msg'] = 'MSO Created Successfully!'
	else:
		# gender = helper.get_gender(request.user)
		# department = helper.get_department(request.user)
		# current_user_name = helper.get_full_name(request.user)
		# job_title = helper.get_job_title(request.user)  
		# args = {
		# 	'current_user_name': str(current_user_name),
		# 	'current_user_email': str(request.user),
		# 	'current_user_gender': str(gender),
		# 	'department': str(department),
		# 	'job_title': str(job_title),
		# 	'full_names':full_names,
		# }
		args['msg'] = ''
		args['full_names'] = ['Henok', 'Ali', 'RS']
	return render(request, 'mso/new_mso.html', args)

# All MSO's
def all_msos(request, msg=''):
	all_msos = Mso.objects.all().order_by('-pk')
	# current_user_name = helper.get_full_name(request.user)   

	# Pagination
	paginator = Paginator(all_msos, 10)

	page = request.GET.get('page')
	msos = paginator.get_page(page)
	# gender = helper.get_gender(request.user)
	# department = helper.get_department(request.user)
	# job_title = helper.get_job_title(request.user)
	args = {
		'msos': msos,
		# 'current_user_name': str(current_user_name),
		# 'current_user_email': str(request.user),
		# 'current_user_gender': str(gender),
		# 'department': str(department),
		# 'job_title': str(job_title),
		'msg': msg,
	}

	return render(request, 'mso/all_msos.html', args)
