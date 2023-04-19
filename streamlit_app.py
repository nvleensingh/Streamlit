import streamlit as st


st.title("Largest of The Three Number")
st.text("Enter the Three numbers and find the Largest amongest them")
st.write(" ")

num1 = st.number_input("Enter the Number 1: ", value = 0)
num2 = st.number_input("Enter the Number 2: ", value = 0)
num3 = st.number_input("Enter the Number 3: ", value = 0)


def largest_calculator(a,b,c):
    if(num1 == num2 == num3):
        st.write("The numbers are Equal and The Number is: ",num1)
    else:
#         return("The Largest number is:", max(num1,num2,num3))
        st.write("The Largest number is: ", max(num1,num2,num3))
    

if(st.button("Check")):
    st.write(largest_calculator(num1,num2,num3))
else:
    st.write("Press The Button!!")
