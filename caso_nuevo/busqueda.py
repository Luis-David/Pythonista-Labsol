import caso_nuevo.datos as datos
import caso_nuevo.valida as validar
def buscar():
	resultados=[]
	with open(datos.ruta) as alumnos:
		busqueda=input("Buscar:")
		for alumno in alumnos:
			alumno=eval(alumno)
			nombreCompleto=alumno[datos.orden[0]]+" "+alumno[datos.orden[1]]+" "+alumno[datos.orden[2]]
			resultado=nombreCompleto.find(busqueda)
			if resultado!=-1:
				resultados.append(nombreCompleto)
	return tuple(resultados)
