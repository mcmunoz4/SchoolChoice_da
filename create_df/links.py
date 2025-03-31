'''
(type:Dataframe) Default=None. Archivo indicando las postulaciones en bloque. Es necesario solo en el caso de indicar 'linked_postulation_activation'=True como kwarg. Esta base debe incluir las siguientes columnas:

applicant_id: Corresponde a un id de postulante.
linked_id: Corresponde a un id de postulante.
Para cada estudiante (applicant_id) habrá una fila por cada estudiante en postulación en bloque (linked_id). Se espera que cada relación de postulación familiar esté duplicada, es decir para A y B postulando en bloque, tendremos las tuplas (applicant_id=A, linked_id=B) y (applicant_id=B, linked_id=A).

Ejemplo:

applicant_id	linked_id
'Applicant_1'	'Applicant_2'
'Applicant_2'	'Applicant_1'
'Applicant_7'	'Applicant_22'
'Applicant_22'	'Applicant_7'
...	

'''