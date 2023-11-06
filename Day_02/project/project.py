name = input("Hello!, What is your name ? : ")
print(f"Great {name}")

sales_mounth = float(input(f"How much did you sell this month {name} ? :"))

if sales_mounth > 1000:
    print(f"Excelent {name}")
else:
    print(f"We are on the good way {name}")


comisions = round(sales_mounth * 13 / 100, 2)

print(
    f"Perfect {name}!!\nSince your sales for the month were {sales_mounth}\nYour bonus will be {comisions}"
)
