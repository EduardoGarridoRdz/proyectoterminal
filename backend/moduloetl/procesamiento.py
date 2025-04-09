from django.http import HttpResponse
import pandas as pd
import json
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import (Estudiante, Estatus, ProEdu, Situacion, Taller, 
                     NombreTaller, Idioma, TipoIngreso, EstadoServicio,
                     ServicioSocial, PracticaProf, VinculacionAcad,
                     Ciudad, Pais, Estado)


Departamentos = ["ServiciosEscolares.xlsx", "PracticasProfesionales.xlsx",
                 "ServicioSocial.xlsx", "DesarrolloEstudiantil.xlsx",
                 "DesarrolloAdemico.xlsx", "VinculacionAcademica.xlsx",
                 "Idiomas.xlsx"]

RutaImagenes = "../../DataBase/EvidenciasServicioSocial/"

@csrf_exempt
def RecibirArchivo(request):
    if request.method == 'POST':
        try:
            # Recibir el archivo del frontend
            Archivo = request.FILES['archivo']
            # Verifica sí el archivo es de tipo Excel, en caso contrario devuelve un mensaje
            if Archivo.content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                # Verifica si el nombre del archivo coincide con el nombre de los Departamentos
                # En caso contrario devuelve un mensaje
                if Archivo.name in Departamentos:
                    # Lee el archivo como objeto panda a partir de la fila nueve
                    #skiprows=0
                    Data = pd.read_excel(Archivo, skiprows=9)
                    # Abrir la función de acuerdo al nombre del Archivo    
                    Matriculas = Menu(Archivo.name, Data)
                    
                    if Matriculas[0] == True:
                        return HttpResponse(
                            json.dumps({'status': 'success', 'message': 'Archivo recibido y procesado correctamente.'}),
                            content_type='application/json'
                        )
                    else:
                        return HttpResponse(
                        json.dumps({'status': 'error', 'message': f'Revisar la siguientes matriculas inexistentes: {Matriculas[1]}'}),
                        content_type='application/json'
                        )

                else:
                    return HttpResponse(
                        json.dumps({'status': 'error', 'message': f'Nombre {Archivo.name} no es valido, se esperaba alguno de los siguientes nombres: {Departamentos}\n'}),
                        content_type='application/json',
                        status=400
                    )
            
            else:
                return HttpResponse(
                    json.dumps({'status': 'error', 'message': 'Tipo de archivo no valido'}),
                    content_type='application/json',
                    status=400
                )
            
        except Exception as e:
            # En caso de haber un error al recibir el archivo, devuelve un mensaje indicandolo
            print("Error al procesar el archivo:", str(e))
            return HttpResponse(
                json.dumps({'status': 'error', 'message': str(e)}),
                content_type='application/json',
                status=400
            )
    
    else:
        return HttpResponse(
            json.dumps({'status': 'error', 'message': 'Método no permitido.'}),
            content_type='application/json',
            status=405
        )

"""Función que abre la función necesaria para procesar el archivo de acuerdo al nombre
INPUT: Nombre del archivo, Datos que se deben proceasr
OUTPUT: No returna ningún valor"""
def Menu(Nombre, Datos):
    Matriculas = []

    if Nombre == Departamentos[0]:
        ProcesarEstudiante(Datos)
        return True, Matriculas
    else:
        Matriculas = ComprobarEstudiante(Datos)
        if len(Matriculas) == 0:
            if Nombre == Departamentos[1]:
                ProcesarPracticas(Datos)
                return True, Matriculas
            elif Nombre == Departamentos[2]:
                ProcesarServicio(Datos)
                return True, Matriculas
            elif Nombre == Departamentos[3]:
                ProcesarTaller(Datos)
                return True, Matriculas
            elif Nombre == Departamentos[4]:
                return True, Matriculas
            elif Nombre == Departamentos[5]:
                ProcesarVinculacion(Datos)
                return True, Matriculas
            elif Nombre == Departamentos[6]:
                ProcesarIdioma(Datos)
                return True, Matriculas
        else:
            return False, Matriculas

"""Función que transforma variables categóricas a binarias
INPUT: Dato de una columna con valor categórico, Valor que se espera comparar
OUTPUT: Retorna veradero en caso de ser igual al valor esperado, en caso contrario falso"""
def TransformarBool(Variable, Valor):
    if Variable == Valor:
        return True
    return False

"""Función que comprueba que existe un estudiante registrado en la tabla de estudiantes
INPUT: Datos del archivo excel
OUTPUT: Una lista con las mátriculas que no están registradas """
def ComprobarEstudiante(Datos):
    MatriculasErroneas = []

    for index, row in Datos.iterrows():
        try:
            Estudiante.objects.get(matricula = row['matricula'])
            pass
        except Estudiante.DoesNotExist:
            MatriculasErroneas.append(row['matricula'])
    
    return MatriculasErroneas

"""Función que procesa el archivo de Servicios Escolares y añade estudiantes a la base de datos
o actualiza toda su información en caso de estar registrado
INPUT: Dataframe que contiene todos los datos del archivo de Servicios Escoalres
OUTPUT: Ningun valor, solo añade nuevos estudiantes"""
def ProcesarEstudiante(Datos):    
    for index, row in Datos.iterrows():

        # Se comprueba si ya existe un estudiante registrado
        try:
            # En caso de que existe se actualizan sus datos
            estudiante = Estudiante.objects.get(matricula = row['matricula'])
            estudiante.nombre = row['estudiante']
            estudiante.curp = row['curp']
            estudiante.direccion = row['direccion']
            estudiante.email_personal = row['email_personal']
            estudiante.telefono = row['telefono']
            estudiante.iems_procedencia = row['bach_nombre']
            estudiante.generacion = row['generacion']
            estudiante.id_tipo_ingreso = TipoIngreso.objects.get(ingreso = row['tipo_ingreso'])
            estudiante.fecha_ingreso = row['FECHA']
            estudiante.discapacidad = TransformarBool(row['discapacidad'], "Si")
            estudiante.nombre_discapacidad = row['nombre_discapacidad']
            estudiante.id_pro_edu = ProEdu.objects.get(nombre_pro_edu = row['programa'])
            estudiante.id_situacion = Situacion.objects.get(situacion = row['situacion'])
            estudiante.motivo_situacion = row['motivo_situacion']
            estudiante.id_estatus = Estatus.objects.get(estatus = row['estado'])
            estudiante.beca = TransformarBool(row['beca'], "Si")
            estudiante.tipo_beca = row['tipo_beca']
            estudiante.creditos = row['creditos']
            estudiante.derecho_servicio_social = TransformarBool(row['derecho_servicio'], "Si")
            estudiante.fecha_nac = row['fecha_nacimiento']
            estudiante.sexo = TransformarBool(row['sexo'], "M")
            estudiante.hablante_indigena = TransformarBool(row['hablante_lengua'], "Si")
            estudiante.nombre_lengua = row['lengua']
            estudiante.promedio = row['promedio'] 

            estudiante.save()
        # En caso contrario crea un nuevo estudiante
        except Estudiante.DoesNotExist:
            estudiante = Estudiante(
                matricula = row['matricula'],
                nombre = row['estudiante'],
                curp = row['curp'],
                direccion = row['direccion'],
                email_personal = row['email_personal'],
                telefono = row['telefono'],
                iems_procedencia = row['bach_nombre'],
                generacion = row['generacion'],
                id_tipo_ingreso = TipoIngreso.objects.get(ingreso = row['tipo_ingreso']),
                fecha_ingreso = row['FECHA'],
                discapacidad = TransformarBool(row['discapacidad'], "Si"),
                nombre_discapacidad = row['nombre_discapacidad'],
                id_pro_edu = ProEdu.objects.get(nombre_pro_edu = row['programa']),
                id_situacion = Situacion.objects.get(situacion = row['situacion']),
                motivo_situacion = row['motivo_situacion'],
                id_estatus = Estatus.objects.get(estatus = row['estado']),
                beca = TransformarBool(row['beca'], "Si"),
                tipo_beca = row['tipo_beca'],
                creditos = row['creditos'],
                derecho_servicio_social = TransformarBool(row['derecho_servicio'], "Si"),
                fecha_nac = row['fecha_nacimiento'],
                sexo = TransformarBool(row['sexo'], "M"),
                hablante_indigena = TransformarBool(row['hablante_lengua'], "Si"),
                nombre_lengua = row['lengua'],
                promedio = row['promedio']
            )
            estudiante.save()

"""Función que procesa el archivo de Desarrollo Estudiantil y añade los talleres que cursa cada 
estudiante a lo largo de su estancia en la universidad.
INPUT: Dataframe que contiene todos los datos del archivo de Desarrollo Estudiantil
OUTPUT: Ningun valor, solo añade los talleres"""        
def ProcesarTaller(Datos):
    for index, row in Datos.iterrows():
      
        tallerComprobacion = Taller.objects.filter(
            id_estudiante = Estudiante.objects.get(matricula = row['matricula']),
            tipo_taller = TransformarBool(row['tipo de taller'], "Artistico"),
            id_nombre_taller = NombreTaller.objects.get(nombre = row['nombre del taller']),
            representante = TransformarBool(row['representativo'], "Si"),
            selectivo = TransformarBool(row['selectivo'], "Si"),
            acreditado = TransformarBool(row['acreditado'], "Si"),
            fecha_inicio = row['fechainicio'],
            fecha_final = row['fechafinal'],
            club = row['club']
        ).exists()

        if not tallerComprobacion:
            taller = Taller(
            id_estudiante = Estudiante.objects.get(matricula = row['matricula']),
            tipo_taller = TransformarBool(row['tipo de taller'], "Artistico"),
            id_nombre_taller = NombreTaller.objects.get(nombre = row['nombre del taller']),
            representante = TransformarBool(row['representativo'], "Si"),
            selectivo = TransformarBool(row['selectivo'], "Si"),
            acreditado = TransformarBool(row['acreditado'], "Si"),
            fecha_inicio = row['fechainicio'],
            fecha_final = row['fechafinal'],
            club = row['club']
            )
            taller.save()


"""Función que procesa el archivo de Idiomas y añade el idioma que cursa el estudiante a lo largo
de su trayectoria universitaria.
INPUT: Dataframe que contiene todos los datos del archivo de Idiomas
OUTPUT: Ningun valor, solo añade los idiomas"""        
def ProcesarIdioma(Datos):
    for index, row in Datos.iterrows():

        idiomaComprobacion = Idioma.objects.filter(
            estudiante = Estudiante.objects.get(matricula = row['matricula']),
            idioma = row['idioma'],
            nivel = row['nivel'],
            acreditado = TransformarBool(row['acreditado'], "Si"),
            asesorias = TransformarBool(row['asesorias'], "Si"),
            certificacion = row['certificacion'],
            fecha_inicio = row['fechainicio'],
            fecha_final = row['fechafinal']
        ).exists()

        if not idiomaComprobacion:
            idioma = Idioma(
                estudiante = Estudiante.objects.get(matricula = row['matricula']),
                idioma = row['idioma'],
                nivel = row['nivel'],
                acreditado = TransformarBool(row['acreditado'], "Si"),
                asesorias = TransformarBool(row['asesorias'], "Si"),
                certificacion = row['certificacion'],
                fecha_inicio = row['fechainicio'],
                fecha_final = row['fechafinal']
            )
            idioma.save()


def ProcesarServicio(Datos):
    for index, row in Datos.iterrows():

        servicioSocialComprobacion = ServicioSocial.objects.filter(
            id_estudiante = Estudiante.objects.get(matricula = row['matricula']),
            id_estado = EstadoServicio.objects.get(estado = row['estado']),
            tipo_proyecto = TransformarBool(row['tipo_proyecto'], "Interno"),
            clase_proyecto = row['clase_proyecto'],
            nombre_proyecto = row['nombre_proyecto'],
            beneficiarios = row['beneficiarios'],
            fecha_inicio = row['fecha_inicio'],
            fecha_final = row['fecha_final'],
            horas_acreditadas = row['horas_acreditadas'],
            horas_pendientes = row['horas_pendientes'],
            horas_proyecto = row['horas_proyecto'],
            fecha_ultimo_reporte = row['fecha_ultimo_reporte']
        ).exists()
        
        if not servicioSocialComprobacion:
            servicioSocial = ServicioSocial(
            id_estudiante = Estudiante.objects.get(matricula = row['matricula']),
            id_estado = EstadoServicio.objects.get(estado = row['estado']),
            tipo_proyecto = TransformarBool(row['tipo_proyecto'], "Interno"),
            clase_proyecto = row['clase_proyecto'],
            nombre_proyecto = row['nombre_proyecto'],
            beneficiarios = row['beneficiarios'],
            fecha_inicio = row['fecha_inicio'],
            fecha_final = row['fecha_final'],
            horas_acreditadas = row['horas_acreditadas'],
            horas_pendientes = row['horas_pendientes'],
            horas_proyecto = row['horas_proyecto'],
            fecha_ultimo_reporte = row['fecha_ultimo_reporte']
        )
        servicioSocial.save()
        

def ProcesarPracticas(Datos):
    for index, row in Datos.iterrows():
        
        practicaComprobacion = PracticaProf.objects.filter(
            id_estudiante = Estudiante.objects.get(matricula = row['matricula']),
            num_practica = row['numero_practica'],
            fecha_inicio = row['fechainicio'],
            fecha_final = row['fechafinal'],
            empresa = row['empresa'],
            telefon_empresa = row['telefono_empresa'],
            contratado = TransformarBool(row['contratado'], "Si")
        ).exists()

        if not practicaComprobacion:
            
            practicaProfesional = PracticaProf(
                id_estudiante = Estudiante.objects.get(matricula = row['matricula']),
                num_practica = row['numero_practica'],
                fecha_inicio = row['fechainicio'],
                fecha_final = row['fechafinal'],
                empresa = row['empresa'],
                telefon_empresa = row['telefono_empresa'],
                contratado = TransformarBool(row['contratado'], "Si")
            )
            
            practicaProfesional.save()

def ProcesarVinculacion(Datos):
    for index, row in Datos.iterrows():

        estudiante = Estudiante.objects.get(matricula = row['matricula'])
        
        Acreditado = TransformarBool(row['acreditado'], "Si")
        beneficiario = TransformarBool(row['beca'], "Si")
        vinculacion = TransformarBool(row['tipo de vinculacion'], "Nacional")        
        hue = TransformarBool(row['huesped'], "Si")
        

        ciudad = comprobarCiudad(row['ciudad'], row['estado'], row['pais'])

        vinculacion = VinculacionAcad(
            id_estudiante = estudiante,
            institucion = row['institucion'],
            fecha_inicio = row['fecha inicio'],
            fecha_final = row['fecha final'],
            acreditado = Acreditado,
            beca = beneficiario,
            nombre_beca = row['nombre de la beca'],
            tipo_vinculacion = vinculacion,
            huesped = hue,
            id_ciudad = ciudad
        )

        print(vinculacion.id_ciudad.id_estado)

def comprobarCiudad(city, estate, country):

    try:
        ciudad = Ciudad.objects.get(nombre_ciudad = city)
        
    except Ciudad.DoesNotExist:
        
        try:
            estado = Estado.objects.get(nombre_estado = estate)
            pais = Pais.objects.get(nombre_pais = country)
            
            ciudad = Ciudad(
                id_estado = estado,
                id_pais = pais,
                nombre_ciudad = city
            )

            ciudad.save()
        
        except Estado.DoesNotExist:
            
            try:
                pais = Pais.objects.get(nombre_pais = country)

                estado = Estado(
                    nombre_estado = estate
                )

                estado.save()

                ciudad = Ciudad(
                    id_estado = estado,
                    id_pais = pais,
                    nombre_ciudad = city
                )

                ciudad.save()

            except:
                
                pais = Pais(
                    nombre_pais = country
                )

                pais.save()

                estado = Estado(
                    nombre_estado = estate
                )

                estado.save()

                ciudad = Ciudad(
                    id_estado = estado,
                    id_pais = pais,
                    nombre_ciudad = city
                )

                ciudad.save()                

    return ciudad