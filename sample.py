import streamlit as st
st.set_page_config(page_title="San Portfolio",page_icon="😁")
st.title("CHINTALACHERUVU L V L SANTOSH",anchor=False)
st.subheader("Full Stack web Developer")
with st.container(border=True):
    st.info("I am engineering student who is currently studying Btech III Year")
col1,col2,col3=st.columns(3)
with col1:
    st.image("mb4.jpg",width=230)
with col2:
    with st.expander(label="Know my skills",expanded=False):
        st.warning("Hello col2")
with col3:
    with st.expander(label="Know my certifications",expanded=False):
        st.error("Hello col3")
