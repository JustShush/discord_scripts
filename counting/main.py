from pynput.keyboard import Key, Controller
import time
import keyboard

kb = Controller()

cooldown = 0
numb = 0
max = 0

print("If you dont want cooldown write 0.  (The default cooldown is 2 sec)")
cooldown = int(input("Cooldown: "))
numb = int(input("Write the number you want to start counting from: "))
max = int(input("Until whitch number do you want to count: "))

#digits = [int(digit) for digit in str(numb)] # retorna um array de ints

i = 0
time.sleep(2) # 2 sec sleep
numb += 1
while numb <= max:
	i = 0
	digits = list(str(numb)) # returns an array of chars
	while i < len(digits):
		kb.press(digits[i])
		kb.release(digits[i])
		i += 1
	time.sleep(2)
	kb.press(kb._Key.enter)
	kb.release(kb._Key.enter)
	if cooldown == 2:
		time.sleep(2)
	else:
		time.sleep(cooldown)
	numb += 1
