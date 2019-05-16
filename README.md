# Tax calculator [May 2019]

Web application to count taxes in UK (2019/2020 current configuration) based on https://listentotaxman.com/

## Technologies:
- Python
- Flask (http://flask.pocoo.org/)

## How to run

Set environment variable:
###### `FLASK_APP=Main.py`
If you would like to dynamically load changes, you should also set below variable:
###### `FLASK_DEBUG=1`

Run:
###### `flask run`

Go to the below URL:
###### localhost:5000

# Additional links
Basic tutorial for Flask:
https://pythonspot.com/flask-web-forms/

## Link to application
TODO https://devcenter.heroku.com/categories/python-support

    # TODO Tax is counting after allow taxes (12509) and pension
    # TODO Pension and NI is counting after only allow taxes

TODO something wrong with counting for NI? or description is wrong

TODO:
- check full stuff from end-2-end
- unit tests/integration tests
- configuration file
- possible to pick up a different tax year
- 'help' with explanation how taxes are working