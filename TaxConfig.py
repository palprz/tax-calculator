
class TaxConfig:

    def __init__(self):
        loaded_file= open("configuration.txt", "r")
        lines = loaded_file.read().splitlines()
        for line in lines:
            if len(line) == 0 or line[0] == '#':
                continue

            values = line.split('=');
            attr = values[0]
            value = float(values[1])

            if attr == 'tax_free_allocate':
                self.TAX_FREE = value
            elif attr == 'tax_20_percent_minimum_range':
                self.TAX_20_MIN = value
            elif attr == 'tax_20_percent_maximum_range':
                self.TAX_20_MAX = value
            elif attr == 'tax_40_percent_minimum_range':
                self.TAX_40_MIN = value
            elif attr == 'tax_40_percent_maximum_range':
                self.TAX_40_MAX = value
            elif attr == 'tax_45_percent_minimum_range':
                self.TAX_45_MIN = value
            elif attr == 'national_insurance_12_percent_minimum_range':
                self.YEAR_NI_12 = value
            elif attr == 'national_insurance_2_percent_minimum_range':
                self.YEAR_NI_2 = value

    def get_tax_free(self):
        return self.TAX_FREE

    def get_tax_20_min(self):
        return self.TAX_20_MIN

    def get_tax_20_max(self):
        return self.TAX_20_MAX

    def get_tax_40_min(self):
        return self.TAX_40_MIN

    def get_tax_40_max(self):
        return self.TAX_40_MAX

    def get_tax_45_min(self):
        return self.TAX_45_MIN

    def get_year_ni_12(self):
        return self.YEAR_NI_12

    def get_year_ni_2(self):
        return self.YEAR_NI_2
