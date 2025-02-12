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
    
    
    
class Procesador(models.Model):
    procesador = models.CharField(max_length=150)
    
    def __str__(self):
        return self.procesador


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
