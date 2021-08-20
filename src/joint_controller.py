import asyncio
import websockets
import pickle
import setup
import interface
import numpy as np
import odrive as od


async def server(websocket, path):
    global joint_cmd
    p_cmd = await websocket.recv()
    cmd = pickle.loads(p_cmd)
    print('received', cmd)

    valid = True
    for i in range(len(cmd)):
        if np.abs(cmd[i] - joint_cmd[i]) > max_step:
            valid = False
    if not valid:
        print('max step exceeded, returning current angles', joint_cmd)
        p_joint_cmd = pickle.dumps(joint_cmd)
        await websocket.send(p_joint_cmd)
    else:
        p_succ = pickle.dumps('k')
        joint_cmd = cmd
        await websocket.send(p_succ)
        do(cmd)

def do(cmd):
    for i in range(len(cmd)):
        print(cmd[i], 'turns')
    print()
    JC.simple_set(cmd, testing=True)

joint_cmd = [0,0,0,0,0,0]
max_step = 2 * (1 * 40 / 240)
print('max step allowable', max_step)

OD_serial_path = 'odrive_serials.txt'
JC = interface.JointController(OD_serial_path)
JC.calib_axes()

start_server = websockets.serve(server, "192.168.1.95", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
