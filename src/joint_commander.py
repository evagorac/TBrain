import asyncio
import websockets
import pickle
import pygame
from pygame import K_LEFT, K_RIGHT, K_1, K_2, K_3, K_4, K_5, K_6, K_LSHIFT 
import time
import numpy as np


async def send_cmd(cmd):
    global joint_setpoints
    uri = "ws://192.168.1.166:8765"
    async with websockets.connect(uri) as websocket:
        pic_cmd = pickle.dumps(cmd)
        await websocket.send(pic_cmd)
        p_result = await websocket.recv()
        result = pickle.loads(p_result)
        if type(result) == list:
            joint_setpoints = result
    
def pass_cmd(cmd):
    asyncio.get_event_loop().run_until_complete(send_cmd(cmd))

# start pygame window for keypress inputs
pygame.display.init()
pygame.display.set_mode(size=(250,250))

joint_setpoints = [0,0,0,0,0,0]
move_vel = 1 # turns/s
sprint_multiplier = 40
rate = 240
move_step = move_vel / rate
print('max step =', move_step * sprint_multiplier)

joint_queue = [1]
while True:
    key = pygame.key.get_pressed()
    vel = -key[K_LEFT] + key[K_RIGHT]

    joint_keys = [None, K_1, K_2, K_3, K_4, K_5, K_6]
    for i in range(len(joint_keys)):
        joint_key = joint_keys[i]
        if joint_key is None: continue
        if key[joint_key] == 1:
            if i not in joint_queue:
                joint_queue.insert(0, i)
        elif len(joint_queue) > 1:
            if i in joint_queue:
                joint_queue.remove(i)
    vel_cmd = (joint_queue[0], vel)

    step = vel_cmd[1] * move_step

    if key[K_LSHIFT]:
        step *= sprint_multiplier

    joint_setpoints[vel_cmd[0]-1] += step

    print('current joint:', vel_cmd[0])
    for x in joint_setpoints:
        print(x, 'turns')
    pass_cmd(joint_setpoints)

    print()
    time.sleep(1/rate)
    pygame.event.pump()
