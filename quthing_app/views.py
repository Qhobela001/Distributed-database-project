from django.shortcuts import render
from quthing_app.models import QuthingPatientModel
from django.contrib import messages
from quthing_app.forms import PatientForms

def Showemp(request):
    showall = QuthingPatientModel.objects.all()
    return render(request, 'index.html', {'data': showall})

def Inserttemp(request):
    if request.method=="POST":
        if request.POST.get('name') and request.POST.get('age'):
            saverecord=QuthingPatientModel()
            saverecord.name=request.POST.get('name')
            saverecord.age=request.POST.get('age')
            saverecord.save()
            messages.success(request, 'Patient ' +saverecord.name+ ' is saved successfully...!')
            return render(request, 'insert.html')
    else:
        return render(request, 'insert.html')

def Editemp(request, id):
    editempobj=QuthingPatientModel.objects.get(id=id)
    return render(request, 'edit.html', {"QuthingPatientModel": editempobj})

def Updateemp(request, id):
    updateemp=QuthingPatientModel.objects.get(id=id)
    form=PatientForms(request.POST, instance=updateemp)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully...!')
        return render(request, 'edit.html', {"QuthingPatientModel": updateemp})
    
def Delemp(request, id):
    delemployee=QuthingPatientModel.objects.get(id=id)
    delemployee.delete()
    showdata=QuthingPatientModel.objects.all()
    return render(request, "index.html", {"data":showdata})
