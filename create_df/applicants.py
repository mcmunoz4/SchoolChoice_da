'''
(type:Dataframe) Archivo indicando a los postulantes al DA. Esta base debe incluir las siguientes columnas:

applicant_id: [int,float,str] Identificador de postulante.
grade_id: [int] Grado (o nivel) al que postula.
special_assignment: [int] (Opcional) Int de 0 a n indicando el tipo de asignación, 0 es regular. En caso de no indicar esta columna se asume que todos los postulantes son de tipo regular.
secured_enrollment_program_id: [int,float,str] (Opcional) En caso de poseer secured enrollment, corresponde a un id de programa. En caso contrario puede tomar valores None o 0.
secured_enrollment_quota_id: [int] (Opcional) En caso de poseer secured enrollment, corresponde a un id de quota. En caso contrario puede tomar valores None o 0.
applicant_characteristic_i: [Any] (Opcional) Columnas con caracteristicas relevantes para alterar el orden de postulacion a quotas.Se espera que i tome valores 1 hasta n, con n la cantidad de caracteristicas. Estas columnas pueden tomar cualquier tipo de valores (ej: int, float, str) siempre y cuando sean consistente con los requisitos expuestos en datafram Quota_order explicado más adelante.
Además, cada applicant_id debe ser único. Se asume que special assignment se procesa antes en cada grado y en orden 1 a n.

Ejemplo:

applicant_id	grade_id	special_assignment	secured_enrollment_program_id	secured_enrollment_quota_id
'Applicant_1'	1	0	0	0
'Applicant_2'	2	0	'Program_B'	1
'Applicant_3'	1	1	0	0
'Applicant_4'	2	0	0	0
...	
'''