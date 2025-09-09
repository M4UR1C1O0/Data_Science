# 2.Cuenta cudántos estudiantes aprobaron todas sus asignaturas (todas las notas >= 4.0).

estudiantes = [
    {"nombre": "Luis", "notas": [3.5, 4.0, 2.8]},
    {"nombre": "Ana", "notas": [4.5, 3.9, 4.1]},
    {"nombre": "Carlos", "notas": [2.8, 3.2, 3.7]},
    {"nombre": "María", "notas": [5.0, 4.8, 4.9]},
    {"nombre": "Javier", "notas": [3.1, 2.9, 3.4]},
    {"nombre": "Camila", "notas": [4.3, 4.1, 3.9]},
    {"nombre": "Diego", "notas": [2.5, 3.0, 3.2]},
    {"nombre": "Valentina", "notas": [4.8, 4.5, 4.7]},
    {"nombre": "Andrés", "notas": [3.7, 3.5, 3.9]},
    {"nombre": "Sofía", "notas": [4.9, 4.6, 5.0]},
    {"nombre": "Pedro", "notas": [2.9, 3.3, 3.0]},
    {"nombre": "Isabella", "notas": [4.4, 4.2, 4.6]},
    {"nombre": "Matías", "notas": [3.8, 3.6, 3.9]},
    {"nombre": "Fernanda", "notas": [4.7, 4.8, 4.9]},
    {"nombre": "Tomás", "notas": [3.2, 3.4, 3.1]},
    {"nombre": "Josefa", "notas": [4.0, 4.2, 3.8]},
    {"nombre": "Nicolás", "notas": [2.7, 3.0, 3.3]},
    {"nombre": "Constanza", "notas": [4.9, 4.8, 5.0]},
    {"nombre": "Sebastián", "notas": [3.4, 3.6, 3.7]},
    {"nombre": "Francisca", "notas": [4.5, 4.7, 4.3]},
    {"nombre": "Ignacio", "notas": [2.6, 3.1, 3.4]},
    {"nombre": "Catalina", "notas": [4.8, 4.9, 4.7]},
    {"nombre": "Felipe", "notas": [3.5, 3.7, 3.8]},
    {"nombre": "Antonia", "notas": [4.6, 4.4, 4.8]},
    {"nombre": "Rodrigo", "notas": [3.0, 2.9, 3.3]},
    {"nombre": "Trinidad", "notas": [4.2, 4.5, 4.1]},
    {"nombre": "Pablo", "notas": [3.6, 3.8, 3.9]},
    {"nombre": "Martina", "notas": [4.7, 4.9, 5.0]},
    {"nombre": "Gabriel", "notas": [2.8, 3.0, 3.1]},
    {"nombre": "Paula", "notas": [4.4, 4.6, 4.5]},
    {"nombre": "Ricardo", "notas": [3.2, 3.5, 3.7]},
    {"nombre": "Josefina", "notas": [4.9, 5.0, 4.8]},
    {"nombre": "Mauricio", "notas": [2.9, 3.3, 3.4]},
    {"nombre": "Daniela", "notas": [4.3, 4.1, 4.5]},
    {"nombre": "Héctor", "notas": [3.7, 3.8, 3.6]},
    {"nombre": "Alejandra", "notas": [4.8, 4.9, 5.0]},
    {"nombre": "Cristóbal", "notas": [3.4, 3.6, 3.5]},
    {"nombre": "Mónica", "notas": [4.2, 4.3, 4.4]},
    {"nombre": "Álvaro", "notas": [2.7, 3.0, 3.2]},
    {"nombre": "Patricia", "notas": [4.6, 4.7, 4.8]}
]

Notas_totales = [] 
Notas_aprobados = []

# Función para guardar notas en una lista
for estudiante in estudiantes:
    Notas = estudiante["notas"]
    Notas_totales.extend(Notas)  

# Función para aprobados sobre 4.0
for nota in Notas_totales:
    if nota >= 4.0:
        aprobados = Notas_totales.count(nota)

#print(Notas_totales)
print(f"Cantidad de notas sobre 4.0: {aprobados}")


