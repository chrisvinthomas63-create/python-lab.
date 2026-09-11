name = input("Enter Consumer Name: ")
consumer_id = input("Enter Consumer ID: ")
prev_reading = float(input("Enter Previous Meter Reading (kWh): "))
curr_reading = float(input("Enter Current Meter Reading (kWh): "))
cost_per_unit = float(input("Enter Cost per Unit (₹): "))

units_consumed = curr_reading - prev_reading
energy_charge = units_consumed * cost_per_unit
electricity_duty = 0.05 * energy_charge
fixed_charge = 100.0
net_bill = energy_charge + electricity_duty + fixed_charge

print("\n--- Electricity Bill Statement ---")
print("Consumer Name =", name)
print("Consumer ID =", consumer_id)
print("Units Consumed =", units_consumed)
print("Energy Charge =", energy_charge)
print("Electricity Duty =", electricity_duty)
print("Fixed Meter Charge =", fixed_charge)
print("Net Bill Amount =", net_bill)