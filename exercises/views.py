from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.forms import ModelForm

from iflex.exercises.models import ExerciseType
from iflex.members.models import Member
from iflex.muscles.models import *

from time import gmtime

# Create your views here.

EXERCISE_TYPE_DICT = {
    '0': 'Lift',
    '1': 'Cardio',
#    'Cardio': 1,
#    'Lift': 0,
}

class ExerciseTypeForm (ModelForm):
    class Meta:
        model = ExerciseType

#     type  = forms.ImageField(required=False)
#     name  = forms.CharField(required=False, widget=forms.Textarea())
#     created_by = 
#     muscle_groups = 

def default (request):
    # TO-DO: figure out what the 'append' equivalent for dicts is
    # TODO: figure out wha the quickest cleanest way to show the 
    # values defined in choices for a queryset is
#    et_set = ExerciseType.objects.all()
    obj_dict = {
        'exercise_type_form': ExerciseTypeForm(),
        'exercise_list': ExerciseType.objects.all(),
        }
    if request.GET:
        obj_dict['feedback'] = request.GET['feedback']
    return render_to_response('exercises/default.html', obj_dict)

# TO-DO: Figure out how to make a ternary conditional in Python
#if request.GET['feedback'] ? request.GET['feedback'] : ''

# TODO: Incorporate member_id for logged in user 
def add (request):
    # Default to Adam's profile as being the contributor
    print request.POST

    # TODO: Error checking (et_form.is_valid()), throw errors (et_form.errors), 
    # use cleaned_data, etc. i.e., form processing
    et_form = ExerciseTypeForm(request.POST)
    et_form.save()
#     ExerciseType (
# #        type = get_type_from_string (request.POST['type']),
#         type = request.POST['type'],
#         name = request.POST['name'],
#         created_by = Member.objects.get(id=request.POST['member']),
#         time_created = gmtime(),
#     ).save()
    feedback = request.POST['name'] + " added successfully."
    return HttpResponseRedirect('/exercises/?feedback=%s' % feedback)
#    return render_to_response('exercises/default.html', obj_dict)
    
def delete (request, exercise_id):
#    type_to_delete = request.POST['delete']
    exercise_type = ExerciseType.objects.get (id=exercise_id)
    feedback = exercise_type.name + " deleted successfully."
    exercise_type.delete()
    return HttpResponseRedirect('/exercises/?feedback=%s' % feedback)

def get_exercise_type(exercise_type_id):
    return EXERCISE_TYPE_DICT(exercise_type_id)

#    if exercise_type_id == '0':
#        return 'Lift'
#    elif exercise_type_id == '1':
#        return 'Cardio'

#    switch exercise_type_id:
#      case '0': return 'Lift',
#      case '1': return 'Cardio'



# TO DO: Figure out how to directly send output to response
