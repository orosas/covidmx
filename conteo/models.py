from django.db import models

# Create your models here.
class Paciente(models.Model):
    fecha = models.DateField(null=True, blank=True)
    id_registro = models.CharField(null=False, blank=False, max_length=150)
    origen = models.ForeignKey('Origen', on_delete='SET_NULL', to_field='clave', related_name='origen')
    sector = models.ForeignKey('Sector', on_delete='SET_NULL', to_field='clave', related_name='sector')
    entidad_um = models.ForeignKey('Entidad', on_delete='SET_NULL', to_field='clave', related_name='entidadum')
    sexo = models.ForeignKey('Sexo', on_delete='SET_NULL', to_field='clave', related_name='sexo')
    entidad_nac = models.ForeignKey('Entidad', on_delete='SET_NULL', to_field='clave', related_name='entidadnac')
    entidad_res = models.ForeignKey('Entidad', on_delete='SET_NULL', to_field='clave', related_name='entidadres')
    municipio_res = models.PositiveSmallIntegerField()
    tipo_paciente = models.ForeignKey('TipoPaciente', on_delete='SET_NULL', to_field='clave', related_name='tipopaciente')
    fecha_ingreso = models.DateField(null=True, blank=True)
    fecha_sintomas = models.DateField(null=True, blank=True)
    fecha_def = models.DateField(null=True, blank=True)
    intubado = models.ForeignKey('CatSiNo', on_delete='SET_NULL', to_field='clave', related_name='intubado')
    neumonia = models.ForeignKey('CatSiNo', on_delete='SET_NULL', to_field='clave', related_name='neumonia')
    edad = models.PositiveSmallIntegerField()
    nacionalidad = models.ForeignKey('Nacionalidad', on_delete='SET_NULL', to_field='clave', related_name='nacionalidad')
    embarazo = models.ForeignKey('CatSiNo', on_delete='SET_NULL', to_field='clave', related_name='embarazo')
    habla_lengua_indig = models.ForeignKey('CatSiNo', on_delete='SET_NULL', to_field='clave', related_name='lenguaindigena')
    diabetes = models.ForeignKey('CatSiNo', on_delete='SET_NULL', to_field='clave', related_name='diabetes')
    epoc = models.ForeignKey('CatSiNo', on_delete='SET_NULL', to_field='clave', related_name='epoc')
    asma = models.ForeignKey('CatSiNo', on_delete='SET_NULL', to_field='clave', related_name='asma')
    inmusupr = models.ForeignKey('CatSiNo', on_delete='SET_NULL', to_field='clave', related_name='inmusupr')
    hipertension = models.ForeignKey('CatSiNo', on_delete='SET_NULL', to_field='clave', related_name='hipertension')
    otra_com = models.ForeignKey('CatSiNo', on_delete='SET_NULL', to_field='clave', related_name='otra_com')
    cardiovascular = models.ForeignKey('CatSiNo', on_delete='SET_NULL', to_field='clave', related_name='cardiovascular')
    obesidad = models.ForeignKey('CatSiNo', on_delete='SET_NULL', to_field='clave', related_name='obesidad')
    renal_cronica = models.ForeignKey('CatSiNo', on_delete='SET_NULL', to_field='clave', related_name='renal_cronica')
    tabaquismo = models.ForeignKey('CatSiNo', on_delete='SET_NULL', to_field='clave', related_name='tabaquismo')
    otro_caso = models.ForeignKey('CatSiNo', on_delete='SET_NULL', to_field='clave', related_name='otro_caso')
    resultado = models.ForeignKey('Resultado', on_delete='SET_NULL', to_field='clave', related_name='resultado')
    migrante = models.ForeignKey('CatSiNo', on_delete='SET_NULL', to_field='clave', related_name='migrante')
    pais_nacionalidad = models.CharField(max_length=100, null=False, blank=False)
    pais_origen = models.CharField(max_length=100, null=False, blank=False)
    uci = models.ForeignKey('CatSiNo', on_delete='SET_NULL', to_field='clave', related_name='uci')
    municipio = models.ForeignKey('Municipio', on_delete='SET_NULL', related_name='municipiosid')

    def __str__(self):
        return u"Resultado: {}. ".format(self.resultado)

class Origen(models.Model):
    clave = models.PositiveSmallIntegerField(unique=True)
    descripcion = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
        return u"{}".format(self.descripcion)

    class Meta:
        verbose_name_plural = 'Origenes'

class Sector(models.Model):
    clave = models.PositiveSmallIntegerField(unique=True)
    descripcion = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
        return u"{}".format(self.descripcion)

    class Meta:
        verbose_name_plural = 'Sectores'

class Sexo(models.Model):
    clave = models.PositiveSmallIntegerField(unique=True)
    descripcion = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
        return u"{}".format(self.descripcion)

    class Meta:
        verbose_name_plural = 'Sexos'


class TipoPaciente(models.Model):
    clave = models.PositiveSmallIntegerField(unique=True)
    descripcion = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
        return u"{}".format(self.descripcion)

    class Meta:
        verbose_name_plural = 'Tipo Pacientes'

class CatSiNo(models.Model):
    clave = models.PositiveSmallIntegerField(unique=True)
    descripcion = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
        return u"{}".format(self.descripcion)

    class Meta:
        verbose_name_plural = "Catálogo Si o No's"

class Nacionalidad(models.Model):
    clave = models.PositiveSmallIntegerField(unique=True)
    descripcion = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
        return u"{}".format(self.descripcion)

    class Meta:
        verbose_name_plural = 'Nacionalidades'


class Resultado(models.Model):
    clave = models.PositiveSmallIntegerField(unique=True)
    descripcion = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
        return u"{}".format(self.descripcion)

    class Meta:
        verbose_name_plural = 'Resultados'

class Entidad(models.Model):
    clave = models.PositiveSmallIntegerField(unique=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    abreviatura = models.CharField(max_length=4, null=False, blank=False)

    def __str__(self):
        return u"{}".format(self.nombre)

    class Meta:
        verbose_name_plural = 'Entidades'

class Municipio(models.Model):
    clave = models.PositiveSmallIntegerField(null=False, unique=False)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    entidad = models.ForeignKey('Entidad', unique=False, on_delete='SET_NULL', to_field='clave', related_name='entidadmun')

    def __str__(self):
        return u"Municipio: {}. Entidad: {}".format(self.nombre, self.entidad)

    class Meta:
        verbose_name_plural = 'Municipios'

class Resumen(models.Model):
    fecha = models.DateField(null=False, blank=False)
    entidad_res = models.ForeignKey('Entidad', on_delete='SET_NULL', to_field='clave', related_name='entidadresResumen')
    municipio = models.ForeignKey('Municipio', on_delete='SET_NULL', related_name='municipiosidResumen')
    contagiados = models.PositiveIntegerField(null=False, blank=False)
    sospechosos = models.PositiveIntegerField(null=False, blank=False)
    negativos = models.PositiveIntegerField(null=False, blank=False)
    activos = models.PositiveIntegerField(null=False, blank=False)
    recuperados = models.IntegerField(null=False, blank=False)
    defunciones_covid = models.PositiveIntegerField(null=False, blank=False)
    defunciones_no_covid = models.PositiveIntegerField(null=False, blank=False)
    intubados = models.PositiveIntegerField(null=False, blank=False)
    intubados_fallecidos = models.PositiveIntegerField(null=False, blank=False)
    sexo_mujer = models.PositiveIntegerField(null=False, blank=False)
    sexo_hombre = models.PositiveIntegerField(null=False, blank=False)
    sexo_no_especificado = models.PositiveIntegerField(null=False, blank=False)
    tipo_paciente_ambulatorio = models.PositiveIntegerField(null=False, blank=False)
    tipo_paciente_hospitalizado = models.PositiveIntegerField(null=False, blank=False)
    tipo_paciente_no_especificado = models.PositiveIntegerField(null=False, blank=False)


