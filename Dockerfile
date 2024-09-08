FROM python:3.8-slim

# RUN mkdir -p /service/src/
COPY protobufs/ /service/protobufs/
COPY src/ /service/src/
COPY requirements.txt /service/src/requirements.txt
WORKDIR /service/src
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m pip install markupsafe==2.0.1 --force-reinstall
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
    --grpc_python_out=. ../protobufs/recommendations.proto

# WORKDIR /service/src
EXPOSE 5000
ENV FLASK_APP=marketplace.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]
