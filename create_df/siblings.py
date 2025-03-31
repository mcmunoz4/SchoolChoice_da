'''
(type:Dataframe) Default=None. Archivo indicando las relaciones familiares entre postulantes. Es necesario solo en el caso de indicar 'sibling_priority_activation'=True como kwarg. Esta base debe incluir las siguientes columnas:

applicant_id: Corresponde a un id de postulante.
sibling_id: Corresponde a un id de postulante.
Para cada estudiante (applicant_id) habrá una fila por cada hermana/o (sibling_id). Se espera que cada relación de parentesco esté duplicada, es decir para A y B hermanas/os, tendremos las tuplas (applicant_id=A,sibling_id=B) y (applicant_id=B,sibling_id=A).

Ejemplo:

applicant_id	sibling_id
'Applicant_1'	'Applicant_2'
'Applicant_2'	'Applicant_1'
'Applicant_5'	'Applicant_83'
'Applicant_83'	'Applicant_5'
...	

'''