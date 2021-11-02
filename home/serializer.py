from home.models import User
from home.models import University
from home.models import Apply
from home.models import Course
from home.models import Certificate
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['full_name','email']
#to get all courses
class CourserSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name']
#end

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['univ_name']   
#to get university name and specific courses
class UniversityCoursesSerializer(serializers.ModelSerializer):
    course = CourserSerlializer()

    class Meta:
        model = University
        fields = ['course','univ_name']

#end 

#start application
class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = ['school_name']
#end application        


class CertificateSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['o_level']        


class ApplicationSerializer(serializers.ModelSerializer):
    certificate = CertificateSerlializer()

    class Meta:
        model = Apply
        fields = ['certificate','school_name']

      

