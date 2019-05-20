

class Result:

    def __init__(self):
        self.salary_before_tax = 0
        self.salary_after_tax = 0

        self.tax_20_pay = 0
        self.tax_40_pay = 0
        self.tax_45_pay = 0
        self.ni_12_pay = 0
        self.ni_2_pay = 0
        self.pension_percent = 0
        self.pension = 0

    def get_annual(self, value):
        return round(value, 2)

    def get_month(self, value):
        return round(value / 12, 2)

    # Count based on 5 working days and 52 weeks in a year.
    def get_day(self, value):
        return round(value / (52 * 5), 2)

    # TAX FREE
    def get_annual_tax_free(self):
        return self.get_annual(self.tax_free)

    def get_month_tax_free(self):
        return self.get_month(self.tax_free)

    def get_day_tax_free(self):
        return self.get_day(self.tax_free)

    # SALARY BEFORE TAX
    def get_annual_salary_before_tax(self):
        return self.get_annual(self.salary_before_tax)

    def get_month_salary_before_tax(self):
        return self.get_month(self.salary_before_tax)

    def get_day_salary_before_tax(self):
        return self.get_day(self.salary_before_tax)

    # SALARY AFTER TAX
    def get_annual_salary_after_tax(self):
        return self.get_annual(self.salary_after_tax)

    def get_month_salary_after_tax(self):
        return self.get_month(self.salary_after_tax)

    def get_day_salary_after_tax(self):
        return self.get_day(self.salary_after_tax)

    # TAX 20%
    def get_annual_tax_20(self):
        return self.get_annual(self.tax_20_pay)

    def get_month_tax_20(self):
        return self.get_month(self.tax_20_pay)

    def get_day_tax_20(self):
        return self.get_day(self.tax_20_pay)

    # TAX 40%
    def get_annual_tax_40(self):
        return self.get_annual(self.tax_40_pay)

    def get_month_tax_40(self):
        return self.get_month(self.tax_40_pay)

    def get_day_tax_40(self):
        return self.get_day(self.tax_40_pay)

    # TAX 45%
    def get_annual_tax_45(self):
        return self.get_annual(self.tax_45_pay)

    def get_month_tax_45(self):
        return self.get_month(self.tax_45_pay)

    def get_day_tax_45(self):
        return self.get_day(self.tax_45_pay)

    # NATIONAL INSURANCE 12%
    def get_annual_ni_12(self):
        return self.get_annual(self.ni_12_pay)

    def get_month_ni_12(self):
        return self.get_month(self.ni_12_pay)

    def get_day_ni_12(self):
        return self.get_day(self.ni_12_pay)

    # NATIONAL INSURANCE 2%
    def get_annual_ni_2(self):
        return self.get_annual(self.ni_2_pay)

    def get_month_ni_2(self):
        return self.get_month(self.ni_2_pay)

    def get_day_ni_2(self):
        return self.get_day(self.ni_2_pay)

    # PENSION
    def get_annual_pension(self):
        return self.get_annual(self.pension)

    def get_month_pension(self):
        return self.get_month(self.pension)

    def get_day_pension(self):
        return self.get_day(self.pension)
