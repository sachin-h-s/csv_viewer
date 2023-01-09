import streamlit as st
import pandas as pd
import base64


st.title("Column Renamer")

# Allow the user to upload a CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV into a Pandas dataframe
    df = pd.read_csv(uploaded_file)

    # Display the dataframe
    st.dataframe(df)

    # Get the column name the user wants to change
    new_name = st.text_input("Enter new column name")

    # Get the name of the column to rename
    column_to_rename = st.selectbox("Select column to rename", df.columns)

    # Rename the column
    df = df.rename(columns={column_to_rename: new_name})

    # Display the modified dataframe
    st.dataframe(df)

    # Allow the user to download the modified CSV
    st.markdown("""
    ## Download modified CSV
    """)
    if st.button("Download modified CSV"):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
        href = f'<a href="data:file/csv;base64,{b64}">Download modified CSV file</a>'
        st.markdown(href, unsafe_allow_html=True)
