# Tax calculator [May 2019]

Web application to count taxes in UK (2019/2020 current configuration) based on https://listentotaxman.com/

## Link to demo of application
https://tax-calculator-palprz.herokuapp.com

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
###### `localhost:5000`

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