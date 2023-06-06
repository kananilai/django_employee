from django.shortcuts import render, redirect
from .models import Employee, Department, Training
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index_page(request):
    return render(request, 'employees/employees_list.html')

def update(request, id):
    # ポストの値をそれぞれ受け取る
    if request.method == 'POST':
        name = request.POST['name']
        employee_id = request.POST['employee_id']
        department = request.POST['department']
        training = request.POST['training']
        # フィルターで更新対象のデータを取得し、updateで更新する
        Employee.objects.filter(employee_id=id).update(name=name, employee_id=employee_id, department=Department.objects.get(id=department), training=Training.objects.get(id=training))
        return redirect('/emp')
    # ポスト送信でなければ、更新前のデータを表示する
    else:
      employee= get_object_or_404(Employee, employee_id=id)
      department_list = Department.objects.all()
      training_list = Training.objects.all()
      context = {
          'employee': employee,
          'department_list': department_list,
          'training_list': training_list,
      }
      return render(request, 'employees/employees_update.html' , context)

