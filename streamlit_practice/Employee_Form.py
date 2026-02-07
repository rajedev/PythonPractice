"""
Author: Rajendhiran Easu
Date: 07/02/26
Description: Employee Information Form with Pydantic validation
"""
from datetime import datetime, date
from typing import Literal, Annotated

import streamlit as st
from pydantic import BaseModel, Field, AfterValidator


def name_must_not_be_empty(v: str) -> str:
    """Validate that name is not empty or just whitespace"""
    if not v or not v.strip():
        raise ValueError('Name cannot be empty')
    return v.strip()


class EmployeeInfo(BaseModel):
    """Employee information model with validation"""
    name: Annotated[str, Field(min_length=1, description="Employee name"), AfterValidator(name_must_not_be_empty)]
    age: int = Field(ge=18, le=65, description="Employee age")
    department: str = Field(min_length=1, description="Department")
    hobbies: list[str] = Field(default_factory=list, description="Employee hobbies")
    experience: int = Field(ge=0, le=40, description="Years of experience")
    gender: Literal["Male", "Female", "Other"] = Field(description="Gender")
    date_of_birth: date = Field(description="Date of Birth")


def employee_form():
    with st.form(key="employee_form", clear_on_submit=True):
        e_name = st.text_input("Name*", placeholder="Enter employee name")
        age = st.number_input("Age*", min_value=18, max_value=65, value=18)
        dob = st.date_input("Date of Birth", min_value=datetime(1975, 1, 1), max_value=datetime.now(),
                            value=datetime(1988, 7, 22))
        experience = st.slider("Years of Experience*", min_value=0, max_value=40, value=0)
        gender = st.radio("Gender*", options=["Male", "Female", "Other"], horizontal=True)
        department = st.selectbox("Department*", ["HR", "IT", "Finance", "Marketing"])
        hobbies = st.multiselect("Hobbies", ["Reading", "Traveling", "Cooking", "Sports"])
        st.markdown("_*Required fields_")
        col1, col2, col3 = st.columns([6, 1.2, 1])
        with col2:
            submit_button = st.form_submit_button(label="Submit", type="primary")
        with col3:
            clear_button = st.form_submit_button(label="Clear")

    if submit_button:
        try:
            # Validate and create employee info
            employee_info = EmployeeInfo(
                name=e_name,
                age=age,
                department=department,
                hobbies=hobbies,
                experience=experience,
                gender=gender,
                date_of_birth=dob
            )

            # Display success message
            st.success("✅ Employee information submitted successfully!")

            # Display submitted information in a nice format
            with st.expander("View Submitted Details", expanded=True):
                col_a, col_b = st.columns(2)
                with col_a:
                    st.write("**Name:**", employee_info.name)
                    st.write("**Age:**", employee_info.age)
                    st.write("**Department:**", employee_info.department)
                    st.write("**DoB:**", employee_info.date_of_birth)
                with col_b:
                    st.write("**Gender:**", employee_info.gender)
                    st.write("**Experience:**", f"{employee_info.experience} years")
                    st.write("**Hobbies:**", ", ".join(employee_info.hobbies) if employee_info.hobbies else "None")

        except ValueError as e:
            st.error(f"❌ Validation Error: {e}")

    if clear_button:
        st.info("Form cleared successfully!")
        st.rerun()


if __name__ == "__main__":
    st.title("SMV Software Solutions")
    st.header("Employee Information")
    employee_form()
