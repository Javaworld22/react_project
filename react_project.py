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
        """) st.markdown("""
            {"New York": {
    temperature: 22,
    condition: "Sunny",
    humidity: 65,
    windSpeed: 15,
    icon: "☀️"
  },
  "London": {
    temperature: 15,
    condition: "Cloudy",
    humidity: 80,
    windSpeed: 20,
    icon: "☁️"
  },
  "Tokyo": {
    temperature: 28,
    condition: "Rainy",
    humidity: 75,
    windSpeed: 10,
    icon: "🌧️"
  },
  "Sydney": {
    temperature: 30,
    condition: "Sunny",
    humidity: 60,
    windSpeed: 12,
    icon: "☀️"
  },
  "Paris": {
    temperature: 18,
    condition: "Partly Cloudy",
    humidity: 70,
    windSpeed: 18,
    icon: "⛅"
  }
};
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
        st.markdown("""
         {
    id: 1,
    title: "Vegetable Pasta",
    image: "🍝",
    ingredients: ["pasta", "tomatoes", "basil", "garlic", "olive oil"],
    instructions: "Cook pasta. Sauté garlic, add tomatoes. Mix with pasta.",
    cookingTime: 20,
    difficulty: "Easy"
  },
  {
    id: 2,
    title: "Chicken Stir Fry",
    image: "🍲",
    ingredients: ["chicken", "bell peppers", "soy sauce", "ginger", "rice"],
    instructions: "Stir fry chicken and vegetables. Add sauce. Serve with rice.",
    cookingTime: 25,
    difficulty: "Medium"
  },
  {
    id: 3,
    title: "Chocolate Cake",
    image: "🍰",
    ingredients: ["flour", "sugar", "cocoa", "eggs", "butter", "milk"],
    instructions: "Mix dry ingredients. Add wet ingredients. Bake at 350°F for 30 mins.",
    cookingTime: 45,
    difficulty: "Medium"
  },
  {
    id: 4,
    title: "Greek Salad",
    image: "🥗",
    ingredients: ["cucumber", "tomatoes", "feta cheese", "olives", "olive oil"],
    instructions: "Chop vegetables. Mix with feta and olives. Dress with oil.",
    cookingTime: 10,
    difficulty: "Easy"
  },
  {
    id: 5,
    title: "Beef Tacos",
    image: "🌮",
    ingredients: ["ground beef", "taco shells", "lettuce", "cheese", "salsa"],
    instructions: "Cook beef with seasoning. Fill taco shells with toppings.",
    cookingTime: 15,
    difficulty: "Easy"
  }
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
