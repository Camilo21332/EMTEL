from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from apps.Trabajadores.manages import PersonaManager


    
class Persona(AbstractBaseUser):
    per_documento = models.CharField(max_length=20, primary_key=True, unique=True)
    per_nombre = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = PersonaManager()

    USERNAME_FIELD = 'per_documento'
    REQUIRED_FIELDS = ['per_nombre']

    def __str__(self):
        return self.per_nombre

    @property
    def is_staff(self):
        return self.is_admin




class VersionWindows(models.Model):
    nombre = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nombre

class VersionOffice(models.Model):
    nombre = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nombre

class Disco(models.Model):
    tipo = models.CharField(max_length=150, unique=True)  # Ejemplo: SSD, HDD

    def __str__(self):
        return self.tipo

class Procesador(models.Model):
    nombre = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    estado = models.CharField(max_length=150, unique=True)  # Ejemplo: Activo, En reparación, Dañado

    def __str__(self):
        return self.estado

class Registros(models.Model):
    nombre_apellidos = models.CharField(max_length=150)
    referencia_equipo = models.CharField(max_length=150)
    version_de_windows = models.ForeignKey(VersionWindows, on_delete=models.CASCADE)
    version_de_office = models.ForeignKey(VersionOffice, on_delete=models.CASCADE)
    disco = models.ForeignKey(Disco, on_delete=models.CASCADE)
    procesador = models.ForeignKey(Procesador, on_delete=models.CASCADE)
    tipo_De_torre = models.CharField(max_length=150)
    ram = models.PositiveIntegerField()
    referencia_licencia = models.CharField(max_length=150)
    ultimos_digitos_licencia = models.CharField(max_length=3)
    se_le_instalo_licencia = models.CharField(max_length=150)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_apellidos} - {self.referencia_equipo}"




    
    
    
class Referencia(models.Model):
    referencia = models.CharField(max_length=150)
    
    def __str__(self):
        return self.referencia


class Windows(models.Model):
    windows = models.CharField(max_length=150)
    
    def __str__(self):
        return self.windows


class Office(models.Model):
    office = models.CharField(max_length=150)
    
    def __str__(self):
        return self.office


class TipoDeDisco(models.Model):
    tipodedisco = models.CharField(max_length=150)
    
    def __str__(self):
        return self.tipodedisco
    
    
    
class MarcaDelEquipo(models.Model):
    marcadelequipo = models.CharField(max_length=150)
    
    def __str__(self):
        return self.marcadelequipo
    
    
    


class Ram(models.Model):
    ram = models.CharField(max_length=150)
    
    def __str__(self):
        return self.ram



class ReferenciasDeLicencias(models.Model):
    referenciasdelicencias = models.CharField(max_length=150)
    
    def __str__(self):
        return self.referenciasdelicencias


class UltimosDigitosDeLicencia(models.Model):
    ultimosdigitosdelicencia = models.CharField(max_length=150)
    
    def __str__(self):
        return self.ultimosdigitosdelicencia


class LicenciadosDeOffice(models.Model):
    licenciadosdeoffice = models.CharField(max_length=150)
    
    def __str__(self):
        return self.licenciadosdeoffice



class MantenimientoDeEquipo(models.Model):
    mantenimientodeequipo = models.CharField(max_length=150)
    
    def __str__(self):
        return self.mantenimientodeequipo
