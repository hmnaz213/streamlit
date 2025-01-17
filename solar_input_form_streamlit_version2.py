def calculate_solar_pv_system(num_bedrooms, num_acs):
    """
    Estimate the cost of a solar PV home system based on user inputs.
    """
    # General BoM prices
    PRICES = {
        "3kW_inverter": 280,
        "5kW_inverter": 360,
        "2.5kWh_battery": 370,
        "5kWh_battery": 570,
        "panel": 30,
        "protection_system": 45,
        "cable": 6,
        "shipping": 350,
        "installation": 130,
    }

    # Determine system configuration based on inputs
    if 2 <= num_bedrooms <= 4:
        if num_acs == 0:
            inverter_type = "3kW_inverter"
            battery_type = "2.5kWh_battery"
            num_batteries = 1
        else:
            inverter_type = "5kW_inverter"
            battery_type = "5kWh_battery"
            num_batteries = num_acs
    elif num_bedrooms > 4:
        if num_acs == 0:
            inverter_type = "5kW_inverter"
            battery_type = "5kWh_battery"
            num_batteries = 1
        else:
            inverter_type = "5kW_inverter"
            battery_type = "5kWh_battery"
            num_batteries = num_acs
            num_inverters = 2  # Use two 5kW inverters
        else:
            num_inverters = 1

    # Calculate battery capacity and number of panels
    battery_capacity = num_batteries * float(battery_type.split("kWh")[0])  # in kWh
    num_panels = int(((battery_capacity * 1000 * 2) * 1.1 * 1.2 / 4) / 450)

    # Calculate costs
    inverter_cost = PRICES[inverter_type] * num_inverters
    battery_cost = PRICES[battery_type] * num_batteries
    panel_cost = PRICES["panel"] * num_panels
    mounting_cost = panel_cost * 0.5
    protection_cost = PRICES["protection_system"] * num_inverters
    cable_cost = PRICES["cable"]
    shipping_cost = PRICES["shipping"]
    installation_cost = PRICES["installation"]

    # Total cost and profit margin
    total_cost = (inverter_cost + battery_cost + panel_cost + mounting_cost +
                  protection_cost + cable_cost + shipping_cost + installation_cost)
    final_cost = total_cost * 2.1  # Apply profit margin

    # Return detailed breakdown
    return {
        "Number of Bedrooms": num_bedrooms,
        "Number of ACs": num_acs,
        "Number of Panels": num_panels,
        "Inverter Type": inverter_type,
        "Number of Inverters": num_inverters,
        "Battery Type": battery_type,
        "Number of Batteries": num_batteries,
        "Costs": {
            "Inverter Cost": inverter_cost,
            "Battery Cost": battery_cost,
            "Panel Cost": panel_cost,
            "Mounting Structure Cost": mounting_cost,
            "Protection System Cost": protection_cost,
            "Cable Cost": cable_cost,
            "Shipping Cost": shipping_cost,
            "Installation Cost": installation_cost,
            "Total Cost (Before Margin)": total_cost,
            "Final Cost (With Margin)": final_cost,
        }
    }

# Collect user input
num_bedrooms = int(input("Enter the number of bedrooms: "))
num_acs = int(input("Enter the number of ACs: "))

# Calculate system and costs
results = calculate_solar_pv_system(num_bedrooms, num_acs)

# Display the output
print("\nSolar PV System Estimate:\n")
for key, value in results.items():
    if key != "Costs":
        print(f"{key}: {value}")

print("\nCost Breakdown:")
for cost_key, cost_value in results["Costs"].items():
    print(f"{cost_key}: ${cost_value:,.2f}")
