'''Python: Basic

15 points

This assignment will develop your familiarity with doing simple computations in Python.
'''

def savings(gross_pay, tax_rate, expenses):
    '''Savings.
    5 points.

    This function calculates the money remaining
        for an employee after taxes and expenses.

    To get the take-home pay of an employee, we will
        follow the following process:
        1. Apply the tax rate to the gross pay of the employee; round down
        2. Subtract the expenses from the after-tax pay of the employee

    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos

    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    gross_pay =int(input("What is the gross pay amount?"))
    tax_rate = float(input("What is the tax rate?"))
    after_tax_pay = gross_pay-(gross_pay*tax_rate)
    print("The employee's after-tax pay is Php",after_tax_pay)

    expenses = int(input("How much is the employee's total expenses?"))
    take_home_pay = int(after_tax_pay-expenses)
    print("After taxes and expenses, the employee's total take home pay is Php",take_home_pay)

"--------------------------------------------------------------------------------------------------------------------------------------"

def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.
    5 points.

    This function calculates how much material input will be wasted
        after running a certain number of jobs that consume
        a set amount of material.

    To get the waste of a set of jobs:
        1. Multiply the number of jobs by the material consumption per job.
        2. Subtract the total material consumed from the total material available.

    The users of this function also want you to format the output as a string, annotated with the
        units in which the material is expressed. Do not add a space between the number and the unit.

    Parameters
    ----------
    total_material: int
        the total material available
    material_units: str
        the units used to express a quantity of the material (e.g., "kg", "L", etc.)
    num_jobs: int
        the number of jobs to run
    job_consumption: int
        the amount of material consumed per job

    Returns
    -------
    str
        the amount of remaining material expressed with its unit (e.g., "10kg").
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
num_jobs =int(input("How many jobs will be run?"))
job_consumption =int(input("How much material is consumed per job?"))
material_units =str(input("What is the unit of the material used?"))
material_used =num_jobs*job_consumption
print("The total material consumed is",str(material_used)+material_units)

total_material =int(input("How much is the total material available?"))
material_waste =total_material-material_used
print("The total material wasted after",num_jobs,"jobs is",str(material_waste)+material_units)

"--------------------------------------------------------------------------------------------------------------------------------------"

def interest(principal, rate, periods):
    '''Interest.
    5 points.

    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.

    To calculate simple interest, simply multiply the principal to the quantity (rate * time).
        Add this amount to the principal to get the final value.

    Round down the final amount.

    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested

    Returns
    -------
    int
        the final value of the investment
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

principal = int(input("What is the principal amount invested?"))
rate = input("What is the interest rate per period?")
rate_percent = float(int(rate)/100)
print("The interest rate is",rate_percent)
period = int(input("For how many periods is the money invested?"))
interest = int(principal*rate_percent*period)
final_investment = principal+interest

print("With a simple interest of Php "+str(interest)+", the final investment value is set to be Php",final_investment)
