import streamlit as st

# Function to estimate solar system cost
def estimate_solar_system_cost(num_bedrooms):
    """
    Estimate the cost of a solar PV system based on the number of bedrooms.
    """
    # Assumptions for calculation:
    panel_area_per_bedroom = 10  # m² of solar panels
    battery_capacity_per_bedroom = 5  # kWh of energy storage
    inverter_rating_per_bedroom = 2  # kW

    # Costs per unit
    panel_cost_per_m2 = 200  # $ per m²
    battery_cost_per_kwh = 300  # $ per kWh
    inverter_cost_per_kw = 150  # $ per kW

    # Calculate requirements
    total_panel_area = num_bedrooms * panel_area_per_bedroom
    total_battery_capacity = num_bedrooms * battery_capacity_per_bedroom
    total_inverter_rating = num_bedrooms * inverter_rating_per_bedroom

    # Calculate costs
    panel_cost = total_panel_area * panel_cost_per_m2
    battery_cost = total_battery_capacity * battery_cost_per_kwh
    inverter_cost = total_inverter_rating * inverter_cost_per_kw
    total_cost = panel_cost + battery_cost + inverter_cost

    return {
        "Panel Cost ($)": panel_cost,
        "Battery Cost ($)": battery_cost,
        "Inverter Cost ($)": inverter_cost,
        "Total Cost ($)": total_cost,
    }

# Streamlit UI
st.title("Solar PV System Cost Estimator")
st.write("Calculate the estimated cost of a solar PV system based on the number of bedrooms.")

# User input
num_bedrooms = st.number_input("Enter the number of bedrooms:", min_value=1, step=1, format="%d")

# Calculate and display results
if st.button("Calculate"):
    results = estimate_solar_system_cost(num_bedrooms)
    st.write("### Cost Breakdown")
    for key, value in results.items():
        st.write(f"{key}: ${value:,.2f}")
