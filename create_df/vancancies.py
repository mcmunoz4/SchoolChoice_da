'''
(type: Dataframe) Archivo indicando los programas que serán parte del DA. Esta base debe incluir las siguientes columnas:

program_id: [int,float,str] Identificador de un programa.
quota_id: [int] Identificador de quota.
institution_id: [int,float,str] Identificador de la institución. Genera relaciones entre varios programas.
grade_id: [int] Grado (o nivel) del programa.
regular_vacancies: [int] Cantidad de vacantes de tipo regular.
special_i_vacancies: [int] (Opcional) Cantidad de vacantes de tipo especial. Se espera que i tome valores 1 hasta n, con n la cantidad de vacantes de tipo especial.
Además, cada tupla de (program_id,quota_id) debe ser única.

Ejemplo:

program_id	quota_id	institution_id	grade_id	regular_vacancies	special_1_vacancies
'Program_A'	1	'Institution_A'	1	2	0
'Program_A'	2	'Institution_A'	1	3	4
'Program_B'	1	'Institution_B'	2	5	0
'Program_C'	2	'Institution_A'	3	0	1
...		
'''