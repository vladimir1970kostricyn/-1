import streamlit as st

st.title("Программная инженерия. Практическая работа 9")
st.subheader("Найти количество мужчин и женщин по указанному классу обслуживания")


def result(data):
    summa = 0
    d2 = 0
    fares = []
    count = 0
    for line in data:
        data = line.rstrip().split(',')
        if data[5] == "male":
            d2 += 1
            if data[9] != "fare":
                fare = float(data[10])
                summa += fare
                fares += [fare]
    return fares


def result2(data):
    summa = 0
    d2 = 0
    fares = []
    count = 0
    for line in data:
        data = line.rstrip().split(',')
        if data[5] == "male":
            d2 += 1
            if data[9] != "fare":
                fare = float(data[10])
                summa += fare
                fares += [fare]
    return summa


def result3(data):
    summa = 0
    d2 = 0
    fares = []
    count = 0
    for line in data:
        data = line.rstrip().split(',')
        if data[5] == "male":
            d2 += 1
            if data[9] != "fare":
                fare = float(data[10])
                summa += fare
                fares += [fare]
    return d2


with open("data.csv") as file:
    data = file.readlines()


def avg():
    summa = result2(data)
    d2 = result3(data)
    avg = summa / d2
    return avg


def two_func():
    avg()

    var = st.selectbox(
        label="Выберите цену обслуживания:",
        options=["Первый", "Второй", "Третий"]
    )

    if var == "Первый":
        st.success(min(result(data)))
        print(f'Минимальная цена билета = {min(result(data))}')
    elif var == "Второй":
        st.success(max(result(data)))
        print(f'Максимальная цена билета = {max(result(data))}')
    else:
        st.success(avg())
        print(f'Средняя цена билета = {avg()}')


two_func()
