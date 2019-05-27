from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.shortcuts import render_to_response
import numpy as np

def here(request, a):
	return HttpResponse(['Mom, I am here！', '1', a])

def add(request, a, b):
	s = np.zeros((4))
	s = int(a) + int(b)
	return HttpResponse("{a} + {b} = {s}.".format(s = str(s), a = str(a), b = str(b)))

def evaluate_time(request, total_number, timeout, skip_probability, arrive_time, average_dining_time, table_number):
	skip_probability = float(skip_probability)
	average_dining_time = float(average_dining_time)
	table_number = float(table_number)
	time = [0.0 for i in range(total_number)]
	for i in range(total_number):
		if i == 0:
			time[i] = average_dining_time / table_number
		else:
			time[i] = time[i - 1] + skip_probability * timeout + (1 - skip_probability) * arrive_time
			time[i - 1] = int(time[i - 1])
	time[total_number - 1] = int(time[total_number - 1])
	return render_to_response('evaluate_time.html', locals())
'''
def calculate_time(request, number, total_number, skip_probability, average_dining_time):
	time = np.zeros((total_number)) 
	for i in range(total_number):
		if i == 0:
			time[i] = 0 
		else:
			time[i] = 1
	return HttpResponse(time)
'''
'''
def math(request, a, b):
    a = int(a)
    b = int(b)
    s = a + b
    d = a - b
    p = a * b
    q = a / b
    html = '<html>sum={s}<br>dif={d}<br>pro={p}<br>quo={q}</html>'.format(s=s,d=d,p=p,q=q)
    return HttpResponse(html)
def math(request, a, b):
	a = int(a)
	b = int(b)
	s = a + b
	d = a - b
	p = a * b
	q = a / b
	t = template.Template('<html>sum={{s}}<br>dif={{d}}<br>pro={{p}}<br>quo={{q}}</html>')
	c = template.Context({'s':s, 'd':d, 'p':p, 'q':q})
	return HttpResponse(t.render(c))
'''
'''
def math(request, a, b):
	a = int(a)
	b = int(b)
	s = a + b
	d = a - b
	p = a * b
	q = a / b
	with open('templates/math.html','r') as reader:
		t = template.Template(reader.read())
	c = template.Context({'s':s, 'd':d, 'p':p, 'q':q})
	return HttpResponse(t.render(c))

'''
'''
def math(request, a, b):
	a = int(a)
	b = int(b)
	s = a + b
	d = a - b
	p = a * b
	q = a / b
	t = get_template('math.html')
	c = template.Context({'s':s, 'd':d, 'p':p, 'q':q})
	return HttpResponse(t.render(c))
	#return HttpResponse(str(s))
'''
def math(request, a, b):
	a = int(a)
	b = int(b)
	s = a + b
	d = a - b
	p = a * b
	q = a / b
	return render_to_response('math.html',{'s':s, 'd':d, 'p':p, 'q':q})
def menu(request):
	food1 = { 'name':'番茄炒蛋', 'price':60, 'comment':'好吃', 'is_spicy':False }
	food2 = { 'name':'蒜泥白肉', 'price':100, 'comment':'人氣推薦', 'is_spicy':True }
	foods = [food1,food2]
	return render_to_response('menu.html',locals())