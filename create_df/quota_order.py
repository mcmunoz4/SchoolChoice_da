'''
(type:Dataframe) Archivo indicando el orden de postulación a las cuotas que le corresponde a distintas de perfiles de prioridad. El orden de postulaciones puede tambien depender del secured enrollment del estudiante y de caracteristicas del estudiante indicadas como 'applicant_characteristic_i' en la base de applicants. Se asume que los postulantes postulan a las cuotas en orden ascendente (1-2-3-...), salvo en los casos particulares indicados en este DataFrame.

priority_profile: [int] Corresponde a uno de los perfiles de prioridad.
secured_enrollment_indicator: (Opcional) Bool. True si el reordenamiento corresponde a un priority profile de secured enrollment. Es necesario solo en el caso de indicar 'secured_enrollment_assignment'=True como kwarg.
secured_enrollment_quota_id_criteria: (Opcional) Criterio a cumplir para aplicar el reordenamiento. Toma valores '<','>','>=','<=','==' y '!=' y sus equivalentes verbales ('le','ge','leq','geq','eq' y 'neq'). Es necesario solo en el caso de indicar 'secured_enrollment_assignment'=True como kwarg.
secured_enrollment_quota_id_value: (Opcional) Valor a comparar según el criterio anterior. Es necesario solo en el caso de indicar 'secured_enrollment_assignment'=True como kwarg.
applicant_characteristic_i_criteria: (Opcional) Criterio a cumplir para aplicar el reordenamiento. Toma valores '<','>','>=','<=','==' y '!=' y sus equivalentes verbales ('le','ge','leq','geq','eq' y 'neq').
applicant_characteristic_i_value: (Opcional) Valor a comparar según el criterio anterior. Se espera que i tome valores según la cantidad de caracteristicas de los postulantes.
order_qj: Se espera que j tome valores según la cantidad de cuotas de la asignación.
Ejemplo:

priority_profile	secured_enrollment_indicator	secured_enrollment_quota_id_criteria	secured_enrollment_quota_id_value	order_q1	order_q2
1	False	''	0	2	1
2	False	''	0	2	1
2	True	'>='	2	2	1
3	False	''	0	2	1
...	
'''