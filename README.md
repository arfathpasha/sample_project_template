# sample_project_template

This is a template repo that contains all the hooks needed for building, testing, continuous integration and coverage reporting. This template may be used as a baseline for creating other repos/projects on github. 

Build status:
master:  [![Build Status](https://travis-ci.org/arfathpasha/sample_project_template.svg?branch=master)](https://travis-ci.org/arfathpasha/sample_project_template)

staging: [![Build Status](https://travis-ci.org/arfathpasha/sample_project_template.svg?branch=staging)](https://travis-ci.org/arfathpasha/sample_project_template)

develop: [![Build Status](https://travis-ci.org/arfathpasha/sample_project_template.svg?branch=develop)](https://travis-ci.org/arfathpasha/sample_project_template)

Code coverage: (master branch)
[![Coverage Status](https://coveralls.io/repos/github/arfathpasha/sample_project_template/badge.svg?branch=master&cacheBuster=1)](https://coveralls.io/github/arfathpasha/sample_project_template?branch=master)

Prerequisites:
--------------
python2.7 <br>
Virtualenv <br>
pip <br>
docker <br>

Usage:
------
1. Create a virtual environment (if not already present)
> virtualenv venv

2. Activate virtual environment
> source venv/bin/activate

3. Install dependencies
> pip install -r requirements.txt

4. View the various build options and exercise one of them
make help

5. Deactivate virtual environment
deactivate
