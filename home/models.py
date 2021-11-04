from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=50,primary_key=True)
    full_name = models.CharField(max_length=150)
    phone_number = models.IntegerField(max_length=150)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    birth = models.CharField(max_length=150)
    language = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    modifield_at = models.DateTimeField(auto_now_add=True)
    


    users = models.Manager()

    class Meta:
        db_table = "users"

class Address(models.Model):
    address_id = models.CharField(max_length=50,primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    citizenship = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    modifield_at = models.DateTimeField(auto_now=True)

    addresses = models.Manager()

    class Meta:
        db_table = "addresses"

# class Rows(models.Model):
#     row_id = models.CharField(max_length=50,primary_key=True)
#     super_user = models.CharField(max_length=150)
#     user = models.CharField(max_length=150)
#     egent = models.CharField(max_length=150)

#     rows = models.Manager()

#     class Meta:
#         db_table = "rows"        

class Course(models.Model):
    course_id = models.CharField(max_length=50,primary_key=True)
    course_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    courses = models.Manager()

    class Meta:
        db_table = "courses"        


class University(models.Model):
    univ_id = models.CharField(max_length=50,primary_key=True)
    univ_name = models.CharField(max_length=150)
    course =  models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)

    universities = models.Manager()

    class Meta:
        db_table = "universities"


class Course_price(models.Model):
    price_id = models.CharField(max_length=50, primary_key=True)
    university = models.ForeignKey(University, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    course_price = models.CharField(max_length=150)
    year_study = models.IntegerField(max_length=150)
    created_at = models.DateTimeField(auto_now=True)


    course_prices = models.Manager()

    class Meta:
        db_table = "course_prices"

class Scholar_ship(models.Model):
    scholar_id = models.CharField(max_length=50, primary_key=True)
    university = models.ForeignKey(University, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    country = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now=True)

    scholar_ships = models.Manager()

    class Meta:
        db_table = "scholar_ships"

#kuatachi vyeti 
class Certificate(models.Model):
    certificate_id = models.CharField(max_length=50, primary_key=True)
    o_level = models.CharField(max_length=150)
    a_level = models.CharField(max_length=150)
    diploma = models.CharField(max_length=150)
    degree = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now=True)
    modifield_at = models.DateTimeField(auto_now=True)


    certificates = models.Manager()

    class Meta:
        db_table = "certificates" 


#application
class Apply(models.Model):
    apply_id  = models.CharField(max_length=50, primary_key=True)
    certificate = models.ForeignKey(Certificate, on_delete=models.DO_NOTHING)
    school_name = models.CharField(max_length=150)
    graduation_year = models.CharField(max_length=150)
    result = models.CharField(max_length=150)
    status =  models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    modifield_at = models.DateTimeField(auto_now=True)


    applies = models.Manager()

    class Meta:
        db_table = "applies"





