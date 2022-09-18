from django.db import models

# Create your models here.

class Empresa(models.Model):
    ID=models.CharField(max_length=25,primary_key=True)
    Nombre=models.TextField(max_length=100,unique=True,null=False)
    NIT=models.IntegerField(null=False)
    Ciudad=models.TextField(max_length=100)
    Direccion=models.TextField(max_length=100)
    Telefono=models.CharField(max_length=50)
    SectorProductivo=models.CharField(max_length=50)
    FechaCreacion=models.DateField()
    
class Empleados(models.Model):
    IDemp=models.IntegerField(max_length=50,primary_key=True)
    Nombre=models.CharField(max_length=50)
    Apellido=models.CharField(max_length=100)
    Email=models.EmailField(unique=True)
    Telefono=models.CharField(max_length=20)
    Empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE)
    FechaCreacion=models.DateField()
    
class Usuarios(models.Model):
    UserName=models.CharField(max_length=50,primary_key=True)
    IDuser=models.ForeignKey(Empleados, on_delete=models.CASCADE)
    Password=models.CharField(max_length=50)
    Empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE)
    Email=models.EmailField(unique=True)
    Roll=models.TextField(max_length=50)
    FechaCreacion=models.DateField()
    
class Transferencias(models.Model):
    IDT=models.AutoField(max_length=100,primary_key=True)
    FechaTransaccion=models.DateField(auto_now=True)
    Concepto=models.TextField(max_length=1000)
    Monto=models.IntegerField(max_length=100)
    Usuario=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    TipoTransferencia=models.CharField(max_length=100)
