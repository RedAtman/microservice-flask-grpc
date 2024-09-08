# microservice-flask-grpc

gRPC is a modern open source high performance Remote Procedure Call (RPC) framework that can run in any environment. It can efficiently connect services in and across data centers with pluggable support for load balancing, tracing, health checking and authentication. It is also applicable in last mile of distributed computing to connect devices, mobile applications and browsers to backend services.

### Command Line:

- $ python --version  #--> Python 3.8.5
- $ python3 -m venv .grpc
- $ source .grpc/bin/activate
- $ python -m pip install -r requirements.txt
- $ cd src
- $ python -m grpc_tools.protoc -I ../protobufs --python_out=. \
            --grpc_python_out=. ../protobufs/recommendations.proto
- $ see more of the rest of the commands used in this project on the realpython link in the reference section below!

### References:

- https://realpython.com/python-microservices-grpc/
- https://grpc.io/
- https://grpc.io/docs/languages/python/
- https://grpc.github.io/grpc/python/
