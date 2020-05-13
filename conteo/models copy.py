from django.db import models

# Create your models here.
class Paciente(models.Model):
    fecha = models.DateField(null=True, blank=True)
    origen = models.PositiveSmallIntegerField()
    sector = models.PositiveSmallIntegerField()
    entidad_um = models.PositiveSmallIntegerField()
    sexo = models.PositiveSmallIntegerField()
    entidad_nac = models.PositiveSmallIntegerField()
    entidad_res = models.PositiveSmallIntegerField()
    municipio_res = models.PositiveSmallIntegerField()
    tipo_paciente = models.PositiveSmallIntegerField()
    fecha_ingreso = models.DateField(null=True, blank=True)
    fecha_sintomas = models.DateField(null=True, blank=True)
    fecha_def = models.DateField(null=True, blank=True)
    intubado = models.PositiveSmallIntegerField()
    neumonia = models.PositiveSmallIntegerField()
    edad = models.PositiveSmallIntegerField()
    nacionalidad = models.PositiveSmallIntegerField()
    embarazo = models.PositiveSmallIntegerField()
    habla_lengua_indig = models.PositiveSmallIntegerField()
    diabetes = models.PositiveSmallIntegerField()
    epoc = models.PositiveSmallIntegerField()
    asma = models.PositiveSmallIntegerField()
    inmusupr = models.PositiveSmallIntegerField()
    hipertension = models.PositiveSmallIntegerField()
    otra_com = models.PositiveSmallIntegerField()
    cardiovascular = models.PositiveSmallIntegerField()
    obesidad = models.PositiveSmallIntegerField()
    renal_cronica = models.PositiveSmallIntegerField()
    tabaquismo = models.PositiveSmallIntegerField()
    otro_caso = models.PositiveSmallIntegerField()
    resultado = models.PositiveSmallIntegerField()
    migrante = models.PositiveSmallIntegerField()
    pais_nacionalidad = models.CharField(max_length=100, null=False, blank=False)
    pais_origen = models.CharField(max_length=100, null=False, blank=False)
    uci = models.PositiveSmallIntegerField()

class Origen(models.Model):
    clave = models.PositiveSmallIntegerField()
    descripcion = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
		return u"{}".format(self.descripcion)

class Sector(models.Model):
    clave = models.PositiveSmallIntegerField()
    descripcion = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
		return u"{}".format(self.descripcion)

class Sexo(models.Model):
    clave = models.PositiveSmallIntegerField()
    descripcion = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
		return u"{}".format(self.descripcion)

class TipoPaciente(models.Model):
    clave = models.PositiveSmallIntegerField()
    descripcion = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
		return u"{}".format(self.descripcion)

class CatSiNo(models.Model):
    clave = models.PositiveSmallIntegerField()
    descripcion = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
		return u"{}".format(self.descripcion)

class Nacionalidad(models.Model):
    clave = models.PositiveSmallIntegerField()
    descripcion = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
		return u"{}".format(self.descripcion)

class Resultado(models.Model):
    clave = models.PositiveSmallIntegerField()
    descripcion = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
		return u"{}".format(self.descripcion)

class Resultado(models.Model):
    clave = models.PositiveSmallIntegerField()
    descripcion = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
		return u"{}".format(self.descripcion)

class Entidad(models.Model):
    clave = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100, null=False, blank=False)
    abreviatura = models.CharField(max_length=2, null=False, blank=False)

    def __str__(self):
        return u"{}".format(self.descripcion)

class Municipio(object):
    clave = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=100, null=False, blank=False)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)

    def __str__(self):
        return u"{}".format(self.nombre)

