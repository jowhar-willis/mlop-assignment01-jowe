# install dependencies
install:
	pip install -r requirements.txt

# run tests
test:
	pytest

# run app
run:
	python app.py
