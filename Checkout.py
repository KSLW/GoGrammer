
age = int(input("Enter your age: "))
total_price = float(input("Enter the total order price: "))
account_balance = float(input("Enter your account balance: "))

if 18 <= age <= 25:
    discount_rate = 0.10
elif 26 <= age <= 60:
    discount_rate = 0.05
else:
    discount_rate = 0.0

discounted_price = total_price * (1 - discount_rate)

if account_balance >= discounted_price:
    print("Order successful! Thank you for your purchase.")
else:
    shortfall = discounted_price - account_balance
    print(f"Insufficient balance. You are short by ${shortfall:.2f}.")
