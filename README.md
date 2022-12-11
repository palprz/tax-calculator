# Tax calculator

Web application to count taxes in UK (with default configuration for 2019/2020 year). Application is based on https://listentotaxman.com/

## Screenshots from running app

Calculated taxes:
![Screnshot from running application with calculated taxes example][calculated_taxes]


Calculated taxes with explanation how it has been calculated (doesn't contain all details):
![Screnshot from running application with calculated taxes with explanation how it has been calculated example][calculated_taxes_explained]

## Technologies:
- Python
- Flask (http://flask.pocoo.org/)

## How to run
Set environment variable:
###### `export FLASK_APP=Main.py`
(optional) To dynamically load changes you should also set below variable:
###### `export FLASK_DEBUG=1`

Run:
###### `flask run`

Go to the below URL:
###### `127.0.0.1:5000`

# Configuration file
`configuration.txt` file contains values for tax/National Insurance bands. You should provide necessary details for the current tax year to be sure that application will count properly. Example of the configuration file you can find below:

```
# Configuration 2019

tax_free_allocate=12500
tax_20_percent_minimum_range=12500
tax_20_percent_maximum_range=49999
tax_40_percent_minimum_range=50000
tax_40_percent_maximum_range=149999
tax_45_percent_minimum_range=150000
national_insurance_12_percent_minimum_range=8632
national_insurance_2_percent_minimum_range=50000
```

# Additional links
Basic tutorial for Flask:
https://pythonspot.com/flask-web-forms/

[calculated_taxes]: https://github.com/palprz/tax-calculator/blob/master/screenshots/calculated_taxes.png
[calculated_taxes_explained]: https://github.com/palprz/tax-calculator/blob/master/screenshots/calculated_taxes_explained.png