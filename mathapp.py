import streamlit as st
st.set_page_config(page_title="mathapp",page_icon="😊")
st.title("prime Number or not")
a=st.text_input(label="Enter the Value")
if st.button("Submit"):
    try:
        num=int(a)
        f=0
        if num<=0:
            st.write("please enter correct number")
        elif num==1:
            st.write("Neither prime nor not-prime")
        else:
            for i in range(2,num):
                if num%i==0:
                    f=1
                    break 
            if f==0:
                st.write("Prime")
            else:
                st.write("Not prime")
    except ValueError:
        st.write("Please enter correct number")
                
            
       