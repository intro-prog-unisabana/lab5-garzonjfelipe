from utils import *

message = input("Please type your message\n")

flipped = flip(message)

count = count_letters(message)

encoded = flipped + str(count)

print("Your encoded message is:", encoded)