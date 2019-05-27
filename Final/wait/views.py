from django.shortcuts import render_to_response, HttpResponse
from wait.models import person_information, parameter

def waiting_time_evaluate(request):
	parameters = parameter.objects.all()
	person_informations = person_information.objects.order_by('place')

	print(type(person_informations[0]))

	total_number = parameters[0].total_number
	timeout = parameters[0].timeout
	skip_probability = parameters[0].skip_probability
	arrive_time = parameters[0].arrive_time
	average_dining_time = parameters[0].average_dining_time
	table_number = parameters[0].table_number
	
	time = [0.0 for i in range(total_number)]
	for i in range(total_number):
		if i == 0:
			time[i] = float(average_dining_time) / float(table_number)
		else:
			time[i] = time[i - 1] + skip_probability * timeout + (1 - skip_probability) * arrive_time
			time[i - 1] = int(time[i - 1])
	time[total_number - 1] = int(time[total_number - 1])

	for i in range(1, total_number + 1):
		person_informations.filter(place=i).update(waiting_time=time[i - 1])
		target = person_informations.filter(place=i)
		target.update(waiting_time=time[i - 1])
		print('第' + str(i) + '位' + target[0].name + '先生, ID = ' + target[0].ID_number + ' 要等' + str(time[i - 1]) + '分鐘')
	#person_informations = person_information.objects.order_by('place')
	return render_to_response('waiting.html',locals())
def why(request):
	return HttpResponse('a')