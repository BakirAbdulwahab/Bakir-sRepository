print("Hello, and welcome to the tip calculator!\n")

totalBill = input("What was the total bill? $")

percentAmount = input("What percentage tip would you like to give? 10%, 12%, or 15%? ")

peopleSplitting = input("How many people are splitting the bill? ")

tipAmount = ((float(totalBill) * (int(percentAmount) / 100) + float(totalBill)) / int(peopleSplitting))

result = (f"Each person should pay: ${round(tipAmount , 2)}")

print(result)