import numpy as np

class DataAnalytics:
    def __init__(self, data=None):
        # Array initialize karne ke liye constructor
        if data is not None:
            self.__array = np.array(data)  # Encapsulation / Private attribute
        else:
            self.__array = None

    # Array get karne ke liye getter method
    def get_array(self):
        return self.__array

    # Array set karne ke liye setter method
    def set_array(self, arr):
        self.__array = np.array(arr)

    # 1. Array Creation (Static method utility ke roop me)[cite: 1, 2]
    @staticmethod
    def create_array(dim, shape, elements):
        arr = np.array(elements)
        return arr.reshape(shape)

    # 2. Indexing aur Slicing[cite: 1, 3]
    def index_element(self, indices):
        return self.__array[tuple(indices)]

    def slice_array(self, row_slice=None, col_slice=None):
        if self.__array.ndim == 1:
            return self.__array[row_slice]
        return self.__array[row_slice, col_slice]

    # 3. Mathematical Operations[cite: 1, 3]
    def add(self, other_arr):
        return self.__array + other_arr

    def subtract(self, other_arr):
        return self.__array - other_arr

    def multiply(self, other_arr):
        return self.__array * other_arr

    def divide(self, other_arr):
        return self.__array / other_arr

    def matrix_multiply(self, other_arr):
        return np.dot(self.__array, other_arr)

    # 4. Combining aur Splitting[cite: 1]
    def combine(self, other_arr, axis=0):
        return np.concatenate((self.__array, other_arr), axis=axis)

    def split(self, num_splits, axis=0):
        return np.array_split(self.__array, num_splits, axis=axis)

    # 5. Search, Sort, aur Filter[cite: 1]
    def search(self, value):
        return np.where(self.__array == value)

    def sort_array(self, ascending=True):
        sorted_arr = np.sort(self.__array, axis=None)
        if not ascending:
            sorted_arr = sorted_arr[::-1]
        return sorted_arr

    def filter_greater_than(self, threshold):
        return self.__array[self.__array > threshold]

    # 6. Aggregating aur Statistical Functions[cite: 1, 2]
    def calculate_stats(self):
        stats = {
            "Sum": np.sum(self.__array),
            "Mean": np.mean(self.__array),
            "Median": np.median(self.__array),
            "Std Dev": np.std(self.__array),
            "Variance": np.var(self.__array),
            "Min": np.min(self.__array),
            "Max": np.max(self.__array)
        }
        return stats

    def calculate_percentile(self, q):
        return np.percentile(self.__array, q)

    # Class-level method example
    @classmethod
    def info(cls):
        return "DataAnalytics Class for NumPy Data Analysis."


# --- Menu-driven UI Execution ---[cite: 2]
def main():
    analyzer = DataAnalytics()

    while True:
        print("\nWelcome to the NumPy Analyzer!")
        print("====================================")
        print("Choose an option:")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nSelect the type of array to create:")
            print("1. 1D Array\n2. 2D Array\n3. 3D Array")
            arr_type = input("Enter your choice: ")

            if arr_type == '1':
                n = int(input("Enter number of elements: "))
                elems = list(map(float, input(f"Enter {n} elements separated by space: ").split()))
                analyzer.set_array(DataAnalytics.create_array(1, (n,), elems))

            elif arr_type == '2':
                r = int(input("Enter the number of rows: "))
                c = int(input("Enter the number of columns: "))
                elems = list(map(float, input(f"Enter {r*c} elements separated by space: ").split()))
                analyzer.set_array(DataAnalytics.create_array(2, (r, c), elems))

            elif arr_type == '3':
                d1 = int(input("Enter depth: "))
                d2 = int(input("Enter rows: "))
                d3 = int(input("Enter columns: "))
                elems = list(map(float, input(f"Enter {d1*d2*d3} elements separated by space: ").split()))
                analyzer.set_array(DataAnalytics.create_array(3, (d1, d2, d3), elems))

            print("\nArray created successfully:")
            print(analyzer.get_array())

            # Indexing / Slicing sub-menu[cite: 3]
            print("\nChoose an operation:")
            print("1. Indexing\n2. Slicing\n3. Go Back")
            sub_op = input("Enter your choice: ")
            
            if sub_op == '1':
                idx = list(map(int, input("Enter index separated by space: ").split()))
                print("Element:", analyzer.index_element(idx))
            elif sub_op == '2':
                if analyzer.get_array().ndim == 2:
                    r_str = input("Enter the row range (start:end): ").split(":")
                    c_str = input("Enter the column range (start:end): ").split(":")
                    r_slice = slice(int(r_str[0]), int(r_str[1]))
                    c_slice = slice(int(c_str[0]), int(c_str[1]))
                    print("\nSliced Array:\n", analyzer.slice_array(r_slice, c_slice))

        elif choice == '2':
            if analyzer.get_array() is None:
                print("Pehle Array create karein (Option 1).")
                continue

            curr_arr = analyzer.get_array()
            print("\nChoose a mathematical operation:")
            print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Matrix Multiplication")
            math_choice = input("Enter your choice: ")

            size = curr_arr.size
            elems = list(map(float, input(f"Enter the same-size array elements ({size} elements separated by space): ").split()))
            second_arr = np.array(elems).reshape(curr_arr.shape)

            print("\nOriginal Array:\n", curr_arr)
            print("Second Array:\n", second_arr)

            if math_choice == '1':
                print("\nResult of Addition:\n", analyzer.add(second_arr))
            elif math_choice == '2':
                print("\nResult of Subtraction:\n", analyzer.subtract(second_arr))
            elif math_choice == '3':
                print("\nResult of Multiplication:\n", analyzer.multiply(second_arr))
            elif math_choice == '4':
                print("\nResult of Division:\n", analyzer.divide(second_arr))
            elif math_choice == '5':
                if curr_arr.ndim == 2 and curr_arr.shape[1] == second_arr.shape[0]:
                    print("\nResult of Matrix Multiplication:\n", analyzer.matrix_multiply(second_arr))
                else:
                    print("Matrix dimensions match nahi ho rahe multiplication ke liye.")

        elif choice == '3':
            if analyzer.get_array() is None:
                print("Pehle Array create karein.")
                continue

            print("\n1. Combine Arrays\n2. Split Array")
            cs_choice = input("Enter choice: ")
            if cs_choice == '1':
                size = analyzer.get_array().size
                elems = list(map(float, input(f"Enter array elements to combine (size {size}): ").split()))
                other = np.array(elems).reshape(analyzer.get_array().shape)
                print("\nCombined Array:\n", analyzer.combine(other, axis=0))
            elif cs_choice == '2':
                parts = int(input("Kitne parts me split karna hai: "))
                print("\nSplit result:\n", analyzer.split(parts))

        elif choice == '4':
            if analyzer.get_array() is None:
                print("Pehle Array create karein.")
                continue

            print("\n1. Search\n2. Sort\n3. Filter")
            sf_choice = input("Enter choice: ")
            if sf_choice == '1':
                val = float(input("Enter value to search: "))
                res = analyzer.search(val)
                print("Indices jahan element mila:", res)
            elif sf_choice == '2':
                print("Ascending Sort:", analyzer.sort_array(ascending=True))
                print("Descending Sort:", analyzer.sort_array(ascending=False))
            elif sf_choice == '3':
                cond = float(input("Elements greater than: "))
                print(f"Filtered (elements > {cond}):", analyzer.filter_greater_than(cond))

        elif choice == '5':
            if analyzer.get_array() is None:
                print("Pehle Array create karein.")
                continue

            print("\nOriginal Array:\n", analyzer.get_array())
            stats = analyzer.calculate_stats()
            for k, v in stats.items():
                print(f"{k}: {v}")

        elif choice == '6':
            print("\nThank you for using the NumPy Analyzer! Goodbye!")
            break

        else:
            print("Invalid choice, dubara try karein.")

if __name__ == "__main__":
    main()