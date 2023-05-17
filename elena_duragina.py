import streamlit as st


def counting(file, ages):
    sum_1 = 0
    sum_2 = 0
    sum_3 = 0
    for line in file:
        lst = line.rstrip().split(",")
        if lst[6] != 'SibSp' and lst[6] != '' and lst[10]:
            if float(lst[6]) in range(ages[0], ages[1] + 1):
                if lst[2] == "1":
                    sum_1 += float(lst[10])
                elif lst[2] == "2":
                    sum_2 += float(lst[10])
                elif lst[2] == "3":
                    sum_3 += float(lst[10])
    return sum_1, sum_2, sum_3


def func_3():
    st.title('Программная инженерия. Практическая работа №9')
    st.subheader(
        'Вариант №14: Найти суммарную стоимость билетов по каждому классу обслуживания среди людей с указанным возрастом')
    ages = st.slider('Укажите возраст:', 0, 100, (25, 75))
    with open("data.csv") as file:
        sum_1, sum_2, sum_3 = counting(file, ages)

    st.text_input("Стоимость билетов 1 класса:", round(sum_1, 2))
    st.text_input("Стоимость билетов 2 класса:", round(sum_2, 2))
    st.text_input("Стоимость билетов 3 класса:", round(sum_3, 2))
