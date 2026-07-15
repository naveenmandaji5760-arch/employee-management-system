print("Leave Module")

employee_name = input("Enter Employee Name: ")
leave_days = int(input("Enter Leave Days: "))

if leave_days <= 5:
    print(employee_name, "Leave Approved")
else:
    print(employee_name, "Manager Approval Required")