import random
import statistics

num_cal = 20  
cal_min = 10
cal_max = 50
cal_examen = [random.randint(cal_min, cal_max) for _ in range(num_cal)]

promedio= statistics.mean(cal_examen)
desviacion_estandar = statistics.stdev(cal_examen)
cal_encima_prom= sum(calificacion > promedio for calificacion in cal_examen)

print("Calificaciones de Prueba:", cal_examen)
print(f"Promedio de Calificaciones: {promedio:.2f}")
print(f"Desviación Estándar: {desviacion_estandar:.2f}")
print(f"Número de Calificaciones por Encima del Promedio: {cal_encima_prom}")
