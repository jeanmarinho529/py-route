lint:
	poetry run pre-commit install && poetry run pre-commit run -a -v

test:
	poetry run pytest -sx --cov

update-precommit:
	poetry run pre-commit autoupdate

runserver:
	uvicorn py_route.main:app --port 8001 --reload

# uvicorn main:app --reload
