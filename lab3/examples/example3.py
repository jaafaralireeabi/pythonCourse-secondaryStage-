START_SPEED = 60
END_SPEED = 131
INCREMENT = 10
CONVERSION_FACTOR = 0.6214 
print('KPH\tMPH')
print('--------------')
for k in range(START_SPEED, END_SPEED, INCREMENT):
       mph = k * CONVERSION_FACTOR
       print(k, '\t', format(mph, '.1f'))
