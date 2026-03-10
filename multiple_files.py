from utils import *

mensaje = input("Please type your message\n")

invertido = flip(mensaje)
cantidad_a = count_letters(invertido, 'a')

print("Your encoded message is:", invertido + str(cantidad_a))