# Freds_gross_sal = 850/week
# 11% for federal deduction 5.5% for state deduction 6.2% for company's pension
# what is net salary for 4 weeks
'''gross_Sal = 850*4 # for 4 weeks
net_Sal_Base = (850 * .227) * 4 # for 4 weeks
net_Sal = gross_Sal - net_Sal_Base
print(net_Sal)'''

'''
Every week fred earns 850$ as gross income and loses 22.7% of that as deductions.
This leaves him with (850 - (850 * .227))$ every week.
Hence, for a 4 week period, his net salary would be (850 - (850 * .227)) * 4.'''

#general solution

gross_Sal = float(input("Enter gross salary per week: "))
fed_ded = float(input("Enter federal deduction: "))
stt_ded = float(input("Enter state deduction: "))
com_pen = float(input("enter company pension plan deduction: "))
no_of_weeks = float(input("Enter number of weeks: "))
net_sal = (gross_Sal*no_of_weeks) - ((gross_Sal*no_of_weeks) * ((fed_ded + stt_ded + com_pen)/100))
deductions_per_week = (gross_Sal) * ((fed_ded + stt_ded + com_pen)/100)
weekly_sal = gross_Sal - deductions_per_week
print(f"\n\nThe amount deducted every week is {deductions_per_week}$\n\nThe weekly salary is {weekly_sal}$\n\nActual salary for specified number of weeks is {gross_Sal * no_of_weeks}$\n\nThe net sal is: {net_sal}$.")
