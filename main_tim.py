import streamlit as st


def result(data):
    name = []
    x = []
    for line in data:

        data = line.rstrip().split(',')

        if data[1] == "1":
            if data[6] < "18" and data[5] != "age":
                name = data[3]
                x.append(name)

    return x


def result2(data):
    male = []

    x2 = []

    for line in data:
        data = line.rstrip().split(',')

        if data[1] == "1":
            if data[6] < "18" and data[5] != "age":
                male = data[5]

                x2.append(male)

    return x2


def result3(data):
    age = []

    x3 = []
    for line in data:
        data = line.rstrip().split(',')

        if data[1] == "1":
            if data[6] < "18" and data[5] != "age":

                if data[6] == "":
                    age = "неопределённ"
                    x3.append(age)
                else:
                    age = data[6]
                    x3.append(age)

    return x3


with open("data.csv") as file:
    data = file.readlines()
name = result(data)
age = result2(data)
sex = result3(data)


def func_4():
    for i in range(0, len(name)):
        st.text(name[i] + " " + " " + age[i] + " " + " " + sex[i])


func_4()
