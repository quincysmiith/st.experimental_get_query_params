import streamlit as st

st.title('st.experimental_get_query_params')

st.header('Contents of st.experimental_get_query_params')
st.write(st.experimental_get_query_params)

st.markdown('''
In the above URL bar of your internet browser, append the following:

`?name=Jack&surname=Beanstalk`

after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`

such that it becomes 

`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?name=Jack&surname=Beanstalk`
''')
