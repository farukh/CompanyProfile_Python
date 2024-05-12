import streamlit as st
import pandas

st.set_page_config(layout='wide')
st.title('Gibraltar Technologies & Solutions')
company_profile = """
Gibraltar Technologies & Solutions (GTS) is a Professional, Website and Mobile App Development Company
that Endeavor on Highly Proficient, Intuitive and Cost Effective Software
solutions. \n
Since our Inception, We have been helping companies across all the
industries to achieve their Business Goals with Impactful, BusinessCentric Software Solutions.\n
With our cutting-edge technologies, Agile Methodologies and in-depth
industry knowledge, We support the Digital Transformation of our clients
across all Business Verticals.
"""
st.write(company_profile)
st.subheader('Our Team')

col1, col2, col3 = st.columns(3)

df = pandas.read_csv('data.csv', sep=',')

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")


with col3:
    for index, row in df[8:12].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")

