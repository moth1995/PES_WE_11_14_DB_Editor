from .utils.common_functions import to_b_int32, to_int

class Salary:

    def __init__(self, idx: int, salary_bytes: bytearray):
        self.idx = idx
        self.salary_bytes = salary_bytes
        self.set_salary_from_bytes()

    def set_salary_from_bytes(self):
        self.__salary = to_int(self.salary_bytes)

    @property
    def salary(self):
        """
        Return player name.
        """
        return self.__salary

    @salary.setter
    def salary(self, salary: int):
        """
        Update player name with the supplied value.
        """
        new_salary = salary
        new_salary_bytes = to_b_int32(salary)
        self.salary_bytes[self.idx * 4 : self.idx * 4 + 4] = new_salary_bytes
        self.__salary = new_salary
