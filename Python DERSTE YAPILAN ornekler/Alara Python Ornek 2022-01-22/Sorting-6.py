# A function that returns the 'year' value:
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
print ("Sıralama öncesi: \n %s \n" %cars)

cars.sort(key=myFunc)
print("Sıralama sonrası: \n %s \n" %cars)
