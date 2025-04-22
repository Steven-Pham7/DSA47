
############################################################################
# Steven code below, download necessary modules thru the YT tutorial linked below
# DONT FORGET TO DO "streamlit run ./main.py" BEFORE RUNNING or else it throws errors i think
###############################################################################
# Tutorial used:
# https://www.youtube.com/watch?v=o8p7uQCGD0U&t=625s

import streamlit as st
import pandas as pd
import time
from Search_Algo import Search_Algorithims
from Data_Parsing import Data_Parser
from Data_Parsing.multiMap_data import Food_Data



st.title("DSA Group 47: Food Finder")

# Creates 2 session states
# step handles what step the user in on
# info handles what the user has inputted and saves it for this session
# without these, info would be lost due to reruns
if "step" not in st.session_state:
    st.session_state.step = 1
if "info" not in st.session_state:
    st.session_state.info = []
if "infoIndex" not in st.session_state:
    st.session_state.infoIndex = []

def go_step2():
    st.session_state.step = 2

def go_step3():
    st.session_state.step = 3

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!FIX FILE PATHS
st.session_state.dataFilePath = "./Data/food.csv"
st.session_state.labelFilePath = "./Data/labels.csv"
st.session_state.data = Data_Parser.Parse_data(st.session_state.dataFilePath, st.session_state.labelFilePath, 3, 2)

# Go to the first step
if st.session_state.step == 1:

    st.subheader("Nutrient Selector (3 max)")
    # Represents the columns (nutrition)
    st.session_state.options = Data_Parser.pretitfyLabels(st.session_state.labelFilePath, 3)
    #     [
    #     "Carbohydrates",
    #     "Cholesterol",
    #     "Fiber",
    #     "Protein",
    #     "Total Sugar",
    #     "Monosaturated Fat",
    #     "Polysaturated Fat",
    #     "Saturated Fat",
    #     "Calcium",
    #     "Iron",
    #     "Magnesium",
    #     "Potassium",
    #     "Sodium (Salt)",
    #     "Vitamin A",
    #     "Vitamin B12",
    #     "Vitamin C",
    #     "Vitamin E",
    #     "Vitamin K",
    # ]

    # create dictionary we will use later
    checked = {}
    # initilizes a sesstion counter to count the number of checkboxes the user has selected
    if "counter" not in st.session_state:
        st.session_state.counter = 0
    # creates the checkboxes
    for nutrients in st.session_state.options:
        checked[nutrients] = st.checkbox(label=nutrients, key=nutrients)

    st.session_state.counter = 0
    # clears st.sesstion_state.info to allow it to be free of any elements during the append
    st.session_state.info.clear()
    st.session_state.infoIndex.clear()
    # incrementents the counter by the number of checkboxes selected
    for i in range(len(st.session_state.options)):
        if checked[st.session_state.options[i]]:
            st.session_state.counter += 1
            st.session_state.info.append(st.session_state.options[i])
            st.session_state.infoIndex.append(i)

    # conditionals if the user has selected a valid number of checkboxes or not
    if st.button("Submit"):
        if st.session_state.counter == 0:
            st.warning("Please select at least 1 checkbox")
        elif st.session_state.counter > 3:
            st.warning("Please select at most 3 checkboxes")
        else:
            # st.sesstion_state.step = 2 and reruns
            go_step2()
            st.rerun()

# step 2
elif st.session_state.step == 2:

    # testing for this step
    def slider_test():
        print('\n\n')
        print(f'Searching algorithm: {st.session_state.searching_Algo}')
        print(f'slider_range1: {st.session_state.slider_range1[0]} - {st.session_state.slider_range1[1]}')
        print(f'slider_range2: {st.session_state.slider_range2[0]} - {st.session_state.slider_range2[1]}')
        print(f'slider_range3: {st.session_state.slider_range3[0]} - {st.session_state.slider_range3[1]}')
        print(f'slider_range1 range: {st.session_state.slider_range1[1] - st.session_state.slider_range1[0]} , maximum range allowed: {max_value[st.session_state.info[0]] / 4.0}')
        print(f'slider_range2 range: {st.session_state.slider_range2[1] - st.session_state.slider_range2[0]} , maximum range allowed: {max_value[st.session_state.info[1]] / 4.0}')
        print(f'slider_range3 range: {st.session_state.slider_range3[1] - st.session_state.slider_range3[0]} , maximum range allowed: {max_value[st.session_state.info[2]] / 4.0}')

    # if searching goes wrong, recheck max values to see if they are exact
    # dictionary of the columns max values
    # all values are floats, true values are commented if they were reduced to 1 decimal place
    max_value = Data_Parser.getMaxValues(st.session_state.data, st.session_state.options, 0)
    # max_value["Carbohydrates"] = 100.0
    # max_value["Cholesterol"] = 3074.0
    # max_value["Fiber"] = 46.2
    # # 78.13
    # max_value["Protein"] = 78.2
    # max_value["Total Sugar"] = 99.8
    # # 75.221
    # max_value["Monosaturated Fat"] = 75.3
    # # 67.849
    # max_value["Polysaturated Fat"] = 67.9
    # max_value["Saturated Fat"] = 82.5
    # max_value["Calcium"] = 1375.0
    # max_value["Iron"] = 64.1
    # max_value["Magnesium"] = 611.0
    # max_value["Potassium"] = 6040.0
    # max_value["Sodium (Salt)"] = 7851.0
    # max_value["Vitamin A"] = 9363.0
    # # 82.5
    # max_value["Vitamin B12"] = 82.5
    # max_value["Vitamin C"] = 560.0
    # max_value["Vitamin E"] = 149.4
    # max_value["Vitamin K"] = 1640.0

    # creates a form where it doesn't rerun when value changes.
    # when user submits, then it changes
    with st.form(key="user_submit_form"):

        if "slider_range1" not in st.session_state:
            st.session_state.slider_range1 = ()
        if "slider_range2" not in st.session_state:
            st.session_state.slider_range2 = ()
        if "slider_range3" not in st.session_state:
            st.session_state.slider_range3 = ()
        # STORES THE SEARCHING ALGORITHM BEING USED
        if "searching_Algo" not in st.session_state:
            st.session_state.searching_Algo = ""

        st.subheader("Range + Searching Algorithm Input")
        st.write("Please input desired nutritional value ranges and select a searching algorithm")
        st.divider()
        
        # searching algorithm that will be used
        st.session_state.searching_Algo = st.radio("Choose a searching algorithm", ["Jump Search", "Exponential Search"])

        # conditionals to properly output the number of sliders depending on the number of checkboxes selected
        # saves the values of the sliders separate lists
        st.session_state.slider_range1 = st.slider(st.session_state.info[0], value=[0.0,max_value[st.session_state.info[0]]])
        if len(st.session_state.info) == 2:
            st.session_state.slider_range2 = st.slider(st.session_state.info[1], value=[0.0,max_value[st.session_state.info[1]]])
        if len(st.session_state.info) == 3:
            st.session_state.slider_range2 = st.slider(st.session_state.info[1], value=[0.0,max_value[st.session_state.info[1]]])     
            st.session_state.slider_range3 = st.slider(st.session_state.info[2], value=[0.0,max_value[st.session_state.info[2]]])

        # when user submits, it will save the things into the session_state variables
        submit_button = st.form_submit_button(label="Submit")
        if submit_button:
            if len(st.session_state.info) == 1:
                if st.session_state.slider_range1[1] - st.session_state.slider_range1[0] >= max_value[st.session_state.info[0]] / 4.0:
                    st.warning(f"Please reduce the range for the {st.session_state.info[0]} slider")
                else:
                    #slider_test()
                    go_step3()
                    st.rerun()
            elif len(st.session_state.info) == 2:
                if st.session_state.slider_range1[1] - st.session_state.slider_range1[0] >= max_value[st.session_state.info[0]] / 4.0:
                    st.warning(f"Please reduce the range for the {st.session_state.info[0]} slider")
                elif st.session_state.slider_range2[1] - st.session_state.slider_range2[0] >= max_value[st.session_state.info[1]] / 4.0:
                    st.warning(f"Please reduce the range for the {st.session_state.info[1]} slider")
                else:
                    #slider_test()
                    go_step3()
                    st.rerun()
            elif len(st.session_state.info) == 3:
                if st.session_state.slider_range1[1] - st.session_state.slider_range1[0] >= max_value[st.session_state.info[0]] / 4.0:
                    st.warning(f"Please reduce the range for the {st.session_state.info[0]} slider")
                elif st.session_state.slider_range2[1] - st.session_state.slider_range2[0] >= max_value[st.session_state.info[1]] / 4.0:
                    st.warning(f"Please reduce the range for the {st.session_state.info[1]} slider")
                elif st.session_state.slider_range3[1] - st.session_state.slider_range3[0] >= max_value[st.session_state.info[2]] / 4.0:
                    st.warning(f"Please reduce the range for the {st.session_state.info[2]} slider")
                else:
                    slider_test()
                    go_step3()
                    st.rerun()

# step 3
elif st.session_state.step == 3:

    # option_index = {}
    # option_index["Carbohydrates"] = 0
    # option_index["Cholesterol"] = 1
    # option_index["Fiber"] = 2
    # option_index["Protein"] = 3
    # option_index["Total Sugar"] = 4
    # option_index["Monosaturated Fat"] = 5
    # option_index["Polysaturated Fat"] = 6
    # option_index["Saturated Fat"] = 7
    # option_index["Calcium"] = 8
    # option_index["Iron"] = 9
    # option_index["Magnesium"] = 10
    # option_index["Potassium"] = 11
    # option_index["Sodium (Salt)"] = 12
    # option_index["Vitamin A"] = 13
    # option_index["Vitamin B12"] = 14
    # option_index["Vitamin C"] = 15
    # option_index["Vitamin E"] = 16
    # option_index["Vitamin K"] = 17

    if "list1" not in st.session_state:
        st.session_state.list1 = ()
    if "list2" not in st.session_state:
        st.session_state.list2 = ()        
    if "list3" not in st.session_state:
        st.session_state.list3 = ()
    if "data_Frame" not in st.session_state:
        st.session_state.data_frame = pd.DataFrame()
        

    st.write("need output")
    if st.session_state.searching_Algo == "Jump Search":
        st.session_state.list1 = Search_Algorithims.search_nutrient(st.session_state.infoIndex[0], st.session_state.slider_range1, "Jump", st.session_state.data)
        for something in st.session_state.list1:
            temp = pd.DataFrame([st.session_state.data.get_data(something)])
            st.session_state.data_frame = pd.concat([st.session_state.data_frame, temp])
    elif st.session_state.searching_Algo == "Exponential Search":
        st.session_state.list1 = Search_Algorithims.search_nutrient(st.session_state.infoIndex[0], st.session_state.slider_range1, "Exponential", st.session_state.data)

    st.dataframe(st.session_state.data_frame)