import streamlit as st

def add(x, y):
    """Adds two numbers"""
    return x + y

def subtract(x, y):
    """Subtracts two numbers"""
    return x - y

def multiply(x, y):
    """Multiplies two numbers"""
    return x * y

def divide(x, y):
    """Divides two numbers"""
    if y == 0:
        return "Error! Division by zero."
    return x / y

st.title("Simple Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
        st.success(f"{num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = subtract(num1, num2)
        st.success(f"{num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = multiply(num1, num2)
        st.success(f"{num1} * {num2} = {result}")
    elif operation == "Divide":
        result = divide(num1, num2)
        if isinstance(result, str):
            st.error(result)
        else:
            st.success(f"{num1} / {num2} = {result}")
