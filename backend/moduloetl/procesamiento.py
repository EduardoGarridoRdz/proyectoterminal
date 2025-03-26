from django.http import HttpResponse
import pandas as pd
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Estudiante, Estatus, ProEdu, Situacion, Taller, NombreTaller


Departamentos = ["ServiciosEscolares.xlsx", "PracticasProfesionales.xlsx",
                 "ServicioSocial.xlsx", "DesarrolloEstudiantil.xlsx",
                 "DesarrolloAdemico.xlsx", "VinculacionUniversitaria.xlsx"]

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
                return True, Matriculas
            elif Nombre == Departamentos[2]:
                return True, Matriculas
            elif Nombre == Departamentos[3]:
                ProcesarTaller(Datos)
                return True, Matriculas
            elif Nombre == Departamentos[4]:
                return True, Matriculas
            elif Nombre == Departamentos[5]:
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
            Estudiante.objects.get(matricula = row['Matricula'])
            pass
        except Estudiante.DoesNotExist:
            MatriculasErroneas.append(row['Matricula'])
    
    return MatriculasErroneas

def ProcesarEstudiante(Datos):
    for index, row in Datos.iterrows():

        # Transformar a booleanas las variables
        Discapacidad = TransformarBool(row['Discapacidad'], "No")
        Sexo = TransformarBool(row['Sexo'], "Masculino")
        HablanteLengua = TransformarBool(row['Hablante Lengua'], "Si")
        # Obtener o crear instancias de los modelos relacionados
        situacion = Situacion.objects.get(situacion = row['Situacion'])
        pro_edu  = ProEdu.objects.get(nombre_pro_edu = row['Programa Educativo'])
        estatus  = Estatus.objects.get(estatus = row['Estatus'])
        
        try:
            # Se comprueba si ya existe un estudiante registrado
            estudiante = Estudiante.objects.get(matricula = row['Matricula'])
            # Se actualizan sus datos
            estudiante.nombre = row['Nombre']
            estudiante.apellido_pat = row['Apellido Paterno']
            estudiante.apellido_mat = row['Apellido Materno']
            estudiante.fecha_nac = row['Fecha de Nacimiento']
            estudiante.sexo = Sexo
            estudiante.curp = row['CURP']
            estudiante.email_personal = row['Email Personal']
            estudiante.telefono = row['Telefono']
            estudiante.discapacidad = Discapacidad
            estudiante.nombre_discapacidad = row['Nombre Discapacidad']
            estudiante.hablante_indigena = HablanteLengua
            estudiante.nombre_lengua = row['Nombre Lengua']
            estudiante.iems_procedencia = row['IEMS Procedencia']
            estudiante.id_estatus = estatus
            estudiante.promedio = row['Promedio']
            estudiante.id_pro_edu = pro_edu
            estudiante.id_situacion = situacion
            estudiante.generacion = row['Generacion']
            estudiante.creditos = row['Creditos']        

            estudiante.save()
        
        except Estudiante.DoesNotExist:
            estudiante = Estudiante(
                matricula = row['Matricula'],
                nombre = row['Nombre'],
                apellido_pat = row['Apellido Paterno'],
                apellido_mat = row['Apellido Materno'],
                fecha_nac = row['Fecha de Nacimiento'],
                sexo = Sexo,
                curp = row['CURP'],
                email_personal = row['Email Personal'],
                telefono = row['Telefono'],
                discapacidad = Discapacidad,
                nombre_discapacidad = row['Nombre Discapacidad'],
                hablante_indigena = HablanteLengua,
                nombre_lengua = row['Nombre Lengua'],
                iems_procedencia = row['IEMS Procedencia'],
                id_estatus = estatus,
                promedio = row['Promedio'],
                id_pro_edu = pro_edu,
                id_situacion = situacion,
                generacion = row['Generacion'],
                creditos = row['Creditos'],
            )
            
            estudiante.save()
        
def ProcesarTaller(Datos):
    for index, row in Datos.iterrows():
        estudiante = Estudiante.objects.get(matricula = row['Matricula'])
        nombreTaller = NombreTaller.objects.get(nombre = row['Nombre del taller'])
                
        TipoTaller = TransformarBool(row['Tipo de taller'], "Artistico")
        Representante = TransformarBool(row['Representante'], "Si")
        Selectivo = TransformarBool(row['Selectivo'], "Si")
        Acreditado = TransformarBool(row['Acreditado'], "Si")

        taller = Taller(
            id_estudiante = estudiante,
            tipo_taller = TipoTaller,
            id_nombre_taller = nombreTaller,
            representante = Representante,
            selectivo = Selectivo,
            acreditado = Acreditado,
            club = row['Club']
        )

        taller.save()
    
#def ProcesarIdioma(Datos):

#def ProcesarServicio(Datos):

#def ProcesarPracticas(Datos):

#def ProcesarVinculacion(Datos):