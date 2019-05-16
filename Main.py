from flask import Flask, url_for, render_template, request, abort, redirect
from CalculationManager import CalculationManager

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')


@app.route("/", methods=['GET'])
def redirection():
    return redirect(url_for('tax_calculator'))


@app.route("/count", methods=['GET'])
def tax_calculator():
    provided_salary = request.args.get('providedSalary')
    provided_pension = request.args.get('providedPension')
    show_description = request.args.get('showDescription')

    if not provided_salary:
        return render_template('index.html', result=None)

    try:
        int(provided_salary)
    except ValueError:
        abort(400)

    try:
        int(provided_pension)
    except ValueError:
        provided_pension = 0

    calculation_manager = CalculationManager(provided_salary, provided_pension)
    calculation_manager.count_pension()
    calculation_manager.count_tax_20()
    calculation_manager.count_tax_40()
    calculation_manager.count_tax_45()
    calculation_manager.count_ni_12()
    calculation_manager.count_ni_2()

    calculation_manager.count_salary_after_taxes()

    return render_template('index.html',
                           result=calculation_manager.get_result(),
                           provided_salary=provided_salary,
                           provided_pension=provided_pension,
                           calculation_manager=CalculationManager,
                           show_description=show_description)


if __name__ == "__main__":
    app.run(host='127.0.0.1')