# Disclaimer
All projects that start with `dev`
are under active development.

This project is in development meaning
it does not produce expected results.

# Problem
Failure on client.

# Error
   asyncio.get_event_loop().run_until_complete(test())
 Traceback (most recent call last):
   File "/code/app.py", line 20, in <module>
     asyncio.get_event_loop().run_until_complete(test())
   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 664, in run_until_complete
     return future.result()
            ^^^^^^^^^^^^^^^
   File "/code/app.py", line 15, in test
     async with websockets.connect('wss://py-srv-server:8000', ssl=ssl_context) as websocket:
   File "/usr/local/lib/python3.12/site-packages/websockets/legacy/client.py", line 629, in __aenter__
     return await self
            ^^^^^^^^^^
   File "/usr/local/lib/python3.12/site-packages/websockets/legacy/client.py", line 647, in __await_impl_timeout__
     return await self.__await_impl__()
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/usr/local/lib/python3.12/site-packages/websockets/legacy/client.py", line 651, in __await_impl__
     _transport, _protocol = await self._create_connection()
                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 1126, in create_connection
     transport, protocol = await self._create_connection_transport(
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/usr/local/lib/python3.12/asyncio/base_events.py", line 1150, in _create_connection_transport
     transport = self._make_ssl_transport(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/usr/local/lib/python3.12/asyncio/selector_events.py", line 83, in _make_ssl_transport
     ssl_protocol = sslproto.SSLProtocol(
                    ^^^^^^^^^^^^^^^^^^^^^
   File "/usr/local/lib/python3.12/asyncio/sslproto.py", line 327, in __init__
     self._sslobj = self._sslcontext.wrap_bio(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/usr/local/lib/python3.12/ssl.py", line 469, in wrap_bio
     return self.sslobject_class._create(
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/usr/local/lib/python3.12/ssl.py", line 808, in _create
     sslobj = context._wrap_bio(
              ^^^^^^^^^^^^^^^^^^
 ssl.SSLError: Cannot create a client socket with a PROTOCOL_TLS_SERVER context (_ssl.c:806)

# Possible solutions
Need to fix client connection.