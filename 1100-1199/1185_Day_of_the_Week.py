# Given a date, return the corresponding day of the week for that date.
#
# The input is given as three integers representing the day, month and year respectively.
#
# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
# "Saturday"}.
#
#
#
# Example 1:
# Input: day = 31, month = 8, year = 2019
# Output: "Saturday"
#
# Example 2:
# Input: day = 18, month = 7, year = 1999
# Output: "Sunday"
#
# Example 3:
# Input: day = 15, month = 8, year = 1993
# Output: "Sunday"
#
#
# Constraints:
# The given dates are valid dates between the years 1971 and 2100.


#from datetime import date


class Solution:
    # def dayOfTheWeek(self, d: int, m: int, y: int) -> str:
    #     return date(y,m,d).strftime("%A")


    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # 1.1.1971 - Friday
        return [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ][
            (
                day
                + [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334][month - 1]
                + (1 if year % 4 == 0 and month > 2 and year != 2100 else 0)
                + int((year - 1971) * 365.25 + 0.5)
                + 4
            )
            % 7
        ]
