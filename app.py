import streamlit as st
import joblib

# Load the trained model
model = joblib.load("student_performance_model.pkl")

# Sidebar
st.sidebar.title("📌 About Project")

st.sidebar.write("**AI-Driven Student Performance Prediction System**")

st.sidebar.write("Developed Using:")

st.sidebar.write("✅ Python")
st.sidebar.write("✅ Machine Learning")
st.sidebar.write("✅ Random Forest")
st.sidebar.write("✅ Streamlit")

# Title
st.title("🎓 AI-Driven Student Performance Prediction System")

# Description
st.write("Predict a student's final exam performance using Machine Learning.")
st.divider()
student_name = st.text_input("Student Name")

attendance = st.number_input(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=75
)

internal_test1 = st.number_input(
    "Internal Test 1 (out of 40)",
    min_value=0,
    max_value=40,
    value=20
)

internal_test2 = st.number_input(
    "Internal Test 2 (out of 40)",
    min_value=0,
    max_value=40,
    value=20
)

assignment_score = st.number_input(
    "Assignment Score (out of 10)",
    min_value=0,
    max_value=10,
    value=5
)

study_hours = st.number_input(
    "Daily Study Hours",
    min_value=0,
    max_value=24,
    value=3
)

predict = st.button("🚀 Predict Performance", use_container_width=True)

if predict:

    input_data = [[
        attendance,
        internal_test1,
        internal_test2,
        assignment_score,
        study_hours
    ]]

    prediction = model.predict(input_data)
    predicted_marks = prediction[0]

    st.success("✅ Prediction completed successfully!")

    st.subheader(f"📋 Prediction Report for {student_name}")

    st.subheader("👨‍🎓 Student Details")

    st.write(f"**Name:** {student_name}")
    st.write(f"**Attendance:** {attendance}%")
    st.write(f"**Internal Test 1:** {internal_test1}/40")
    st.write(f"**Internal Test 2:** {internal_test2}/40")
    st.write(f"**Assignment Score:** {assignment_score}/10")
    st.write(f"**Daily Study Hours:** {study_hours} Hours")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="🎯 Predicted Marks",
            value=f"{predicted_marks:.2f}/100"
        )

    with col2:
        st.metric(
            label="📚 Daily Study Hours",
            value=f"{study_hours} Hours"
        )

    # Grade
    if predicted_marks >= 90:
        grade = "A+"
    elif predicted_marks >= 80:
        grade = "A"
    elif predicted_marks >= 70:
        grade = "B+"
    elif predicted_marks >= 60:
        grade = "B"
    elif predicted_marks >= 50:
        grade = "C"
    else:
        grade = "F"

    st.subheader("🏅 Grade")
    st.info(f"Grade: {grade}")

    # Performance
    if predicted_marks >= 85:
        st.success("🏆 Performance: Excellent")
    elif predicted_marks >= 70:
        st.info("👍 Performance: Good")
    elif predicted_marks >= 50:
        st.warning("⚠️ Performance: Average")
    else:
        st.error("❌ Performance: Needs Improvement")

    st.subheader("📊 Performance Score")
    st.progress(min(int(predicted_marks), 100))

    st.subheader("💡 Study Recommendations")

    if predicted_marks >= 85:
        st.write("✅ Excellent performance! Keep maintaining your study routine.")
    elif predicted_marks >= 70:
        st.write("📚 Good job! Revise regularly to achieve even better marks.")
    elif predicted_marks >= 50:
        st.write("📝 Increase your study hours and focus on weak subjects.")
    else:
        st.write("⚠️ Improve attendance, complete assignments, and study consistently.")