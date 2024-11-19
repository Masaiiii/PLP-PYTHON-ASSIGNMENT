def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    return price


price = float(input("Enter the original price: $"))
discount_percent = float(input("Enter the discount percentage: "))


final_price = calculate_discount(price, discount_percent)

if final_price == price:
    print(f"No discount applied. Final price: ${price:.2f}")
else:
    print(f"Final price after {discount_percent}% discount: ${final_price:.2f}")