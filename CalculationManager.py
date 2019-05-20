from Result import Result
from TaxConfig import TaxConfig


class CalculationManager:

    PENSION = 0

    tax_config = TaxConfig()

    def __init__(self, provided_salary, provided_pension):
        self.salary_before_taxes = provided_salary
        self.PENSION = provided_pension
        self.result = Result()
        self.result.salary_before_tax = provided_salary
        self.result.pension_percent = provided_pension
        self.result.tax_free = self.tax_config.get_tax_free()

    def get_result(self):
        return self.result

    def count_tax_20(self):
        if self.salary_before_taxes > (self.tax_config.get_tax_20_min() + self.PENSION):
            if self.salary_before_taxes > (self.tax_config.get_tax_20_max() + self.PENSION):
                salary_above = (self.tax_config.get_tax_20_max() + self.PENSION) - (self.tax_config.get_tax_20_min() + self.PENSION)
            else:
                salary_above = self.salary_before_taxes - (self.tax_config.get_tax_20_min() + self.PENSION)
            self.result.tax_20_pay = round(salary_above * float(0.20), 2)

    def count_tax_40(self):
        if self.salary_before_taxes > (self.tax_config.get_tax_40_min() + self.PENSION):
            if self.salary_before_taxes > (self.tax_config.get_tax_40_max() + self.PENSION):
                salary_above = (self.tax_config.get_tax_40_max() + self.PENSION) - (self.tax_config.get_tax_40_min() + self.PENSION)
            else:
                salary_above = self.salary_before_taxes - (self.tax_config.get_tax_40_min() + self.PENSION)
            self.result.tax_40_pay = round(salary_above * float(0.40), 2)

    def count_tax_45(self):
        if self.salary_before_taxes > (self.tax_config.get_tax_45_min() + self.PENSION):
            salary_above = self.salary_before_taxes - (self.tax_config.get_tax_45_min() + self.PENSION)
            self.result.tax_45_pay = round(salary_above * float(0.45), 2)

    def count_ni_12(self):
        if self.salary_before_taxes > self.tax_config.get_year_ni_12():
            if self.salary_before_taxes > self.tax_config.get_year_ni_2():
                salary_above = self.tax_config.get_year_ni_2() - self.tax_config.get_year_ni_12()
            else:
                salary_above = self.salary_before_taxes - self.tax_config.get_year_ni_12()
            self.result.ni_12_pay = round(salary_above * float(0.12), 2)

    def count_ni_2(self):
        if self.salary_before_taxes > self.tax_config.get_year_ni_2():
            salary_above = self.salary_before_taxes - self.tax_config.get_year_ni_2()
            self.result.ni_2_pay = round(salary_above * float(0.02), 2)

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
