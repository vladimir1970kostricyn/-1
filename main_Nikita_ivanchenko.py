import streamlit as st

st.title("Программная инженерия. Практическая работа 9")
st.subheader("Найти количество мужчин и женщин по указанному классу обслуживания")


def two_func():
    summa = 0
    d2 = 0
    fares = []
    with open("data.csv") as file:
        count = 0
        for line in file:
            data = line.rstrip().split(',')
            if data[5] == "male":
                d2 += 1
                if data[9] != "fare":
                    fare = float(data[10])
                    summa += fare
                    fares += [fare]
    avg = summa / d2

    var = st.selectbox(
        label="Выберите цену обслуживания:",
        options=["Первый", "Второй", "Третий"]
    )

    if var == "Первый":
        st.success(min(fares))
        print(f'Минимальная цена билета = {min(fares)}')
    elif var == "Второй":
        st.success(max(fares))
        print(f'Максимальная цена билета = {max(fares)}')
    else:
        st.success(avg)
        print(f'Средняя цена билета = {avg}')
