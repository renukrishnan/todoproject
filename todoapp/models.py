from django.db import models

# Create your models here.
# closely related to database tables.
#create table todos(id int,task_name varchar(50),status varchar(20),user varchar(25))
#create model class

class Todos(models.Model):
    task_name=models.CharField(max_length=150)
    status=models.CharField(max_length=25,default="notcompleted")
    user=models.CharField(max_length=140)
    date=models.DateField(auto_now=True)

    def __str__(self):
        return self.task_name

#python3 manage.py makemigrations-> to make or update db, a file will be generate in migrate package
#python3 manage.py migrate-> to run that file
#ORM queries for creating an object
#instead of insert query here ,
# reference_name=className(fieldname=value,fieldname=value,fieldname=value)
#reference.save()
#example
#todo=Todos(task_name="gaspayment",status="notcompleted",user="ajay")
#todo.save()

#orm query for fetching all records
#reference_name=classname.objects.all()
#example
#todos=Todos.objects.all()
#print(todos)-> to print all objects--> in shell u need to type only todos



# print todos created by user ajay
# to filter from SQlite--> refname=modelname.objects.filter(field=value)
#ex)todos=Todos.objects.filter(user="ajay")

# fetching record with id=3 from SQlite
# todos=Todos.objects.get(id=3)

#change status to completed for the todo whose id=3, update orm query with id=3 and set status=completed
#fetch objects with id=3 and then update
# todo=Todos.objects.get(id=3)
#todo.status="completed"
#todo.save()

# change task_name as gas bill for id=1
# todo=Todos.objects.get(id=1)
#todo.task_name="gas bill"
#todo.save()


# deleting an object
#first fetch that object
#todo=Todos.objects.get(id=2)
#todo.delete()
# delete object whose id=3


# to show values in a particular date
#todos=Todos.objects.filter(date__lt="2021-5-31")-->date less than it means
