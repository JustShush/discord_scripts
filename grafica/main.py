from pynput.keyboard import Key, Controller
import time
import keyboard

kb = Controller()

cooldown = 10
max = 0

print("If you dont want cooldown write 0.  (The default cooldown is 10 sec)")
cooldown = int(input("Cooldown: "))
max = int(input("How many times do you want to farm: "))

i = 0
time.sleep(2) # 2 sec sleep
while i <= max:
	kb.press('1')
	time.sleep(0.1) # hold the key down a short duration
	kb.release('1')
	i += 1
	time.sleep(cooldown)
