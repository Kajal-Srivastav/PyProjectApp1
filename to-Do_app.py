import streamlit as st
import functions

fdata = functions.get_data()


def add_items():
    new_value = st.session_state["new_item"] + "\n"
    fdata.append(new_value)
    functions.get_write(fdata)


st.title("My todo App")
st.subheader("This is my todo application ")
st.write("Enter the value to add this value in the list .")

st.text_input(label="Enter the value to add" , placeholder = "Add value .....", on_change=add_items,  key="new_item")

'''in this for loop st.checkbox  is creating a check for all i val 
like it item is "hi kajal " so it will add this item to check box item
'''
for index , i in enumerate(fdata):
    check_val = st.checkbox(i , key=i)
    if check_val:
        fdata.pop(index)
        functions.get_write(fdata)
        del st.session_state[i]
        st.experimental_rerun()
