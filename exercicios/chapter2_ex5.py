# Calcular a distancia entre dois maximos consecutivos, \Delta y de uma figura de interferência
# delta_y = lambda*D/d

lambda_laser = 632.8E-9 # m
dist_D = 1.98 # m  
d = 0.250E-3 # m

delta_y = lambda_laser*dist_D/d
print('delta_y = ', delta_y)