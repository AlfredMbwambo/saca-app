from home.models import User
from home.models import University
from home.models import Apply
from home.models import Course
from home.models import Course_price
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

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['univ_name']   

  #price
class Course_priceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_price
        fields = ['course_price','year_study']
  #end
  #price
class Course_priceSerializer(serializers.ModelSerializer):
    course = CourserSerlializer()
    university = UniversitySerializer() 
    class Meta:
        model = Course_price
        fields = ['course','university','course_price','year_study']
  #end
#end          
#to get university name and specific courses

#search university detail
class UnivSearchSerializer(serializers.ModelSerializer):
    course = CourserSerlializer()
    
    class Meta:
        model = University
        fields = ['course','univ_name']

#end university detail

#searchcourse start
class CourseSearchSerlializer(serializers.ModelSerializer):
    course = CourserSerlializer()

    class Meta:
        model = University
        fields = ['course','univ_name']
#end searchcourse

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

      

