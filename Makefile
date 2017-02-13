help:
	@echo '    clean'
	@echo '       Remove python and build artifacts.'
	@echo '    lint'
	@echo '        Check style with flake8.'
	@echo '    test'
	@echo '        Run unit tests'
	@echo '    run'
	@echo '        Run the `my_project` service on your local machine.'
	@echo '    docker-run'
	@echo '        Build and run the `my_project` service in a Docker container.'


clean:
	@echo "removing python artifacts..."
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force  {} +

	@echo "removing build artifacts..."
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

	@echo "removing coverage output"
	rm --force --recursive docs/coverage


lint:
	flake8 --ignore=E302 --exclude=.tox src/python


test:
	@echo "running unit tests..."
	nosetests --tests=test/python --with-coverage --cover-html --cover-html-dir=docs/coverage