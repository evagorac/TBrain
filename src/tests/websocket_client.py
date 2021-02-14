import asyncio
import websockets
import pickle

async def hello():
    uri = "ws://192.168.1.95:8765"
    async with websockets.connect(uri) as websocket:

        joint_vel_cmds = [0,0,0,0,0,0]
        print(f'attempting to send {joint_vel_cmds}')
        pic_cmd = pickle.dumps(joint_vel_cmds)

        await websocket.send(pic_cmd)

        success = await websocket.recv()
        if success == '1':
            print('success')

asyncio.get_event_loop().run_until_complete(hello())
