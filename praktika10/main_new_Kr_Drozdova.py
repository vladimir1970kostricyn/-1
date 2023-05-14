import streamlit as st

st.title("Программная инженерия. Практическая работа 9")
st.subheader("Найти количество мужчин и женщин по указанному классу обслуживания")


def one_func():
    male = 0
    female = 0
    with open("data.csv") as file:
        var = st.selectbox(
            label="Выберите класс обслуживания:",
            options=["Первый", "Второй", "Третий"]
        )
        for line in file.readlines()[1:]:
            lst = line.rstrip().split(",")
            if var == "Первый" and lst[2] == "1":
                if lst[5] == 'male':
                    male += 1
                else:
                    female += 1
            elif var == "Второй" and lst[2] == "2":
                if lst[5] == 'male':
                    male += 1
                else:
                    female += 1
            elif var == "Третий" and lst[2] == "3":
                if lst[5] == 'male':
                    male += 1
                else:
                    female += 1
        if var == "Первый":
            st.success("В первом классе мужчин: " + str(male) + ", женщин: " + str(female))
        elif var == "Второй":
            st.success("Во втором классе мужчин: " + str(male) + ", женщин: " + str(female))
        elif var == "Третий":
            st.success("В треьем классе мужчин: " + str(male) + ", женщин: " + str(female))
