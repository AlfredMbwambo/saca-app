from home.models import User
from home.models import  Address
from home.models import Course
from home.models import University
from home.models import Course_price
from home.models import Scholar_ship
from home.models import Certificate
from home.models import Apply
from home.serializer import UserSerializer
from home.serializer import UniversitySerializer
from home.serializer import ApplySerializer
from home.serializer import  CourserSerlializer
from home.serializer import UnivSearchSerializer
from home.serializer import CourseSearchSerlializer
from home.serializer import Course_priceSerializer
from home.serializer import ApplicationSerializer
from home.serializer import UniversityCoursesSerializer
from django.db.models import Q

import json

import uuid
# to login admin
def admin_registration(data):
    if not User.users.filter(email=data['email']).exists():
        new_user = User()
        new_user.user_id = uuid.uuid4()
        new_user.full_name = data["full_name"]
        new_user.phone_number = data["phone_number"]
        new_user.email = data["email"]
        new_user.password = data["password"]
        new_user.birth = data["birth"]
        new_user.language = data["language"]
        new_user.save()
        return json.dumps({'code':200,
                            "msg":"User Registered"})
    else:
            return json.dumps({'code': 300,
                                "msg":"Email name arleady exist"})                            

def admin_address(data):
    new_user =  Address()
    new_user.address_id = uuid.uuid4()
    new_user.user_id = data['user_id']
    new_user.country = data['country']
    new_user.city = data['city']
    new_user.citizen_ship = data['citizen_ship']
    new_user.save()
    return json.dumps({'code':200,
                        "msg":"Admin Registered"})

def admin_login(data):
    if User.users.filter(email=data['email']).exists():
      user = User.users.get(email=data['email'])
      if user.password == data['password']:
        return json.dumps({'code': 200,
                            "full_name": user.full_name,
                            "msg": "Super_admin successfuly loing"})
      else: 
        return json.dumps({'code': 300,
                            "msg": "Incorrect password"})
    else:
        return json.dumps({'code': 300,
                             "msg": "Email is arleady exist"})                



#end admin

#to register user
def user_registration(data):
    if not User.users.filter(email=data['email']).exists():
        new_user = User()
        new_user.user_id = uuid.uuid4()
        new_user.full_name = data["full_name"]
        new_user.phone_number = data["phone_number"]
        new_user.email = data["email"]
        new_user.password = data["password"]
        new_user.birth = data["birth"]
        new_user.language = data["language"]
        new_user.save()
        return json.dumps({'code':200,
                            "msg":"User Registered"})
    else:
            return json.dumps({'code': 300,
                                "msg":"Email name arleady exist"})                            

def address(data):
    new_user =  Address()
    new_user.address_id = uuid.uuid4()
    new_user.user_id = data['user_id']
    new_user.country = data['country']
    new_user.city = data['city']
    new_user.citizen_ship = data['citizen_ship']
    new_user.save()
    return json.dumps({'code':200,
                        "msg":"Address Registered"})

def user_login(data):
    if User.users.filter(email=data['email']).exists():
      user = User.users.get(email=data['email'])
      if user.password == data['password']:
        return json.dumps({'code': 200,
                            "full_name": user.full_name,
                            "msg": "Super_admin successfuly loing"})
      else: 
        return json.dumps({'code': 300,
                            "msg": "Incorrect password"})
    else:
        return json.dumps({'code': 300,
                             "msg": "Email is arleady exist"})    
#end user

#to add corses 

def corse_name(data):
    if not Course.courses.filter(course_name=data['course_name']).exists():
        new_user = Course()
        new_user.course_id = uuid.uuid4()
        new_user.course_name = data["course_name"]
        new_user.save()
        return json.dumps({'code':200,
                            "msg":"Corse Added"})
    else:
            return json.dumps({'code': 300,
                                "msg":"Corse name arleady registered"})
#end corse

#to register university
def university(data):
  if not University.universities.filter(univ_name=data['univ_name']).exists():
    new_univ = University()
    new_univ.univ_id = uuid.uuid4()
    new_univ.univ_name = data['univ_name']
    new_univ.course_id = data['course_id']
    new_univ.save()
    return json.dumps({'code': 200,
                        "msg": "University is Added"})
  else:
    return json.dumps({'code': 300,
                        "msg": "University is arleady registered"})
#end university                                               

#to put price
def price(data):
  new_price = Course_price()
  new_price.price_id = uuid.uuid4()
  new_price.university_id = data['university_id']
  new_price.course_id = data['course_id']
  new_price.course_price = data['course_price']
  new_price.year_study = data['year_study']
  new_price.save()
  return json.dumps({'code': 200,
                     "msg": "Added Price"})

#end price

#to post scholar_ship
def scholarship(data):
  new_schol= Scholar_ship()
  new_schol.scholar_id = uuid.uuid4()
  new_schol.university_id = data['university_id']
  new_schol.course_id = data['course_id']
  new_schol.country = data['country']
  new_schol.description = data['description']
  new_schol.save()
  return json.dumps({'code': 200,
                      "msg": "Addeed scholarship"})
#end scholar_ship


#to apply scholarship
 #to post edu certificates

def certificate(data):
  level = Certificate()
  level.certificate_id = uuiduuid4()
  level.o_level = data['o_level']
  level.a_level = data['a_level']
  level.diploma = data['diploma']
  level.degree = data['degree']
  level.save()
  return json.dumps({'code': 200,
                     "msg": "certificate uploaded"})
 #end certificate

 #to post education information

def education_infor(data):
  new_infor = Apply()
  new_infor.apply_id = uuid.uuid4()
  new_infor.certificate_id = data['certificate_id']
  new_infor.school_name = data['school_name']
  new_infor.graduation_year = data['graduation_year']
  new_infor.result = data['result']
  new_infor.save()
  return json.dumps({'code': 200,
                      "msg": "uploaded"})
#end apply scholarship
#status pending and accept user application
def Status(data):
  if Apply.applies.filter(apply_id=data['apply_id']).exists():

    application_status = Apply.applies.get(apply_id=data['apply_id'])
    application_status.status = data['status']
    application_status.save()
    return json.dumps({'code': 200,
                        "msg":"status_marked"})
  else:
    return json.dumps({'code': 300,
                       "mag": "Invalid status_marked"})                      
#end status

#serializer function start
#admin start
def pull_all_user(data):
  Users = User.users.all()
  fetch_users = UserSerializer(Users,many=True).data

  return json.dumps({'code': 200, "Users": fetch_users})

def pull_all_universities(data):
  collages = University.universities.all()
  fetch_university = UniversityCoursesSerializer(collages, many=True).data

  return json.dumps({'code': 200, "Universities": fetch_university})


def pull_all_application(data):
  application = Apply.applies.all()
  fetch_application =ApplicationSerializer(application, many=True).data

  return json.dumps({'code': 200, "Applies": fetch_application})

def pull_all_course(data):
  corse = Course.courses.all()
  fetch_courses = CourserSerlializer(corse, many=True).data

  return json.dumps({'code': 200, "courses": fetch_courses})

  #to pull cource name,univ name and price provided
def pull_all_price(data):
  pric = Course_price.course_prices.all()
  fetch_price = Course_priceSerializer(pric, many=True).data

  return json.dumps({'code': 200, "price": fetch_price})


  
#End admin

#search function 
#university search
def search_university_name(data):
  query = data['univ_name']
  collage = University.universities.filter(univ_name__icontains=query)
  count = collage.count()
  Collage = UnivSearchSerializer(collage, many=True).data

  return json.dumps({'code': 200, "collage": Collage}) 
#end university search

#search course 
def search_course(data):
  query = data['course_name']
  corse = University.universities.filter(course__course_name__icontains=query)
  count = corse.count()
  Corse =  CourseSearchSerlializer(corse, many=True).data

  return json.dumps({'code': 200, "collage": Corse})  
# def search_course(data):
#   query = data['course_name']
#   corse = University.universities.filter(course__course_name__icontains=query)
#   count = corse.count()
#   Corse =  CourseSearchSerlializer(corse, many=True).data

#   return json.dumps({'code': 200, "collage": Corse})  
#end #search course 
#end search function
#serializer function end  