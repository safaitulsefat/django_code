from django.db import models

# Create your models here.


class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=30)
    address = models.TextField()

#model inheritance
# 1.abstrct based class
# 2.multi inheritance
# 3.proxy mode


# 1.abstrct based class
class comonInfoModel(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    class Meta:
        abstract = True

class StudentInfoModel(comonInfoModel):
    roll = models.IntegerField()
    payment = models.IntegerField()

class TeacherInfoModel(comonInfoModel):
    salary = models.IntegerField()
    
# 2.multi inheritance

class EmployeeModel(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    designation = models.CharField(max_length=30)

class ManagerModel(EmployeeModel):
    take_interview = models.BooleanField()
    hiring = models.BooleanField()
    
#proxy_model
class Friend(models.Model):
    school = models.CharField(max_length=40)
    section = models.CharField(max_length=10)
    attendence = models.BooleanField()
    hw = models.CharField(max_length = 50)

class Me(Friend):
    class Meta:
        proxy = True
        ordering = ['id']
        
#one to one relationship
class Person(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self) -> str:
        return self.name
class Passport(models.Model):
    user = models.OneToOneField(to=Person,on_delete = models.CASCADE)
    pass_num = models.IntegerField()
    page = models.IntegerField()
    validaty = models.IntegerField()

#many to one
class Post(models.Model):
    user = models.ForeignKey(Person,on_delete=models.SET_NULL,null=True)
    post_cap = models.CharField(max_length=50)
    post_details = models.CharField(max_length=50)
    
#many to many
class student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    class_name= models.CharField(max_length=11)
    def __str__(self) -> str:
        return self.name
class teacher(models.Model):
    students = models.ManyToManyField(student,related_name='teacherss')
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11)
    def student_list(self):
        return ",".join(str(i) for i in self.students.all())
        

    