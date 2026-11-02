
import streamlit as st
import random

# Remember previous dice rolls
if "history" not in st.session_state:
    st.session_state.history = []
    
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

    # Save the result of each roll
    st.session_state.history.append({
        "Dice 1": dice1,
        "Dice 2": dice2,
        "Total": total
    })

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
    
# PART 2: ROLL HISTORY

st.divider()
st.header("📜 Previous Rolls")

if len(st.session_state.history) > 0:

    st.dataframe(
        st.session_state.history,
        use_container_width=True
    )

    # PART 3: FREQUENCY CHART

    st.header("📊 Dice Roll Statistics")

    # Count how often each total appears
    totals = [roll["Total"] for roll in st.session_state.history]

    frequency = {
        number: totals.count(number)
        for number in range(2, 13)
    }

    st.bar_chart(
        frequency,
        x_label="Dice Total",
        y_label="Number of Rolls"
    )

    # PART 4: RESET BUTTON

    if st.button("Clear History"):
        st.session_state.history = []
        st.rerun()

else:
    st.write("No rolls yet. Click Roll Dice to begin!")


