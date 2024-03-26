def calculate_tip_per_person(bill_amount, service_quality, num_people):
    tip_percentage = service_quality / 100
    total_tip = bill_amount * tip_percentage
    tip_per_person = total_tip / num_people
    return tip_per_person

bill_amount = float(input("Enter the total bill amount: "))
service_quality = int(input("Enter the level of satisfaction (1-5): "))
num_people = int(input("Enter the number of people splitting the bill: "))

tip_per_person = calculate_tip_per_person(bill_amount, service_quality, num_people)
print(f"The tip per person is: {tip_per_person:.2f}")