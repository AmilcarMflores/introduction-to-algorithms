# Problem Desription: Tienes una lista de eventos con sus horas de inicio y fin (en formato de 24 horas). Escribe un algoritmo para determinar si alguno de los eventos se superpone.

def has_overlap(events):
  # Ordenamos los eventos por la hora de inicio
  events.sort(key  = lambda x: x['start'])
  
  for i in range(len(events) - 1):
    if events[i]['end'] > events[i + 1]['start']:
      return True
  return False

#events = [ {'start': 1, 'end': 3}, {'start': 2, 'end': 4}, {'start': 5, 'end': 7} ]
#print(has_overlap(events)) # True
events = [ {'start': 1, 'end': 3}, {'start': 4, 'end': 5}, {'start': 5, 'end': 7} ]
print(has_overlap(events)) # False


