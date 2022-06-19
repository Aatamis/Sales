import pickle
import numpy as np
import streamlit as st

model = pickle.load(open(r'C:/Users/hp/Desktop/NHEF Projects/model_NHEF','rb'))
#model = pickle.load(open('model_pkl','rb'))

st.title("NHEF SALES TOOL")
st.write('Hello, World! The purpose of this App is to allow team members from the marketing team the opportunity to input key KYC data into the system and have it produce the most likely estate potential clients will buy a plot from. Currently, we are selling plots for the Chibombo and Riverdale Estates. By utilizing this App, team members will be able to segment their marketing efforts and target the most likely group or individuals in their efforts to sell land')

html_temp = """
<div style ="background-color:#800080 ;padding:10px">
<h2 style="color:white;text-align:center;">Estate Predictor ML App</h2>
</div>
"""


#background styling
page_bg = '''
<style>
body {
background-color : #f4f4f4;
}
</style>
'''
st.markdown(page_bg, unsafe_allow_html=True)


st.markdown(html_temp, unsafe_allow_html=True)
Location = st.text_input("Location", placeholder="Central: 1, Copperbelt: 2, Eastern: 3, Luapula: 4, "
                                                 "Lusaka: 5, Muchinga: 6,North-Western: 7,North-Western: 8, Southern: 9, Western: 10")
Gender = st.text_input("Gender", placeholder="Male = 1, Female = 2")
Age = st.text_input("Age")
EstimatedSalary = st.text_input("EstimatedSalary")

safe_html = """
<div style ="background-color:#FFFF00;padding:10px>
<h2 style="color:white; text-align:center;">Customer will not exit</h2>
</div>
"""
danger_html = """
<div style ="background-color:#F4D03F;padding:10px>
<h2 style="color:white; text-align:center;">Customer will exit</h2>
</div>
"""


def predict_cust(Location, Gender, Age, EstimatedSalary):
    input = np.array([[Location, Gender,Age, EstimatedSalary]]).astype(np.float64)
    prediction = model.predict_proba(input)
    pred = np.argmax(prediction)
    return pred


if st.button('Predict'):
    makeprediction = model.predict([[Location,Gender,Age,EstimatedSalary,]])
    output=round(makeprediction[0],2)
    st.success('Customer fits the Chibombo Profile {}'.format(output))

else:
    st.write('Customer fits the Riverdale Profile!')

st.write('www.nhef.co.zm')

#if st.button("Predict"):
    #output = predict_cust(Location, Gender, Age, EstimatedSalary)
    #st.success("The verdict{}".format(output))


 #   if output == 1:
  #      st.markdown(Chibombo_html, unsafe_allow_html=True)
   # else:
    #    st.markdown(Riverdale_html, unsafe_allow_html=True)