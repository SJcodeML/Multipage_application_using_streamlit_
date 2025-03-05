import streamlit as st

# from forms.contact import contact_form

from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


# Hero Section

col1 , col2 = st.columns(2, gap="small" , vertical_alignment= "center")
with col1:
    st.title("hi")
            # st.image("./assets/profile_image.png" , width = 230)
with col2:
    st.title("Sidra Jabin" , anchor= False)
    st.write(
        "Senior Data Analyst , assisting enterprises by supporting data-driven decision-making"
    )
    if st.button("📞 Contact Me"):
     show_contact_form()
       


# Adding Experience and Education
st.write ("\n")
st.subheader("Qualification" , anchor=False)
st.write(
    """
       - Degree: BS, Computer Science - University X (Expected May 2025)
       - Relevant Coursework: Data Structures, Algorithms, Machine Learning, Web Development
       - GPA: 3.8 (Optional, include if strong)
       - Skills: Python, Streamlit, Pandas, NumPy, scikit-learn, HTML, CSS
    
     """
)


st.subheader("Experience" , anchor=False)
st.write(
    """
      - Project: Developed a Streamlit app for [Project Description] using [Technologies].
      - Internship: Data Science Intern at [Company] - [Responsibilities, e.g., "Built and deployed a model..."]
      - Volunteer: Tutored students in Python programming.
      - Hackathon: [Award/Recognition] for [Project Name] at [Hackathon Name].
    
     """
)



