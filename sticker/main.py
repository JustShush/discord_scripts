from pynput.keyboard import Key, Controller
import time
import keyboard

#while True:
#    if keyboard.is_pressed("a"):
#        print("You pressed 'a'.")
#        break

# create a kb controller object
kb = Controller()

cooldown = 14
alt_tab = False

print("If you dont want cooldown write 0.  (The default cooldown is 10 sec)")
Input = input("Cooldown: ")
if Input == "":
	cooldown = 14
	print(f"Cooldown set to default: {cooldown}")
else: 
	cooldown = int(Input)
top = int(input("how many times: "))
print(f"it should take around: {(top * 10) + (top * 4)}s\n{((top * 10) + (top * 4)) / 60} min")

i = 0
time.sleep(2) # 2 sec sleep
while i < top:
			kb.press(kb._Key.ctrl_l)
			kb.press('s')
			kb.release(kb._Key.ctrl_l)
			kb.release('s')
			time.sleep(2) # 2 sec sleep
			kb.press(kb._Key.enter)
			kb.release(kb._Key.enter)
			print(f"{(top - 1) - i} stickers left")
			time.sleep(cooldown) # 14 sec sleep
			i += 1

