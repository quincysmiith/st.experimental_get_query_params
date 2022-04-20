import streamlit as st

st.title('st.experimental_get_query_params')

st.header('Contents of st.experimental_get_query_params')
st.write(st.experimental_get_query_params)

st.markdown('''
In the above URL bar of your internet browser, append at the end of the URL the following:

`?name=Jack&surname=Database`
''')
