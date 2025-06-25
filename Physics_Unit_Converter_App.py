import streamlit as st
from pint import UnitRegistry

# Initialize unit registry
ureg = UnitRegistry()

# Define units for each category
units = {
    "Length": ["meter", "kilometer", "centimeter", "inch", "foot", "mile"],
    "Mass": ["kilogram", "gram", "pound", "ounce"],
    "Time": ["second", "minute", "hour"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Energy": ["joule", "calorie", "kilojoule"],
    "Force": ["newton", "dyne", "pound_force"]
}

st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("🔁 Simple Physics Unit Converter")

st.write("Select a category and convert values easily between units.")

category = st.selectbox("Pick a category", list(units.keys()))
from_unit = st.selectbox("From", units[category])
to_unit = st.selectbox("To", units[category])
value = st.number_input("Enter value", value=0.0)

if st.button("Convert"):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        st.success(f"{value} {from_unit} = {result:.3f}")
    except Exception as e:
        st.error("Oops! Something went wrong.")

with st.expander("Need Help?"):
    st.markdown("""
    - **Temperature**: °C to °F: T(°F) = T(°C) × 9/5 + 32
    - **Energy**: 1 calorie = 4.184 joules
    - **Force**: 1 newton = 10⁵ dynes
    """)

st.caption("Built with Streamlit and Pint by [M Usman]")
