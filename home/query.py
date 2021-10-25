from home.models import User
from home.models import  Address
from home.models import Course
from home.models import University
from home.models import Course_price
from home.models import Scholar_ship
from home.models import Certificate
from home.models import Apply

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