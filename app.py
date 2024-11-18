import streamlit as st

# Title of the application
st.title("Simple Calculator")

# Input fields for the numbers
num1 = st.number_input("Enter the first number", format="%f")
num2 = st.number_input("Enter the second number", format="%f")

# Select the operation
operation = st.selectbox(
    "Select an operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Perform the calculation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The result of addition is: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The result of subtraction is: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The result of multiplication is: {result}")
    elif operation == "Division":
        if num2 == 0:
            st.error("Error: Division by zero is not allowed")
        else:
            result = num1 / num2
            st.success(f"The result of division is: {result}")
