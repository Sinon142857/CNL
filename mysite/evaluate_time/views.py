from django.shortcuts import render
from django.shortcuts import render_to_response

def waiting(request):
    person1 = {'name':'王先生', 'phone': '23456789', 'ID':'B23456789', 'place': 1}
    person2 = {'name':'張先生', 'phone': '12345678', 'ID':'B12345678', 'place': 2}
    person3 = {'name':'林小姐', 'phone': '13579246', 'ID':'B13579246', 'place': 3}
    people = [person1,person2,person3]
    return render_to_response('evaluate_time.html',locals())