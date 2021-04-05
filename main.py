from collections import Counter
grades = [83,95,87,95,70,0,85,82,100,67,73,77,0]

histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)
