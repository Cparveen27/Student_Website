from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def home(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            gender=request.POST['gender'],
            course=request.POST['course'],
            marks=request.POST['marks']
        )
        return redirect('/')
    return render(request, 'add.html')


def delete_student(request, id):
    Student.objects.get(id=id).delete()
    return redirect('/')


def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.marks = request.POST['marks']
        student.save()
        return redirect('/')
    return render(request, 'update.html', {'student': student})


def topper(request):
    student = Student.objects.order_by('-marks').first()
    return render(request, 'topper.html', {'student': student})


