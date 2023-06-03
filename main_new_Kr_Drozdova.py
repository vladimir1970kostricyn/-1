import streamlit as st

st.title("Программная инженерия. Практическая работа 9")
st.subheader("Найти количество мужчин и женщин по указанному классу обслуживания")


def result1(data):
    male = 0
    female = 0
    for line in data:
        lst = line.rstrip().split(",")
        if lst[2] == "1":
            if lst[5] == 'male':
                male += 1
            else:
                female += 1
    return male, female


def result2(data):
    male2 = 0
    female2 = 0
    for line in data:
        lst = line.rstrip().split(",")
        if lst[2] == "2":
            if lst[5] == 'male':
                male2 += 1
            else:
                female2 += 1
    return male2, female2


def result3(data):
    male3 = 0
    female3 = 0
    for line in data:
        lst = line.rstrip().split(",")
        if lst[2] == "3":
            if lst[5] == 'male':
                male3 += 1
            else:
                female3 += 1
    return male3, female3


def one_func():
    var = st.selectbox(
        label="Выберите класс обслуживания:",
        options=["1", "2", "3"]
    )
    with open("data.csv") as file:
        data = file.readlines()
    if var == "1":
        st.success("Мужчин, девушек в первом классе")
        st.success(str(result1(data)))
    elif var == "2":
        st.success("Мужчин, девушек в втором классе")
        st.success(str(result2(data)))
    elif var == "3":
        st.success("Мужчин, девушек в третьем классе")
        st.success(str(result3(data)))


one_func()
