import streamlit as st
import pandas as pd

FMT_FLOAT = {'float_kind':lambda x: "%.3f" % x}

###########
# MAIN SCRIPT
###########

def main():
    st.title("Testing streamlit share !")

###########
# DATA
###########

    st.header("Loading data")
    uploaded_file = st.file_uploader('Select a csv file', 'csv', )

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head(10))

###########
# EDA
###########

###########
# CALL MAIN
###########
main()