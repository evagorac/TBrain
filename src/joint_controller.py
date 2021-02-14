import asyncio
import websockets
import pickle
from utils import setup
from utils import interface
import numpy
import odrive as od


async def server(websocket, path):
    cmd = await websocket.recv()
    print(f"received command {cmd}")
    do(cmd)

def do(cmd):
    joint, vel_dir = cmd

    

    JC.simple_set(setpoints, testing=True)


OD_serial_path = '../odrive_serials.txt'
JC = interface.JointController(OD_serial_path)
JC.calib_axes()

start_server = websockets.serve(server, "192.168.1.95", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
