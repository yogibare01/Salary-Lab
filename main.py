hourly_rate = 20.00
overtime_rate = hourly_rate * 1.50
hours_worked = float(input())

if hours_worked <= 40:
  regular_hours = hours_worked
  overtime_hours = 0
else:
  regular_hours = 40
  overtime_hours = hours_worked - 40

regular_pay = regular_hours * hourly_rate
overtime_pay = overtime_hours * overtime_rate
weekly_pay = f'{(regular_pay + overtime_pay):.2f}'

print(weekly_pay)
