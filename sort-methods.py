class Sorter:
    def bubble_sort(self, data, swapped=True):
        if swapped is True:
            data, swapped = self.compare_indexes(0, 1, data, False)
            self.bubble_sort(data, swapped)
        return data

    def compare_indexes(self, a, b, data, swapped):
        if data[a] > data[b]:
            data[a], data[b] = data[b], data[a]
            swapped = True
        if b + 1 < len(data):
            return self.compare_indexes(b, b + 1, data, swapped)
        if b + 1 == len(data):
            return data, swapped

    @staticmethod
    def quick_sort(data, pivot=0, current_index=1):
        if pivot < len(data):
            for i in range(pivot, len(data)):
                if data[i] < data[pivot]:
                    data[i], data[current_index] = data[current_index], data[i]
                    data[pivot], data[current_index] = data[current_index], data[pivot]
                    current_index += 1
            if current_index - pivot > 1:
                Sorter.quick_sort(data, pivot, pivot + 1)
            else:
                Sorter.quick_sort(data, pivot + 1, current_index + 1)
        return data

# Create Sorter
sorter = Sorter()

# Bubble Sort
nums = [8, 3, 2, 1, 5, 200, 15, 3, 5, 26, 18, 33, 7, 6, 4]
print('bubble sort:', sorter.bubble_sort(nums))

# Quick Sort
nums2 = [8, 3, 2, 1, 5, 200, 15, 26, 18, 7, 33, 6, 34]
print('quick sort:', Sorter.quick_sort(nums2))