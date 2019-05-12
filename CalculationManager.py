from decimal import Decimal
from Result import Result


class CalculationManager:

    # Constant values
    PENSION = 0

    TAX_FREE = 12500
    TAX_20_MIN = 12500
    TAX_20_MAX = 49999
    TAX_40_MIN = 50000
    TAX_40_MAX = 149999
    TAX_45_MIN = 150000

    YEAR_NI_12 = 8632 # £166 per week
    YEAR_NI_2 = 50000 # Wrong: £962 per week

    def __init__(self, provided_salary, provided_pension):
        self.salary_before_taxes = Decimal(provided_salary)
        self.pension = Decimal(provided_pension)
        self.result = Result()
        self.result.salary_before_tax = Decimal(provided_salary)
        self.result.pension_percent = Decimal(provided_pension)
        self.result.tax_free = self.TAX_FREE

    def get_result(self):
        return self.result

    def count_tax_20(self):
        if self.salary_before_taxes > (self.TAX_20_MIN + self.PENSION):
            if self.salary_before_taxes > (self.TAX_20_MAX + self.PENSION):
                salary_above = (self.TAX_20_MAX + self.PENSION) - (self.TAX_20_MIN + self.PENSION)
            else:
                salary_above = self.salary_before_taxes - (self.TAX_20_MIN + self.PENSION)
            self.result.tax_20_pay = round(salary_above * Decimal(0.20), 2)

    def count_tax_40(self):
        if self.salary_before_taxes > (self.TAX_40_MIN + self.PENSION):
            if self.salary_before_taxes > (self.TAX_40_MAX + self.PENSION):
                salary_above = (self.TAX_40_MAX + self.PENSION) - (self.TAX_40_MIN + self.PENSION)
            else:
                salary_above = self.salary_before_taxes - (self.TAX_40_MIN + self.PENSION)
            self.result.tax_40_pay = round(salary_above * Decimal(0.40), 2)

    def count_tax_45(self):
        if self.salary_before_taxes > (self.TAX_45_MIN + self.PENSION):
            salary_above = self.salary_before_taxes - (self.TAX_45_MIN + self.PENSION)
            self.result.tax_45_pay = round(salary_above * Decimal(0.45), 2)

    def count_ni_12(self):
        if self.salary_before_taxes > self.YEAR_NI_12:
            if self.salary_before_taxes > self.YEAR_NI_2:
                salary_above = self.YEAR_NI_2 - self.YEAR_NI_12
            else:
                salary_above = self.salary_before_taxes - self.YEAR_NI_12
            self.result.ni_12_pay = round(salary_above * Decimal(0.12), 2)

    def count_ni_2(self):
        if self.salary_before_taxes > self.YEAR_NI_2:
            salary_above = self.salary_before_taxes - self.YEAR_NI_2
            self.result.ni_2_pay = round(salary_above * Decimal(0.02), 2)

    def count_pension(self):
        if self.result.pension_percent != 0:
            pension_pay = self.result.salary_before_tax * self.result.pension_percent / 100
            self.result.salary_after_tax = self.result.salary_after_tax - pension_pay
            self.PENSION = pension_pay
            self.result.pension = pension_pay

    def count_salary_after_taxes(self):
        self.result.salary_after_tax = self.result.salary_before_tax \
                                       - self.result.get_annual_tax_45() \
                                       - self.result.get_annual_tax_40() \
                                       - self.result.get_annual_tax_20() \
                                       - self.result.get_annual_ni_12() \
                                       - self.result.get_annual_ni_2() \
                                       - self.result.get_annual_pension()
