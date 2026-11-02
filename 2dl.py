
import streamlit as st
import random

# Website title
st.title("🎲 My Dice Roller")

st.write("Roll two dice with six faces each!")

# Button to roll dice
if st.button("Roll Dice"):

    # Generate random numbers
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    # Calculate total
    total = dice1 + dice2

    # Display dice faces
    faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Dice 1")
        st.markdown(f"# {faces[dice1 - 1]}")

    with col2:
        st.subheader("Dice 2")
        st.markdown(f"# {faces[dice2 - 1]}")

    # Display total
    st.success(f"Total: {total}")

