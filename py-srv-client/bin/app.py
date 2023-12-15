import asyncio
import websockets
import os
import ssl

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
cert = os.path.join('cert', "server.crt")
private_key = os.path.join('cert', "server.key")
ssl_context.verify_mode = ssl.CERT_OPTIONAL 
ssl_context.check_hostname = False
# ssl_context.load_verify_locations(cafile=cert)
ssl_context.load_cert_chain(cert, keyfile=private_key)

async def test(): 
    async with websockets.connect('wss://py-srv-server:8000', ssl=ssl_context) as websocket:
        await websocket.send("hello world")
        response = await websocket.recv()
        print(f'[CLIENT] {response}')
 
asyncio.get_event_loop().run_until_complete(test())