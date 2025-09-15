# task: build an income tax calculator function
def taxCalculator(avg_income):
    if avg_income < 5000000:
        income_tax = 0 + avg_income * 0.05
        return income_tax
    elif avg_income >= 5000000 and avg_income < 10000000:
        income_tax = 250000 + (avg_income - 5000000) * 0.1
        return income_tax
    elif avg_income >= 10000000 and avg_income < 18000000:
        income_tax = 750000 + (avg_income - 10000000) * 0.15
        return income_tax
    elif avg_income >= 18000000 and avg_income < 32000000:
        income_tax = 1950000 + (avg_income - 18000000) * 0.2
        return income_tax
    elif avg_income >= 32000000 and avg_income < 52000000:
        income_tax = 4750000 + (avg_income - 32000000) * 0.25
        return income_tax
    elif avg_income >= 52000000 and avg_income < 80000000:
        income_tax = 9750000 + (avg_income - 52000000) * 0.3
        return income_tax
    else:
        income_tax = 18150000 + (avg_income - 80000000) * 0.3
        return income_tax
