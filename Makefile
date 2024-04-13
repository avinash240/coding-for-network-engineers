gen-proto:
	python -m grpc_tools.protoc -I libs/frr --python_out=. --pyi_out=. --grpc_python_out=. frr-northbound.proto

build-venv:
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.in
