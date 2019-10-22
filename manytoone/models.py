from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


# patient.doctors.all()
# doctor.patients.all()
class Patient(models.Model):
    name = models.CharField(max_length=200)
    # 두번째 친구에서만 가능 
    # 중개모델 안만들어도되!!!
    doctors = models.ManyToManyField(Doctor, related_name='patients')

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
    

# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     # migrations 안해도됨
#     def __str__(self):
#         return f'{self.doctor.id}번 의사의 {self.patient.id}번 환자'
    