# Write a program to count the number of days between two dates.
#
# The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.
#
#
#
# Example 1:
#
# Input: date1 = "2019-06-29", date2 = "2019-06-30"
# Output: 1
# Example 2:
#
# Input: date1 = "2020-01-15", date2 = "2019-12-31"
# Output: 15
#
#
# Constraints:
#
# The given dates are valid dates between the years 1971 and 2100.


class Solution:
    # def daysBetweenDates(self, date1: str, date2: str) -> int:
    #     from datetime import datetime
    #
    #     M = datetime.strptime(date1, "%Y-%m-%d").date()
    #     N = datetime.strptime(date2, "%Y-%m-%d").date()
    #     return abs((N - M).days)

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def getdaysfrom19710101(date: str) -> int:
            dm = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
            y, m, d = map(int, date.split("-"))

            return (
                (y - 1971) * 365
                + (y - 1969) // 4
                + dm[m - 1]
                + (y % 4 == 0 and m > 2 and y != 2100)
                + d
            )

        return abs(getdaysfrom19710101(date1) - getdaysfrom19710101(date2))
