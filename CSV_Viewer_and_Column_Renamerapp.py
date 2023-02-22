# import streamlit as st
# import pandas as pd
# import base64


# st.title("CSV Viewer and Column Renamer")

# # Allow the user to upload a CSV file
# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")


# if uploaded_file is not None:
#     # Read the CSV into a Pandas dataframe
#     df = pd.read_csv(uploaded_file)

#     # Display the dataframe
#     st.dataframe(df)

#     # Get the column name the user wants to change
#     new_name = st.text_input("Enter new column name")

#     # Get the name of the column to rename
#     column_to_rename = st.selectbox("Select column to rename", df.columns)

#     # Rename the column
#     df = df.rename(columns={column_to_rename: new_name})

#     # Display the modified dataframe
#     st.dataframe(df)

#     # Allow the user to download the modified CSV
# # Allow the user to download the modified CSV
# st.markdown("""
# ## Download modified CSV
# """)
# if st.button("Download modified CSV"):
#     csv = df.to_csv(index=False)
#     b64 = base64.b64encode(csv.encode()).decode()
#     href = f'<a href="data:file/csv;base64,{b64}" download="modified.csv">Download modified CSV file</a>'
#     st.markdown(href, unsafe_allow_html=True)






# import streamlit as st
# import pandas as pd
# import base64


# st.title("CSV Viewer and Column Editor")

# # Allow the user to upload a CSV file
# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# if uploaded_file is not None:
#     # Read the CSV into a Pandas dataframe
#     df = pd.read_csv(uploaded_file)

#     # Display the dataframe
#     st.dataframe(df)

#     # Get the column names the user wants to change
#     selected_columns = st.multiselect("Select columns to rename", df.columns)

#     # Get the new names for the selected columns
#     new_names = {}
#     for col in selected_columns:
#         new_name = st.text_input(f"Enter new name for '{col}'", value=col)
#         new_names[col] = new_name

#     # Rename the selected columns
#     df = df.rename(columns=new_names)

#     # Get the position where the user wants to add the new column
#     new_column_position = st.slider("Select position for new column", 0, len(df.columns))

#     # Get the name of the new column
#     new_column_name = st.text_input("Enter name of new column")

#     # Get the value to fill the new column
#     new_column_value = st.text_input("Enter value for new column")

#     # Insert the new column at the specified position
#     df.insert(new_column_position, new_column_name, new_column_value)

#     # Display the modified dataframe
#     st.dataframe(df)

#     # Allow the user to download the modified CSV
#     st.markdown("""
#     ## Download modified CSV
#     """)
#     if st.button("Download modified CSV"):
#         csv = df.to_csv(index=False)
#         b64 = base64.b64encode(csv.encode()).decode()
#         href = f'<a href="data:file/csv;base64,{b64}" download="modified.csv">Download modified CSV file</a>'
#         st.markdown(href, unsafe_allow_html=True)












# import streamlit as st
# import pandas as pd
# import base64


# st.title("CSV Viewer and Column Editor")

# # Allow the user to upload a CSV file
# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# if uploaded_file is not None:
#     # Read the CSV into a Pandas dataframe
#     df = pd.read_csv(uploaded_file)

#     # Display the dataframe
#     st.dataframe(df)

#     # Get the column names the user wants to change
#     selected_columns = st.multiselect("Select columns to rename", df.columns)

#     # Get the new names for the selected columns
#     new_names = {}
#     for col in selected_columns:
#         new_name = st.text_input(f"Enter new name for '{col}'", value=col)
#         new_names[col] = new_name

#     # Rename the selected columns
#     df = df.rename(columns=new_names)

#     # Get the position where the user wants to add the new column
#     new_column_position = st.slider("Select position for new column", 0, len(df.columns))

#     # Get the name of the new column
#     new_column_name = st.text_input("Enter name of new column")

#     # Get the value to fill the new column
#     new_column_value = st.text_input("Enter value for new column")

#     # Insert the new column at the specified position
#     df.insert(new_column_position, new_column_name, new_column_value)

#     # Get the column names the user wants to remove
#     columns_to_remove = st.multiselect("Select columns to remove", df.columns)

#     # Remove the selected columns
#     df = df.drop(columns_to_remove, axis=1)

#     # Display the modified dataframe
#     st.dataframe(df)

#     # Allow the user to download the modified CSV
#     st.markdown("""
#     ## Download modified CSV
#     """)
#     if st.button("Download modified CSV"):
#         csv = df.to_csv(index=False)
#         b64 = base64.b64encode(csv.encode()).decode()
#         href = f'<a href="data:file/csv;base64,{b64}" download="modified.csv">Download modified CSV file</a>'
#         st.markdown(href, unsafe_allow_html=True)






import streamlit as st
import pandas as pd
import base64

st.title("CSV Viewer and Column Editor")

# Allow the user to upload a CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV into a Pandas dataframe
    df = pd.read_csv(uploaded_file)

    # Display the dataframe
    st.dataframe(df)

    # Get the column names the user wants to change
    selected_columns = st.multiselect("Select columns to rename", df.columns)

    # Get the new names for the selected columns
    new_names = {}
    for col in selected_columns:
        new_name = st.text_input(f"Enter new name for '{col}'", value=col)
        new_names[col] = new_name

    # Rename the selected columns
    df = df.rename(columns=new_names)

    # Check if the user wants to add a new column
    add_new_column = st.checkbox("Add a new column")

    if add_new_column:
        # Get the position where the user wants to add the new column
        new_column_position = st.slider("Select position for new column", 0, len(df.columns), len(df.columns))

        # Get the name of the new column
        new_column_name = st.text_input("Enter name of new column")

        # Get the value to fill the new column
        new_column_value = st.text_input("Enter value for new column")

        # Insert the new column at the specified position
        df.insert(new_column_position, new_column_name, new_column_value)

    # Get the column names the user wants to remove
    columns_to_remove = st.multiselect("Select columns to remove", df.columns)

    # Remove the selected columns
    df = df.drop(columns_to_remove, axis=1)

    # Display the modified dataframe
    st.dataframe(df)

    # Allow the user to download the modified CSV
    st.markdown("""
    ## Download modified CSV
    """)
    if st.button("Download modified CSV"):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="modified.csv">Download modified CSV file</a>'
        st.markdown(href, unsafe_allow_html=True)
