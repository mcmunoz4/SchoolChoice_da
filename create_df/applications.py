'''
type:Dataframe) Archivo indicando las postulaciones de cada estudiante y la prioridad y lotería de estas. Esta base debe incluir las siguientes columnas:

applicant_id: [int,float,str] Corresponde a un id de postulante.
program_id: [int,float,str] Corresponde a un id de programa.
quota_id: [int] Corresponde a un id de cuota.
institution_id: [int,float,str] Corresponde al id de institución correspondiente al programa.
ranking_program: [int] Lugar de el programa en la postulación del postulante. Toma valores 0 a n con n la cantidad de postulaciones del postulante.
priority_profile_program: [int] Corresponde a un de los perfiles de prioridad del la asignación.
priority_number_quota: [int] Número de prioridad correspondiente al programa y quota de la postulación. Esta determinado por el perfil de prioridad.
lottery_number_quota: [float] (Opcional) Número de lotería correspondiente al programa y quota de la postulación. Debe ser un valor entre 0 y 1. Si no es ingresado, se llamará al paquete cb_lottery_maker para generar números de lotería. Los parametros para la generación de esta lotería pueden ser entregados como argumentos de la función da.
Para cada estudiante (applicant_id) habrá una fila por cada programa y cuota a las que postula, cuyo orden de postulación está indicado en la columna ranking_program. La columna lottery_number_quota es necesaria, pues el algoritmo DA no genera números de lotería.

Ejemplo:

applicant_id	program_id	quota_id	institution_id	ranking_program	priority_profile_program	priority_number_quota	lottery_number_quota
'Applicant_1'	'Program_A'	1	'Institution_A'	1	3	4	0.0124
'Applicant_1'	'Program_C'	2	'Institution_A'	2	2	3	0.4592
'Applicant_1'	'Program_A'	2	'Institution_A'	1	3	3	0.3314
'Applicant_2'	'Program_B'	1	'Institution_B'	3	1	1	0.9324
...	

'''