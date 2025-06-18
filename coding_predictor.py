import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
      

data=pd.read_csv("student_coding_data.csv")
x=data.drop("skill_level",axis=1)
le=LabelEncoder()
y=le.fit_transform(data["skill_level"])

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model=RandomForestClassifier()
model.fit(x_train,y_train)

st.title("🚀 Student Coding Skill Predictor")
st.write("📌 Note: *Being marked 'Advanced' means you're ready to learn advanced topics — not an expert yet!*")

leetcode_total=st.number_input("🧠 LeetCode Total Problems Solved", 0, 1000)
gfg_count=st.number_input("📘 GeeksforGeeks Problems Solved", 0, 500)
codechef_rating=st.number_input("🏆 CodeChef Rating", 800, 2000)
hackerrank_badges=st.number_input("🎖️ HackerRank Badges", 0, 20)

if st.button("🔍 Predict My Coding Skill Level"):
    input_data=np.array([[leetcode_total,gfg_count,codechef_rating,hackerrank_badges]])
    prediction=model.predict(input_data)[0]
    result=le.inverse_transform([prediction])[0]
    st.success(f"💡 Your predicted level: **{result}**")

if st.button("📈 Show Model Accuracy"):
    y_pred=model.predict(x_test)
    acc=accuracy_score(y_test,y_pred)*100
    st.info(f"✅ Model Accuracy: **{acc:.2f}%** (on test data)")   
        



