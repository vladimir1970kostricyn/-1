import streamlit as st


def func_4():
    with open('data.csv') as file:
        i = 0
        age = []
        name = []
        male = []
        for line in file:
            survived = line.rstrip().split(',')
            if survived[1] == "1":
                if survived[6] < "18" and survived[5] != "age":

                    name = survived[3]
                    male = survived[5]

                    if survived[6] == "":
                        age = "неопределённ"
                    else:
                        age = survived[6]

                    st.success(f" имя {name}"+ f" возраст {age}"+ f" пол {male}")
