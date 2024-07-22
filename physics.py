# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Creating a function that will convert Fahrenheit to Celcius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9 
  return round(c_temp, 2)
# testing function with a value of 100 Fahrenheit
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return round(f_temp, 2)
# testing function with a value of 0 Celcius
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

def get_force(mass, acceleration):
  return mass * acceleration
# Testing function
train_force = get_force(train_mass, train_acceleration)
print(train_force)

print('The GE train supplies ' + str(train_force) + ' Newtons of force.')

# Defining a function that takes in mass and c
def get_energy(mass, c=3*10**8):
  return mass * c**2

bomb_energy = get_energy(bomb_mass)
print('A 1kg bomb supplies ' + str(bomb_energy) + ' Joules')

# Defining a function that takes mass, distance and acceleration
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print('The GE train does ' + str(train_work) + ' Joules of work over ' + str(train_distance) + ' meters')



