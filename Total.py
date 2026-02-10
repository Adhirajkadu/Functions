def total_calc(amount,tip):
    bill=amount*(1 + 0.01*tip)
    bill=round(bill,2)
    print("Please Pay ",bill)

total_calc(5000,10)