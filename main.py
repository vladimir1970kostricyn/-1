import streamlit as st
from main_new_Kr_Drozdova import one_func
from main_Nikita_ivanchenko import two_func
from elena_duragina import func_3
from main_tim import func_4
from main_vladimir import func_5

st.title("Программная инженерия. Практическая работа 10")

func = st.selectbox(
    label="Выберите работу:",
    options=["Первый", "Второй", "Третий", "четвёртый", "пятый"]
)



if func == "Первый":
    st.title("Дроздова Кристина -13 вариант")
    one_func()
elif func == "Второй":
    st.title("вариант 15, Иванченко Никита")
    two_func()
elif func == "Третий":
    st.title("Дюрягина Елена - 14 вариант")
    func_3()
elif func == "четвёртый":
    st.title("Кишев Тимур - 1 вариант")
    func_4()
elif func == "пятый":
    st.title("Кострицын Владимир 9 вариант")
    func_5()



