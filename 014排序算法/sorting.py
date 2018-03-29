# -*- encoding: utf-8 -*-
a = [18, 2, 56, 43, 77, 11, 32, 45, 23, 10, 99]

'''
冒泡排序 Bubble Sort
它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
这个算法的名字由来是因为越大的元素会经由交换慢慢“浮”到数列的顶端，故名“冒泡排序”。
时间复杂度：O(n^2)
'''
def bubble_sort(s):
    for i in range(len(s)-1):
        for j in range(len(s)-1-i):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
    return s


'''
选择排序 Select Sort
是一种简单直观的排序算法。
它的工作原理是每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，直到全部待排序的数据元素排完。 
选择排序是不稳定的排序方法（比如序列[5， 5， 3]第一次就将第一个[5]与[3]交换，导致第一个5挪动到第二个5后面）。
时间复杂度：O(n^2)
'''
def selection_sort(s):
    for i in range(len(s)):
        min = i
        for j in range(i+1, len(s)):
            if s[j] < s[min]:
                min = j
        s[i], s[min] = s[min], s[i]
    return s


'''
插入排序 Insert Sort
插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，
是稳定的排序方法。插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，但将最后一个元素除外
（让数组多一个空间才有插入的位置），而第二部分就只包含这一个元素（即待插入元素）。在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中。
插入排序的基本思想是：每步将一个待排序的记录，按其关键码值的大小插入前面已经排序的文件中适当位置上，直到全部插入完为止。
时间复杂度：O(n^2)。
'''
def insert_sort(s):
    for i in range(1, len(s)):
        for j in range(i-1,-1,-1):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
    return s


'''
希尔排序 Shell Sort
是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。希尔排序是非稳定排序算法。
该方法因DL．Shell于1959年提出而得名。 希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
时间复杂度：O(n^1.3)
'''
def shell_sort(s):
    n = len(s)
    step = n//2
    while step >= 1:
        for i in range(0, n-step):
            for j in range(i, n-step, step):
                if s[j] > s[j+step]:
                    s[j], s[j+step] = s[j+step], s[j]
        step -= 1
    return s


'''
归并排序 Merge Sort
建立在归并操作上的一种有效的排序算法,该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。
若将两个有序表合并成一个有序表，称为二路归并。
时间复杂度：O(n log n) 
<此算法来自百度百科>
'''
def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    num = int( len(lists) / 2 )
    left = MergeSort(lists[:num])
    right = MergeSort(lists[num:])
    return Merge(left, right)
def Merge(left,right):
    r, l = 0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result
