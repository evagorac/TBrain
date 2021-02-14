import asyncio
import websockets
import pickle
import pygame
from pygame import K_LEFT, K_RIGHT, K_1, K_2, K_3, K_4, K_5, K_6
import time


async def send_cmd(cmd):
    print(f'attempting to send {cmd}')
    uri = "ws://192.168.1.95:8765"
    async with websockets.connect(uri) as websocket:
        pic_cmd = pickle.dumps(cmd)
        await websocket.send(pic_cmd)
    
def pass_cmd(cmd):
    asyncio.get_event_loop().run_until_complete(send_cmd(cmd))

# start pygame window for keypress inputs
pygame.display.init()
pygame.display.set_mode(size=(250,250))

joint_queue = [1]
while True:
    key = pygame.key.get_pressed()
    vel_cmd = -key[K_LEFT] + key[K_RIGHT]

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
    cmd = (joint_queue[0], vel_cmd)
    pass_cmd(cmd)

    time.sleep(.05)
    pygame.event.pump()
