venv:
	python3 -m venv ./venv
	./venv/bin/pip install -r requirements.in

test: venv
	./venv/bin/python -m unittest discover tests
