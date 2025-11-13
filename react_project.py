import streamlit as st

st.title("Select from the dropdown link to get your project details")

leagues = ('0', '1', '2', '3', '4', '5', '6', '7')


projectType = st.selectbox("Select Project", leagues)


if st.button("Check Project"):
    if projectType == '1':
          st.markdown(""" 
        Shopping Cart
        Concept: State, Context API, Components
        Add/remove items from cart
    """)

    elif projectType == '2':
        st.markdown("""
            Simple Counter
            Concept: State, Event Handling
            Display a number with + and - buttons
            Implement reset functionality
          """)

    elif projectType == '3':
        st.markdown("""
            Digital Clock
            Concept: useEffect, setInterval
            Display current time
            Update time every second
            """)

    elif projectType == '4':
        st.markdown("""
            Weather App 
            Concept:useEffect
            Fetch data from payload
            Display temperature and conditions
            Handle loading states

        """)

    elif projectType == '5':
        st.markdown("""
        Calculator
        Concept: State Management, Events
        Build basic arithmetic operations
        Handle user input
        Practice complex state logic
        """)

    elif projectType == '6':
        st.markdown(""""
        Recipe Finder
        Concept: Payload Integration, Search
        Search for recipes by ingredient
        Display results with images
        Practice handling user input
        """)

    elif projectType == '7':
        st.markdown("""
        Budget Tracker
        Concept: State, Forms, Calculations
        Add income/expenses
        Calculate balance
        List transactions
        Practice complex state management


        """)
