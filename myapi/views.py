from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse ,JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_detail(request):
    if(request.method=='GET'):
        json_data=request.body
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        id=parsed_data.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        else:
            stu=Student.objects.all()
            serializer=StudentSerializer(stu,many=True)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
    if(request.method=='POST'):
        json_data=request.body
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=parsed_data)
        if(serializer.is_valid()):
            serializer.save()
            x={'msg':'data created'}
            json_data=JSONRenderer().render(x)
            return HttpResponse(json_data,content_type='application/json')

        else:
            json_data=JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type='application/json')
    
    if(request.method=='PUT'):
        json_data=request.body
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        id=parsed_data.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=parsed_data,partial=True)
        if(serializer.is_valid()):
            serializer.save()
            x={'msg':'data updated'}
            json_data=JSONRenderer().render(x)
            return HttpResponse(json_data,content_type='application/json')

        else:
            json_data=JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type='application/json')

    if(request.method=='DELETE'):
        json_data=request.body
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        id=parsed_data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        x={'msg':'data deleted'}
        #json_data=JSONRenderer().render(x)
        #return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(x,safe=False)


def view_database(request):
    p=Student.objects.all()
    return render(request,'myapi/database.html',{'prashant':p})

# return all JSON data
def all_student_detail(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    return JsonResponse(serializer.data,safe=False)

# return specific JSON data
def specific_student_detail(request):
    stu=Student.objects.get(id=1)
    serializer=StudentSerializer(stu)
    return JsonResponse(serializer.data)