import asyncio
import websockets
import pickle

async def hello(websocket, path):
    pic_cmd = await websocket.recv()
    joint_vel_cmds = pickle.loads(pic_cmd)

    print('recieved data')

    await websocket.send('1')
    print(f"> {joint_vel_cmds}")

start_server = websockets.serve(hello, "192.168.1.95", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
