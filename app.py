import time
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

class App:

    def __init__(self):
        self.section0 = None
        self.section1 = None
        self.section2 = None
        self.section3 = None

        self.times0 = np.array([])
        self.times1 = np.array([])
        self.times2 = np.array([])
        self.times3 = np.array([])
        self.times4 = np.array([])

    def main(self):

        st.set_page_config(layout="centered", page_title="Algorithm Speed", page_icon="📊")
        hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                </style>
                """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

        st.header("Execution Time of Sorting Algorithms")

        self.section0 = st.container()

        list_size = self.section0.number_input("Enter the size of list", min_value=1, max_value=1000000, step=1)
        mean = self.section0.number_input("Enter the mean of Normal Distribution", min_value=-100, max_value=100, step=1, )
        std_dev = self.section0.number_input("Enter the standard deviation of Normal Distribution", min_value=1, max_value=10, step=1)
        one_to_n = self.section0.checkbox(f"From 1 to {list_size}")
        self.section0.divider()

        self.section1 = st.container()
        
        self.section1.subheader("Select Sorting Algorithms:")
        col1, col2 = self.section1.columns([1,1], gap="medium", vertical_alignment="center")
        algos = [col1.checkbox("Bubble Sort", value=False),
                col1.checkbox("Selection Sort", value=False),
                col1.checkbox("Insertion Sort", value=False),
                col2.checkbox("Merge Sort", value=False),
                col2.checkbox("Quick Sort", value=False)]
        
        self.section1.divider()

        _, col, _  = self.section1.columns([1,1,1], gap="medium", vertical_alignment="center")

        col.button("Execute Sorting", on_click = self.generate_list, args=(list_size, mean, std_dev, algos, one_to_n), type="primary", use_container_width=True)
        
        self.section2 = st.container()

        self.section2.divider()

        self.section3 = st.container()

        

# -----------------------------------------------

    def generate_list(self, list_size, mean, std_dev, algos, one_to_n):

        for selection in algos:
            if selection:
                if not one_to_n:
                    self.section2.subheader("Probability Density of the Data")
                    list = np.random.normal(mean, std_dev, list_size)
                    fig, ax = plt.subplots()
                    ax.set_xlabel("Data Values")
                    ax.set_ylabel("Probability")
                    ax.hist(list, density=True, bins=max(list_size//200,20))
                    self.section2.pyplot(fig)
                    self.execute_sorting(list, algos, one_to_n)
                    break
                else:
                    percent_complete = 0
                    progress_text = f"List Sorting in Progress ({percent_complete}%)"
                    my_bar = self.section3.progress(percent_complete, text=progress_text)
                    for i in range(1,list_size+1):
                        list = np.random.normal(mean, std_dev, i)
                        self.execute_sorting(list, algos, one_to_n)
                        percent_complete = int((i/(list_size+1))*100)
                        progress_text = f"List Sorting in Progress ({percent_complete}%)"
                        my_bar.progress(min(percent_complete,100), text=progress_text)
                    my_bar.empty()
                    self.plot_graph([], one_to_n)
                    break

# -----------------------------------------------

    def execute_sorting(self, list, algos, one_to_n):
        if not one_to_n:
            percent_complete = 0
            progress_text = f"List Sorting in Progress ({percent_complete}%)"
            my_bar = self.section3.progress(percent_complete, text=progress_text)
            times = np.array([0,0,0,0,0])
            for i in range(len(algos)):
                if algos[i]:                    
                    if i == 0:
                        sum = 0
                        for _ in range(10):
                            t_start = time.time_ns() // 1000000
                            self.bubble_sort(list.copy(), list.size)
                            t_end = time.time_ns() // 1000000
                            sum += t_end - t_start
                        times[i] = sum / 10
                    elif i == 1:
                        sum = 0
                        for _ in range(10):
                            t_start = time.time_ns() // 1000000
                            self.selection_sort(list.copy(), list.size)
                            t_end = time.time_ns() // 1000000
                            sum += t_end - t_start
                        times[i] = sum / 10    
                    elif i == 2:
                        sum = 0
                        for _ in range(10):
                            t_start = time.time_ns() // 1000000
                            self.insertion_sort(list.copy(), list.size)
                            t_end = time.time_ns() // 1000000
                            sum += t_end - t_start
                        times[i] = sum / 10
                    elif i == 3:
                        sum = 0
                        for _ in range(10):
                            t_start = time.time_ns() // 1000000
                            self.merge_sort(list.copy(), list.size)
                            t_end = time.time_ns() // 1000000
                            sum += t_end - t_start
                        times[i] = sum / 10
                    else:
                        sum = 0
                        for _ in range(10):
                            t_start = time.time_ns() // 1000000
                            self.quick_sort(list.copy(), list.size)
                            t_end = time.time_ns() // 1000000
                            sum += t_end - t_start
                        times[i] = sum / 10
                percent_complete += 20
                progress_text = f"List Sorting in Progress ({percent_complete}%)"
                my_bar.progress(percent_complete, text=progress_text)
            my_bar.empty()
            
            for selection in algos:
                if selection:
                    self.plot_graph(times, one_to_n)
                    break
        else:
            for i in range(len(algos)):
                if algos[i]:
                    if i == 0:
                        sum = 0
                        for _ in range(10):
                            t_start = time.time_ns() // 1000
                            self.bubble_sort(list.copy(), list.size)
                            t_end = time.time_ns() // 1000
                            sum = sum + t_end - t_start
                        self.times0 = np.append(arr=self.times0, values=sum/10)
                    elif i == 1:
                        sum = 0
                        for _ in range(10):
                            t_start = time.time_ns() // 1000
                            self.selection_sort(list.copy(), list.size)
                            t_end = time.time_ns() // 1000
                            sum = sum + t_end - t_start
                        self.times1 = np.append(arr=self.times1, values=sum/10)
                    elif i == 2:
                        sum = 0
                        for _ in range(10):
                            t_start = time.time_ns() // 1000
                            self.insertion_sort(list.copy(), list.size)
                            t_end = time.time_ns() // 1000
                            sum = sum + t_end - t_start
                        self.times2 = np.append(arr=self.times2, values=sum/10)
                    elif i == 3:
                        sum = 0
                        for _ in range(10):
                            t_start = time.time_ns() // 1000
                            self.merge_sort(list.copy(), list.size)
                            t_end = time.time_ns() // 1000
                            sum = sum + t_end - t_start
                        self.times3 = np.append(arr=self.times3, values=sum/10)
                    else:
                        sum = 0
                        for _ in range(10):
                            t_start = time.time_ns() // 1000
                            self.quick_sort(list.copy(), list.size)
                            t_end = time.time_ns() // 1000
                            sum = sum + t_end - t_start
                        self.times4 = np.append(arr=self.times4, values=sum/10)                        

# -----------------------------------------------

    def plot_graph(self, times, one_to_n):
        self.section3.subheader("Comparison of execution time of Sorting Algorithms")
        if not one_to_n:
            fig, ax = plt.subplots()
            x=["Bubble Sort","Selection Sort","Insertion Sort","Merge Sort","Quick Sort"]
            ax.bar(x, height=times)
            max_time = np.max(times)
            plt.ylim(0, max_time+max_time//10+10)
            plt.ylabel("Time (milliseconds)")
            plt.xticks(rotation=45)
            for i in range(len(x)):
                plt.text(i, times[i], times[i], ha = 'center')
            self.section3.pyplot(fig)
        else:
            fig, ax = plt.subplots()
            if len(self.times0) != 0:
                ax.plot(self.times0, linestyle="solid", linewidth=1, label="Bubble Sort", alpha=0.7)
            if len(self.times1) != 0:
                ax.plot(self.times1, linestyle="solid", linewidth=1, label="Selection Sort", alpha=0.7)
            if len(self.times2) != 0:
                ax.plot(self.times2, linestyle="solid", linewidth=1, label="Insertion Sort", alpha=0.7)
            if len(self.times3) != 0:
                ax.plot(self.times3, linestyle="solid", linewidth=1, label="Merge Sort", alpha=0.7)
            if len(self.times4) != 0:
                ax.plot(self.times4, linestyle="solid", linewidth=1, label="Quick Sort", alpha=0.7)
            plt.legend()
            plt.ylabel("Time (microseconds)")
            plt.xlabel("Input Size")
            self.section3.pyplot(fig)
    
# -----------------------------------------------

    def bubble_sort(self, list, n):
        for i in range(n-1):
            for j in range(n-i-1):
                if (list[j] > list[j+1]):
                    temp = list[j]
                    list[j] = list[j+1]
                    list[j+1] = temp

# -----------------------------------------------

    def selection_sort(self, list, n):
        for i in range(n):
            minIndex = i
            for j in range(n-i):
                if list[j] < list[minIndex]:
                    minIndex = j
            temp = list[minIndex]
            list[minIndex] = list[n-1-i]
            list[n-1-i] = temp

# -----------------------------------------------

    def insertion_sort(self, list, n):
        if n <= 1:
            return
        for i in range(1, n):
            key = list[i]
            j = i-1
            while j >= 0 and key < list[j]:
                list[j+1] = list[j]
                j -= 1
            list[j+1] = key

# -----------------------------------------------

    def merge(self, list, low, mid, high):
        i = low
        j = mid+1
        k = 0
        copy_list = []
        while i <= mid and j <= high:
            if list[i] <= list[j]:
                copy_list.insert(k, list[i])
                i += 1
            else:
                copy_list.insert(k, list[j])
                j += 1
            k += 1
        while i <= mid:
            copy_list.insert(k, list[i])
            i += 1
            k += 1
        while j <= high:
            copy_list.insert(k, list[j])
            j += 1
            k += 1
        for i in range(low,high+1):
            list[i] = copy_list[i-low]

    def divide(self, list, low, high):
        if (low >= high):
            return list
        else:
            mid = (low+high)//2
            self.divide(list, low, mid)
            self.divide(list, mid+1, high)
            self.merge(list, low, mid, high)

    def merge_sort(self, list, n):
        self.divide(list, 0, n-1)

# -----------------------------------------------

    def partition(self, list, low, high):
        pivot = list[low]
        i = low
        j = high

        while i < j:
            while i < j and list[i] <= pivot:
                i += 1
            while j >= 0 and list[j] > pivot:
                j -= 1
            if i < j:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
        temp = list[low]
        list[low] = list[j]
        list[j] = temp
        return j

    def sort(self, list, low, high):
        if (low >= high):
            return list
        else:
            partitionIndex = self.partition(list, low, high)
            self.sort(list, low, partitionIndex-1)
            self.sort(list, partitionIndex+1, high)

    def quick_sort(self, list, n):
        self.sort(list, 0, n-1)

# -----------------------------------------------

if __name__ == "__main__":
    app = App()
    app.main()
