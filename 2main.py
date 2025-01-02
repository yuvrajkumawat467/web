import  streamlit as st

st.title('Improve your skills')
st.header('Achieve your target')
st.subheader('Prepare your mindset')
st.text("By ...UV...")
st.markdown("### This is a markdown")
st.success('Success')
st.info('Information')
st.warning('Warning')
st.error('Error')
exp = ZeroDivisionError("Trying to divide by zero")
st.exception(exp)
st.write("Text with write")
st.write(range(10))
status = st.radio("Select Gender:", ("Male", "Female"))
if status == "Male":
    st.success('Male')
else:
    st.success('Female')
hobby = st.selectbox("Hobbies:",
                     ['Dancing', 'Reading', 'Singing', 'Sports'])
st.write("Your hobby is:",hobby)
hobbies = st.multiselect("Hobbies:",
                         ['Dancing', 'Reading', 'Singing', 'Sports'])
st.write("You selected", len(hobbies),'hobbies')
st.button("Click me for no reason")
if st.button("About"):
    st.text("You are so genius")
name = st.text_input("Enter your name")
if st.button('Submit'):
    result = name.title()
    st.success(result)
level = st.slider('select the level',1,10)
st.text('Selected: {}'.format(level))



