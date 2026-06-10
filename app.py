import streamlit as st
import pandas as pd
import pickle
import gzip

# Load model
with gzip.open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.write("Model Type:", type(model))

st.set_page_config(page_title="Hotel Booking Cancellation Prediction")
st.title("🏨 Hotel Booking Cancellation Prediction")

# Form
with st.form("prediction_form"):

    hotel = st.text_input("Hotel")
    lead_time = st.number_input("Lead Time", min_value=0)

    arrival_date_year = st.number_input(
        "Arrival Date Year",
        min_value=2015,
        max_value=2030
    )

    arrival_date_month = st.text_input("Arrival Date Month")

    arrival_date_week_number = st.number_input(
        "Arrival Date Week Number",
        min_value=1,
        max_value=53
    )

    arrival_date_day_of_month = st.number_input(
        "Arrival Date Day Of Month",
        min_value=1,
        max_value=31
    )

    stays_in_weekend_nights = st.number_input(
        "stays in Weekend Nights",
        min_value=0
    )

    stays_in_week_nights = st.number_input(
        "stays in Week Nights",
        min_value=0
    )

    adults = st.number_input("Adults", min_value=1)

    children = st.number_input(
        "Children",
        min_value=0.0
    )

    babies = st.number_input(
        "Babies",
        min_value=0
    )

    meal = st.selectbox("Meal", ["BB", "FB", "HB", "SC", "Undefined"])
    country = st.text_input("Country")
   market_segment = st.selectbox(
    "Market Segment",
    ["Online TA", "Offline TA/TO", "Direct", "Groups", "Corporate"]
    )
    distribution_channel = st.selectbox(
    "Distribution Channel",
    ["TA/TO", "Direct", "Corporate", "GDS"]
    )

    previous_cancellations = st.number_input(
        "Previous Cancellations",
        min_value=0
    )

    previous_bookings_not_canceled = st.number_input(
        "Previous Bookings Not Canceled",
        min_value=0
    )

    reserved_room_type = st.text_input(
        "Reserved Room Type"
    )

    assigned_room_type = st.text_input(
        "Assigned Room Type"
    )

    booking_changes = st.number_input(
        "Booking Changes",
        min_value=0
    )

    deposit_type = st.selectbox("Deposit Type", ["No Deposit", "Refundable", "Non Refund"])

    days_in_waiting_list = st.number_input(
        "Days In Waiting List",
        min_value=0
    )

    customer_type = st.selectbox(
    "Customer Type",
    ["Transient", "Contract", "Group", "Transient-Party"]
    )

    adr = st.number_input(
        "ADR",
        min_value=0.0
    )

    required_car_parking_spaces = st.number_input(
        "Required Car Parking Spaces",
        min_value=0
    )

    total_of_special_requests = st.number_input(
        "Total Special Requests",
        min_value=0
    )

    submit = st.form_submit_button("Predict")
if submit:
    try:
        import pandas as pd

        df = pd.DataFrame([{
            "hotel": hotel,
            "lead_time": lead_time,
            "arrival_date_year": arrival_date_year,
            "arrival_date_month": arrival_date_month,
            "arrival_date_week_number": arrival_date_week_number,
            "arrival_date_day_of_month": arrival_date_day_of_month,

            "stays_in_weekend_nights": stays_in_weekend_nights,
            "stays_in_week_nights": stays_in_week_nights,
            "adults": adults,
            "children": children,
            "babies": babies,

            "meal": meal,
            "country": country,
            "market_segment": market_segment,
            "distribution_channel": distribution_channel,

            "previous_cancellations": previous_cancellations,
            "previous_bookings_not_canceled": previous_bookings_not_canceled,

            "reserved_room_type": reserved_room_type,
            "assigned_room_type": assigned_room_type,

            "booking_changes": booking_changes,
            "deposit_type": deposit_type,
            "days_in_waiting_list": days_in_waiting_list,
            "customer_type": customer_type,

            "adr": adr,
            "required_car_parking_spaces": required_car_parking_spaces,
            "total_of_special_requests": total_of_special_requests
        }])

        prediction = model.predict(df)[0]

        if prediction == 1:
            st.error("❌ Booking will be cancelled")
        else:
            st.success("✅ Booking will not be cancelled")

    except Exception as e:
        st.error(f"Error: {e}")
