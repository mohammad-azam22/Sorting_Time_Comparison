# Sorting Algorithm Execution Time Comparison

## Overview
This web application compares the execution time of various sorting algorithms. The algorithms included are:
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort

The results are presented in two forms:
1. **Bar Graph**: Displays execution time for a single input size.
2. **Line Graph**: Shows execution time for input sizes ranging from 1 to N (for a selected value of N).

## Features
- **User-Friendly Interface**: Easily select sorting algorithms and input sizes.
- **Normal Distribution**: The data generated for sorting is Normally Distributed.
- **Graphical Representation**: Clear and intuitive bar and line graphs.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/mohammad-azam22/Sorting_Time_Comparison.git
    ```
2. Install the libraries:
   ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Start the application:
    ```bash
    streamlit run app.py
    ```
2. Streamlit will automatically open the applicaiton at `http://localhost:8501`.

## How It Works
1. **Input Size**: Enter the size of the input array.
2. **Input Mean**: Enter the Mean of the Normal Distribution.
3. **Input Standard Deviaiton**: Enter the Standard Deviation of the Normal Distribution.
4. **Select Algorithms**: Choose the sorting algorithms you want to compare.
5. **1 to N**: Select whether you want to compare the algorithms for every input from 1 to N.
6. **Run Comparison**: Click the "Compare" button to execute the algorithms and display the results.
7. **View Results**: Analyze the execution times in the graphical representation.

## Technologies Used
- **Frontend**: Streamlit
- **Backend**: Python, NumPy
- **Visualization**: Matplotlib

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
---
Happy Sorting!
