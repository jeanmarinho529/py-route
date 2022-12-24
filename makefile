lint:
	poetry run pre-commit install && poetry run pre-commit run -a -v

test:
	poetry run pytest -sx --cov

update-precommit:
	poetry run pre-commit autoupdate

runserver:
	uvicorn py_route.main:app --host 127.0.0.1 --port 8000 --reload
