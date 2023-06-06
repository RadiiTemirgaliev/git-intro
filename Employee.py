# create a class
class Employee:

    # create a class attribute
    vacation_days = 20




# create object/instance from the class
Mike = Employee()
Jane = Employee()
Bob = Employee()

print(f'Vacation days of Maike is {Mike.vacation_days}')
print(f'Vacation days of Jane is {Jane.vacation_days}')
print(f'Vacation days of Jane is {Bob.vacation_days}')

# change object attribute value
print('Vacation days of Jane incresed to 20')
Jane.vacation_days = 20
Jane.is_manager = True

print(Jane.is_manager)

# change class attribute value
print('Minimum vacation days incresed to 12')
Employee.vacation_days = 12

print(f'Vacation days of Maike is {Mike.vacation_days}')
print(f'Vacation days of Jane is {Jane.vacation_days}')
print(f'Vacation days of Jane is {Bob.vacation_days}')






# print(mike)
# print(type(mike))
# print(isinstance(mike, Employee))

