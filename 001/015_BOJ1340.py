Month, D, Y, T = input().split()
D = int(D[:2])
Y = int(Y)
H, M = int(T[0:2]), int(T[3:5])  # map(int,T.splice(':'))
month_name_li = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
month_day_li = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if Y % 400 == 0 or (Y % 4 == 0 and Y % 100 != 0):
    month_day_li[1] = 29
total_time = sum(month_day_li) * 24 * 60
last_month_idx = sum(month_day_li[0 : (month_name_li.index(Month))]) * 24 * 60
current_time = 24 * 60 * (D - 1) + H * 60 + M + last_month_idx
print(current_time / total_time * 100)
