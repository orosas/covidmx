from django.shortcuts import render

from django.db.models import Max, Count, Q
from conteo.models import Paciente

from operator import itemgetter

# Resumen de contagios positivos en:
# Cuauhtémoc, Benito Juárez, Miguel Hidalgo, El Oro
#

# Conteo inicial
# 1.- Números totales de: Confirmados, Sospechosos, Defunciones a nivel nacional
# 2.- Números totales en CDMX.
# 3.- Números totales para algunos Municipios del Estado de México.
def main(request):

    # Buscar en base la última fecha, para encontrar resultados conforme a eso
    # SQL query: SELECT max(Fecha) FROM conteo_paciente;
    # Django query: ultima_fecha_registros = Paciente.objects.all().aggregate(Max('fecha'))
    qfecha_ultimo_registros = Paciente.objects.all().aggregate(Max('fecha'))
    str_ultima_fecha = str(qfecha_ultimo_registros['fecha__max'])
    # print(str_ultima_fecha)

    # Querys Casos A Nivel Nacional
    # ToDo: Un solo query para todos los resultados usando annotate(Count('resultado'))
    confirmados_nacional = Paciente.objects.filter(resultado=1).filter(fecha=str_ultima_fecha).count()
    sospechosos_nacional = Paciente.objects.filter(resultado=3).filter(fecha=str_ultima_fecha).count()
    defunciones_nacional = Paciente.objects.filter(fecha=str_ultima_fecha).filter(resultado=1).\
                            filter(fecha_def__isnull=False).count()

    # Querys. Casos en CDMX
    # ToDo: Un solo query para todos los resultados usando annotate(Count('resultado'))
    confirmados_cdmx = Paciente.objects.all().filter(resultado=1).filter(fecha=str_ultima_fecha).filter(entidad_res=9).count()
    sospechosos_cdmx = Paciente.objects.all().filter(resultado=3).filter(fecha=str_ultima_fecha).filter(entidad_res=9).count()
    defunciones_cdmx = Paciente.objects.filter(fecha=str_ultima_fecha).filter(fecha_def__isnull=False).filter(resultado=1).\
                        filter(entidad_res=9).count()


    # Django Group By (annotate) reference:
    # https://simpleisbetterthancomplex.com/tutorial/2016/12/06/how-to-create-group-by-queries.html

    # Query. Detalle CDMX

    # detalle_cdmx = Paciente.objects.filter(fecha=str_ultima_fecha).filter(entidad_res=9).\
    # values('municipio_id__nombre', 'resultado__descripcion').annotate(Count('resultado'))

    # Omar: Produce un Queryset que contiene una lista de diccionarios, con 3 items por diccionario, con los keys:
    # municipio_id__nombre. Contiene el nombre del municipio
    # resultado__descripcion. Contiene la descripción de resultado ya sea, Positivo SARS-CoV-2 o Resultado pendiente
    # resultado__count. Cuenta el número de resultados en éste caso de resultado__descripcion

    # detalle_cdmx = Paciente.objects.filter(fecha=str_ultima_fecha).filter(entidad_res=9).filter(Q(resultado=1) | Q(resultado=3)).\
    # values('municipio_id__nombre', 'resultado__descripcion').annotate(Count('resultado'))

    # Omar: Buscar solo infectados (resultado=1) para todos los municipios de la CDMX
    detalle_cdmx = Paciente.objects.filter(fecha=str_ultima_fecha).filter(entidad_res=9).filter(resultado=1).\
    values('municipio_id__nombre', 'resultado__descripcion').annotate(Count('resultado'))

    detalle_cdmx_lista = sorted(detalle_cdmx, key=itemgetter('resultado__count'), reverse=True)
    print("asdfasdfasdfas")
    print(detalle_cdmx_lista)

    # algunos_edo_mex = Paciente.objects.filter(fecha=str_ultima_fecha).filter(entidad_res=15).filter(resultado=1).\
    #                     filter(Q(municipio_id=710) | Q(municipio_id=732) | Q(municipio_id=735) | Q(municipio_id=739) | \
    #                     Q(municipio_id=779) | Q(municipio_id=708) | Q(municipio_id=943)).values('municipio_id__nombre', 'resultado__descripcion').annotate(Count('resultado'))


    algunos_edo_mex = Paciente.objects.filter(fecha=str_ultima_fecha).filter(resultado=1).\
                        filter(Q(municipio_id=710) | Q(municipio_id=732) | Q(municipio_id=735) | Q(municipio_id=739) | \
                        Q(municipio_id=779) | Q(municipio_id=708) | Q(municipio_id=943)).values('municipio_id__nombre', 'resultado__descripcion').annotate(Count('resultado'))



    algunos_edo_mex_lista = sorted(algunos_edo_mex, key=itemgetter('municipio_id__nombre'), reverse=True)


    context = {'confirmados_nacional':confirmados_nacional,
                'sospechosos_nacional':sospechosos_nacional,
                'defunciones_nacional':defunciones_nacional,
                'str_ultima_fecha': str_ultima_fecha,
                'confirmados_cdmx':confirmados_cdmx,
                'sospechosos_cdmx':sospechosos_cdmx,
                'defunciones_cdmx':defunciones_cdmx,
                'detalle_cdmx_lista': detalle_cdmx_lista,
                'algunos_edo_mex': algunos_edo_mex,
            }
    return render(request, 'conteo/main.html', context)


