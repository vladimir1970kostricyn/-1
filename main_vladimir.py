import streamlit as st

st.title("Программная инженерия. Практическая работа 9")
st.subheader("Посчитать долю пассажиров Титаника, указав: вести поиск среди спасенных или погибших, искать в возрастных группах до 30 лет или старше 60 лет")






def avg30_avg60(data):
    avg30 = 0
    avg60 = 0
    for line in data:
        survived = line.rstrip().split(",")
        if survived[1] == '1':
            if survived[6] < '30':
                avg30 += 1
            if survived[6] > '60':
                avg60 += 1
    return avg60, avg30

def unsurv(data):
    unsurv30 = 0
    unsurv60 = 0
    for line in data:
        unsurvived = line.rstrip().split(",")
        if unsurvived[1] == '0':
            if unsurvived[6] < '30':
                unsurv30 += 1
            if unsurvived[6] > '60':
                unsurv60 += 1
    return unsurv30, unsurv60
def func_5():
    with open("data.csv") as file:
        data = file.readlines()
    choice = st.radio("Среди кого вести поиск?:", ['среди спасенных', 'среди погибших'])
    if choice == 'среди спасенных':
        st.success("Спасенные пассажиры Титиника(первое число старше 60 второе моложе 30)")
        st.success(avg30_avg60(data))
    else:
        st.warning("Погибшие пассажиры Титаника(первое число старше 60 второе моложе 30)")
        st.warning(unsurv(data))
func_5()
