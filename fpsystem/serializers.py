from rest_framework import serializers 
from fpsystem.models import records
from fpsystem.models import kihonjyouhou
from fpsystem.models import bumon
from fpsystem.models import room
from fpsystem.models import permission

class RecordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = records
        fields = ('No',
                  'SAKUSEISHA',
                  'SAKUSEIYMD',
                  'KOUSINSHA',
                  'KOUSINYMD',
                  'EMPLOYEEID',
                  'DAKOKU_TIME',
                  'KUBUN')
        
class KihonjyouhouSerializer(serializers.ModelSerializer):

    class Meta:
        model = kihonjyouhou
        fields = (
                  'SAKUSEISHA',
                  'SAKUSEIYMD',
                  'KOUSINSHA',
                  'KOUSINYMD',
                  'EMPLOYEEID',
                  'NAME',
                  'SEX',
                  'BIRTHDAY',
                  'JOBGRADE',
                  'STATUS',
                  'ROLE_ID',
                  'CAPTURE',
                  'DEPARTMENT_CODE',
                  'ROOM_NO')

class BumonSerializer(serializers.ModelSerializer):

    class Meta:
        model = bumon
        fields = (
                  'SAKUSEISHA',
                  'SAKUSEIYMD',
                  'KOUSINSHA',
                  'KOUSINYMD',
                  'DEPARTMENT_CODE',
                  'DEPARTMENT_NAME'
                )

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = room
        fields = (
                  'SAKUSEISHA',
                  'SAKUSEIYMD',
                  'KOUSINSHA',
                  'KOUSINYMD',
                  'ROOM_NO',
                  'ROOM_NAME'
                )

class Permissionerializer(serializers.ModelSerializer):

    class Meta:
        model = permission
        fields = (
                  'EMPLOYEEID',
                  'PASSWORD',
                  'MODIFIED_YMD',
                  'EXPIRED_DAYS',
                  'ROLE_ID',
                  'ROLE_NAME'
                )