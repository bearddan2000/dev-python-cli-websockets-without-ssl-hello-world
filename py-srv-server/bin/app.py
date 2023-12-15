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
 
# create handler for each connection
 
async def handler(websocket, path):
 
    data = await websocket.recv()
 
    reply = f"[SERVER] Data recieved as:  {data}!"
 
    await websocket.send(reply)
 
start_server = websockets.serve(handler, "0.0.0.0", 8000)
  
asyncio.get_event_loop().run_until_complete(start_server)
 
asyncio.get_event_loop().run_forever()