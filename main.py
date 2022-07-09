import time

person_forward = '''
     O
  / /\_,
___/\ 
   /_ 
'''

person_backward = '''
     O
  / /\_,
   /\ 
 /   \\
'''

running = [person_forward, person_backward]

def clear(sleep_time):
    time.sleep(sleep_time)
    print("\033c")

def print_with_time(string, sleep_time):
    print(string)
    print("˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙")
    clear(sleep_time)

clear(0)

speed = 10
for i in range(100):
    sleep_time = 1/speed
    print_with_time(running[i%2], sleep_time)
    if speed <= 1:
        continue
    speed = speed - 0.1

