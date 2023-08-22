import asyncio;
import websockets;
 
async def accept(websocket, path):
  while True:
    data = await websocket.recv();
    print("receive : " + data);
    await websocket.send("echo : " + data);
 
# 웹 소켓 서버 생성.호스트는 localhost에 port는 9998로 생성한다. 
start_server = websockets.serve(accept, "localhost", 9998);

# 비동기로 서버를 대기한다.
asyncio.get_event_loop().run_until_complete(start_server);
asyncio.get_event_loop().run_forever();
