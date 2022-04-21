import streamlit as st

st.title('st.experimental_get_query_params')

# Contents of st.experimental_get_query_params
st.header('Contents of st.experimental_get_query_params')

st.markdown('''
In the above URL bar of your internet browser, append the following:

`?name=Jack&surname=Beanstalk`

after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`

such that it becomes 

`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')

st.write(st.experimental_get_query_params())


# Retrieving and displaying information from the URL
st.header('Retrieving and displaying information from the URL')

firstname = st.experimental_get_query_params()['firstname'][0]
surname = st.experimental_get_query_params()['surname'][0]

st.write(f'Hello **{firstname} {surname}**, how are you?')
