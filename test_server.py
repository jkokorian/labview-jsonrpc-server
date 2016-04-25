#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:10102")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)
    
    request = json.loads(message)    
    response = json.dumps(dict(id=request['id'],result=request['id']+1,jsonrpc="2.0"))
    #  Do some 'work'
    time.sleep(1)

    
    #  Send reply back to client
    socket.send(response)