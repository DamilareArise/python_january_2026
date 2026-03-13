import datetime as dt



now = dt.datetime.now()
# print(now)
# print(now.date())
# print(now.time())
# print(now.year)
# print(now.month)

my_date = dt.datetime(2026, 6, 7, 12, 00)
# print(type(my_date))


# .strftime
"""

Token	Meaning	Example Output
%Y	Year (4 digits)	2026
%y	Year (2 digits)	26
%m	Month (zero-padded)	03
%B	Full month name	March
%b / %h	Abbreviated month name	Mar
%d	Day of month (zero-padded)	13
%e	Day of month (space-padded)	13
%A	Full weekday name	Friday
%a	Abbreviated weekday name	Fri
%w	Weekday as number (0=Sunday)	5
%j	Day of year (001–366)	072
%U	Week number (Sunday first day, 00–53)	10
%W	Week number (Monday first day, 00–53)	10
%H	Hour (24-hour, zero-padded)	14
%I	Hour (12-hour, zero-padded)	02
%p	AM/PM	PM
%M	Minute (zero-padded)	45
%S	Second (zero-padded)	09
%f	Microsecond (zero-padded, 6 digits)	123456
%z	UTC offset	+0100
%Z	Time zone name	WAT
%c	Locale’s date and time	Fri Mar 13 14:45:09 2026
%x	Locale’s date	03/13/26
%X	Locale’s time	14:45:09
%%	Literal % character	%


"""
# 7,june,2026

# print(my_date.strftime("%d, %B, %Y"))

# strptime
# dt_str = "25-Dec-26"
# dt_obj = dt.datetime.strptime(dt_str, "%d-%b-%y")
# print(dt_obj.date())


# print(my_date - now)

# print(my_date + dt.timedelta(days=2))


# Age calculator

dob = input("DOB dd/mm/yyyy: ")
dob_obj = dt.datetime.strptime(dob, "%d/%m/%Y")
age = now.year - dob_obj.year
print(f"{age} years")