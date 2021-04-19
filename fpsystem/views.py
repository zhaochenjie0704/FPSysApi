from django.shortcuts import render 
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from rest_framework import status
from fpsystem.models import kihonjyouhou,records,permission,room,bumon
from fpsystem.serializers import KihonjyouhouSerializer,RecordsSerializer
from django.core import serializers
import json
from collections import OrderedDict
import datetime
from django.core.exceptions import ObjectDoesNotExist



#在席状況
@csrf_exempt
#def Attendance(request,room_no):
def Attendance(request):
        # 模式是GET模式数据
        if request.method == 'POST':
                #room_no = request.POST['room_no']
                room_no = request.POST.get('room_no')
                #return HttpResponse(room_no)
                books = []
                try:
                        queryset=kihonjyouhou.objects.all().filter(ROOM_NO=room_no)
                except kihonjyouhou.DoesNotExist: 
                        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
                if queryset.count() == 0:
                        return HttpResponse("kihonjyouhou No data",status=status.HTTP_404_NOT_FOUND)
                record = []
                for data in queryset:
                        records_querySet=records.objects.all().filter(EMPLOYEEID=data.EMPLOYEEID).order_by('No')
                        if records_querySet.count() == 0:
                                return HttpResponse("No data",status=status.HTTP_404_NOT_FOUND)
                        for record_querySet in records_querySet:
                                situation=''
                                if record_querySet.KUBUN == '1':
                                        situation='commuting'
                                elif record_querySet.KUBUN == '2':
                                        situation='Leave work'
                                
                                #time=datetime(record_querySet.DAKOKU_TIME,tzinfo=<DstTzInfo 'Asia/Tokyo' JST+9:00:00 STD>)
                                record_dict = OrderedDict([
                                        ('NO', record_querySet.No),
                                        ('employeeid', record_querySet.EMPLOYEEID),
                                        ('dakoku_time', utc_to_jst(record_querySet.DAKOKU_TIME.strftime('%Y-%m-%d %H:%M:%S.%f%z'))),
                                        ('kubun', record_querySet.KUBUN),
                                        ('situation', situation)
                                ])
                                record.append(record_dict)

                        for room_querySet in room.objects.all().filter(ROOM_NO=data.ROOM_NO):
                                room_dict = OrderedDict([
                                        ('id', room_querySet.id),
                                        ('room_no', room_querySet.ROOM_NO),
                                        ('room_name', room_querySet.ROOM_NAME)
                                ])
                                record.append(room_dict)

                        for bumon_querySet in bumon.objects.all().filter(DEPARTMENT_CODE=data.DEPARTMENT_CODE):
                                bumon_dict = OrderedDict([
                                        ('id', bumon_querySet.id),
                                        ('department_code', bumon_querySet.DEPARTMENT_CODE),
                                        ('department_name', bumon_querySet.DEPARTMENT_NAME)
                                ])
                                record.append(bumon_dict)

                        kihonjyouhous=OrderedDict([
                                        ('employeeid', data.EMPLOYEEID),
                                        ('name', data.NAME),
                                        ('sex', data.SEX),
                                        ('birthday', data.BIRTHDAY),
                                        ('jobgradw', data.JOBGRADE),
                                        ('status', data.STATUS),
                                        ('role', data.ROLE_ID),
                                        ('capture', data.CAPTURE),
                                        ('room_no', data.ROOM_NO),
                                        ('department_code', data.DEPARTMENT_CODE),
                                        ('record', record_dict),
                                        ('room', room_dict),
                                        ('bumon', bumon_dict)
                                ])
                        books.append(kihonjyouhous)
                #kihonjyouhou_serializer = KihonjyouhouSerializer(queryset, many=True)
                #qs_json = serializers.serialize('json', records)
                
                books = sorted(books, key=lambda k: k['record']['kubun'], reverse=False)
                data = OrderedDict([ ('result', books) ])
                json_str = json.dumps(data, ensure_ascii=False, indent=2)
        
                return HttpResponse(json_str, content_type='application/json')
        else:
                return HttpResponse('Wrong method')

#ログイン権限チェック
@csrf_exempt
def Login(request):
    #if request.method == 'CheckLoginMember':
    #    queryset=kihonjyouhou.objects.select_related('permission').get(EMPLOYEEID=EmployeeID,PASSWORD=Password)
    #    return JsonResponse(queryset.data)
        if request.method == 'POST':
                employeeID = request.POST.get('employeeID')
                password = request.POST.get('password')
                #return HttpResponse(employeeID)
                try:
                        queryset=kihonjyouhou.objects.all().filter(EMPLOYEEID=employeeID)
                except kihonjyouhou.DoesNotExist: 
                        return HttpResponse("kihonjyouhou DoesNotExist",status=status.HTTP_404_NOT_FOUND)
                if queryset.count() == 0:
                        return HttpResponse("kihonjyouhou has No data",status=status.HTTP_404_NOT_FOUND)

                try:
                        permission_querySet=permission.objects.all().filter(EMPLOYEEID=employeeID)
                except permission.DoesNotExist: 
                        return HttpResponse("permission DoesNotExist",status=status.HTTP_404_NOT_FOUND)

                if permission_querySet.count() == 0:
                        return HttpResponse("permission has No data",status=status.HTTP_404_NOT_FOUND)

                try:
                        permission_pass_querySet=permission.objects.all().filter(EMPLOYEEID=employeeID,PASSWORD=password)
                except permission.DoesNotExist: 
                        return HttpResponse("permission DoesNotExist",status=status.HTTP_404_NOT_FOUND)

                if permission_pass_querySet.count() == 0:
                        return HttpResponse("password is incorrect",status=status.HTTP_404_NOT_FOUND)

                permission_dict = OrderedDict([
                                ('employeeid', permission_pass_querySet.first().EMPLOYEEID),
                                ('modified_ymd', permission_pass_querySet.first().MODIFIED_YMD.strftime('%Y-%m-%d')),
                                ('expired_days', permission_pass_querySet.first().EXPIRED_DAYS),
                                ('role_id', permission_pass_querySet.first().ROLE_ID),
                                ('role_name', permission_pass_querySet.first().ROLE_NAME)
                        ])
                
                data = OrderedDict([ ('result', permission_dict) ])
                json_str = json.dumps(data, ensure_ascii=False, indent=2)
                return HttpResponse(json_str, content_type='application/json')
        else:
                return HttpResponse('Wrong method')

def utc_to_jst(timestamp_utc):
    datetime_utc = datetime.datetime.strptime(timestamp_utc , "%Y-%m-%d %H:%M:%S.%f%z")
    datetime_jst = datetime_utc.astimezone(datetime.timezone(datetime.timedelta(hours=+9)))
    timestamp_jst = datetime.datetime.strftime(datetime_jst, '%Y-%m-%d %H:%M:%S.%f')
    return timestamp_jst

