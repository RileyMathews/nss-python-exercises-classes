class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = set()

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    # Add the remaining methods to fill the requirements above

    def get_employees(self):
        print(f'Employee report for {self.company_name}')
        for employee in self.employees:
            employee.print_information()


class Employee:
    """ this class represent the people which work at companies """

    def __init__(self, fn, ln, job_title, start_date):
        self.first_name = fn
        self.last_name = ln
        self.job_title = job_title
        self.start_date = start_date

    def print_information(self):
        print(f'{self.first_name} {self.last_name} started working as {self.job_title} on {self.start_date}')

# create a company
galactic_empire = Company("The Galactic Empire", "-10 BBY")

# declare employee objects
vader = Employee("Darth", "Vader", "Sith Lord", "-10 BBY")
sidious = Employee("Darth", "Sidious", "Emperor", "-10 BBY")
thrawn = Employee("Mithrando", "Thrawn", "Admiral", "-6 BBY")

# add employees to galactic empire
galactic_empire.employees.add(vader)
galactic_empire.employees.add(sidious)
galactic_empire.employees.add(thrawn)

# call employee report for galactic empire
galactic_empire.get_employees()
