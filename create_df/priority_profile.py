'''

(type:Dataframe) Archivo indicando los perfiles de prioridad, indicando además las transiciones de números de prioridad para el caso de sibling dinámico.

priority_profile: [int] Número de prioridad. Se espera tome valores 1 a n, con n la cantidad de perfiles de prioridad.
priority_qi: [int] Prioridad de la quota i. Se espera que i tome valores según la cantidad de cuotas presentes.
priority_profile_sibling_transition: [int] (Opcional) Transición del perfil de prioridad en caso de recibir sibling_priority. Corresponde a uno de los perfiles de prioridad. Es necesario solo en el caso de indicar 'sibling_priority_activation'=True como kwarg.
Ejemplo:

priority_profile	priority_q1	priority_q2	priority_profile_sibling_transition
1	3	3	5
2	3	2	3
3	1	2	3
4	2	2	5
...			
'''
