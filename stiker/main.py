from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller
import time
import keyboard

#while True:
#    if keyboard.is_pressed("a"):
#        print("You pressed 'a'.")
#        break

# create a mouse/kb controller object
mouse = Controller()
kb = Controller()

op = input("mouse(1) or keyboard(2)?: ")
if op == 1:
	flag = True
else:
	flag = False

max = int(input("quantas vezes: "))
print(f"deve demorar por volta de: {(max * 10) + (max * 4)}s\n{((max * 10) + (max * 4)) / 60} min")

i = 0
time.sleep(2) # 2 sec sleep
while i < max:
		if flag == True:

			# open stikers (1080, 680)
			mouse.position = (1080, 680)
			mouse.click(Button.left)
			time.sleep(2) # 2 sec sleep

			# click the stiker (776, 364)
			mouse.position = (776, 364)
			mouse.click(Button.left)
			time.sleep(14) # 14 sec sleep
			i += 1
		else:
			kb.press(kb._Key.ctrl_l)
			kb.press('s')
			kb.release(kb._Key.ctrl_l)
			kb.release('s')
			time.sleep(2) # 2 sec sleep
			kb.press(kb._Key.enter)
			kb.release(kb._Key.enter)
			time.sleep(14) # 14 sec sleep
			i += 1

