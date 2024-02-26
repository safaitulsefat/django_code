from django.contrib import admin
from first_app.models import StudentModel,StudentInfoModel,TeacherInfoModel,EmployeeModel,ManagerModel,Friend,Me,Passport,Person,Post,student,teacher
# Register your models here.
admin.site.register(StudentModel)
admin.site.register(StudentInfoModel)
admin.site.register(TeacherInfoModel)

#admin.site.register(ManagerModel)

@admin.register(EmployeeModel)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','designation']
@admin.register(ManagerModel)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','designation','take_interview','hiring']
@admin.register(Friend)
class FriendModelAdmin(admin.ModelAdmin):
    list_display = ['id','school','section','attendence','hw']
@admin.register(Me)
class MeModelAdmin(admin.ModelAdmin):
    list_display = ['id','school','section','attendence','hw']

@admin.register(Person)
class MeModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','email']

@admin.register(Passport)
class MeModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','pass_num','page','validaty']

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','post_cap','post_details']

@admin.register(student)
class studentModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','class_name']

@admin.register(teacher)
class teacherModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','subject','student_list','mobile']