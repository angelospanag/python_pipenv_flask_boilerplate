.PHONY: run lint

run:
	@pipenv run gunicorn -w 4 -b 0.0.0.0:5000 main:app

lint:
	@pipenv run flake8 app --max-complexity 10
