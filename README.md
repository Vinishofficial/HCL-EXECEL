# 25-09-2026

## TASK - Python 

```python
'''1. Student Attendance Analysis
A college maintains the daily attendance details of its students in the form of a list containing student IDs. Some students may have attended multiple sessions on the same day. The administration wants to identify the longest continuous sequence of sessions in which no student ID is repeated. Develop a solution that determines the maximum length of such a sequence.'''

student_ids = list(map(int, input().split()))

seen_students = set()
left = 0
max_sequence = 0

for right in range(len(student_ids)):
    while student_ids[right] in seen_students:
        seen_students.remove(student_ids[left])
        left += 1

    seen_students.add(student_ids[right])
    max_sequence = max(max_sequence, right - left + 1)

print(max_sequence)


-----


'''2. Online Shopping Price Analysis
An online shopping application stores the prices of products viewed by a customer during a browsing session. The customer wants to identify a continuous range of products that provides the maximum possible total discount value. Given the discount values, determine the maximum value that can be obtained from any continuous range.'''

discount_values = list(map(int, input().split()))

current_discount = discount_values[0]
maximum_discount = discount_values[0]

for discount in discount_values[1:]:
    current_discount = max(discount, current_discount + discount)
    maximum_discount = max(maximum_discount, current_discount)

print(maximum_discount)

---

''3. Rainwater Collection System
A city installs buildings of different heights along a straight road. During rainfall, water gets collected between taller buildings. The engineering team needs to calculate the total amount of water that can remain trapped after heavy rainfall based on the heights of the buildings.'''

building_heights = list(map(int, input().split()))

left = 0
right = len(building_heights) - 1
left_max = 0
right_max = 0
trapped_water = 0

while left < right:
    if building_heights[left] <= building_heights[right]:
        if building_heights[left] >= left_max:
            left_max = building_heights[left]
        else:
            trapped_water += left_max - building_heights[left]
        left += 1
    else:
        if building_heights[right] >= right_max:
            right_max = building_heights[right]
        else:
            trapped_water += right_max - building_heights[right]
        right -= 1

print(trapped_water)

-----

'''4. Employee Performance Analysis
A company stores the monthly performance scores of an employee for several months. The scores may contain both positive and negative values depending on the employee's performance. Management wants to identify the continuous period during which the employee achieved the highest overall performance.'''

performance_scores = list(map(int, input().split()))

current_performance = performance_scores[0]
highest_performance = performance_scores[0]

for score in performance_scores[1:]:
    current_performance = max(score, current_performance + score)
    highest_performance = max(highest_performance, current_performance)

print(highest_performance)

------

'''5. Product Sales Analysis
A retail company stores the daily sales quantity of a product for several consecutive days. Due to seasonal changes, some days may have negative adjustments. The company wants to identify the period that produced the highest multiplication of sales-related values. Develop a solution to determine this maximum product.'''

sales_values = list(map(int, input().split()))

maximum_product = sales_values[0]
minimum_product = sales_values[0]
highest_sales_product = sales_values[0]

for sales in sales_values[1:]:
    if sales < 0:
        maximum_product, minimum_product = minimum_product, maximum_product

    maximum_product = max(sales, maximum_product * sales)
    minimum_product = min(sales, minimum_product * sales)

    highest_sales_product = max(highest_sales_product, maximum_product)

print(highest_sales_product)

-------

'''6. Customer Purchase History
An e-commerce application stores the product IDs purchased by a customer in chronological order. The same product may appear multiple times. The system needs to determine the longest sequence of consecutive purchases in which every product ID is unique.'''

product_ids = list(map(int, input().split()))

purchased_products = set()
left = 0
longest_purchase_sequence = 0

for right in range(len(product_ids)):
    while product_ids[right] in purchased_products:
        purchased_products.remove(product_ids[left])
        left += 1

    purchased_products.add(product_ids[right])
    longest_purchase_sequence = max(
        longest_purchase_sequence,
        right - left + 1
    )

print(longest_purchase_sequence)

-------

'''7. Bank Transaction Analysis
A bank stores transaction amounts for a customer's account. A continuous group of transactions may add up to a specific target amount. The auditing system needs to determine how many different continuous transaction groups produce exactly the specified amount.'''

transaction_amounts = list(map(int, input().split()))
target_amount = int(input())

prefix_sum = 0
transaction_groups = 0
prefix_counts = {0: 1}

for amount in transaction_amounts:
    prefix_sum += amount

    if prefix_sum - target_amount in prefix_counts:
        transaction_groups += prefix_counts[prefix_sum - target_amount]

    prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1

print(transaction_groups)

-------

'''8. Employee Skill Grouping
A company receives a list of employee skill codes represented as strings. Employees having the same set of characters in their skill codes belong to the same skill category, even if the characters appear in a different order. The HR system needs to organize employees into appropriate skill groups.'''

skill_codes = input().split()

skill_groups = {}

for skill in skill_codes:
    skill_key = ''.join(sorted(skill))

    if skill_key not in skill_groups:
        skill_groups[skill_key] = []

    skill_groups[skill_key].append(skill)

for group in skill_groups.values():
    print(*group)

------

'''9. Network Packet Analysis
A network monitoring system receives packet identifiers in chronological order. The system must determine the longest sequence of consecutive packets whose identifiers form a continuous numerical sequence, regardless of their original order in the incoming data.'''

packet_ids = list(map(int, input().split()))

packet_set = set(packet_ids)
longest_packet_sequence = 0

for packet_id in packet_set:
    if packet_id - 1 not in packet_set:
        current_packet = packet_id
        current_sequence = 1

        while current_packet + 1 in packet_set:
            current_packet += 1
            current_sequence += 1

        longest_packet_sequence = max(
            longest_packet_sequence,
            current_sequence
        )

print(longest_packet_sequence)

-------

'''10. Hospital Appointment Scheduling
A hospital receives appointment requests represented by starting and ending times. Some appointments overlap with each other. The scheduling system needs to combine overlapping appointment periods so that the final schedule contains only non-overlapping time ranges.'''

appointment_count = int(input())

appointments = []

for _ in range(appointment_count):
    start_time, end_time = map(int, input().split())
    appointments.append([start_time, end_time])

appointments.sort()

merged_appointments = []

for appointment in appointments:
    if not merged_appointments or appointment[0] > merged_appointments[-1][1]:
        merged_appointments.append(appointment)
    else:
        merged_appointments[-1][1] = max(
            merged_appointments[-1][1],
            appointment[1]
        )

for appointment in merged_appointments:
    print(*appointment)


```






# 23-09-2026

## TASK - Python 

```python
'''Write a program which can compute the factorial of a given numbers.Theresults should be printed in a comma-separated sequence on a singleline.Suppose the following input is supplied to the program:8
Then, the output should be:40320'''

n = int(input())

fact = 1;

for i in range(1,n+1):
  fact = fact*i;
print(fact)


-----


'''Write a Python program which accepts a sequence of comma separated 4 digit
binary numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated
sequence.
Example:
0100,0011,1010,1001
0100,0011-1010/1001_1111
Then the output should be:
1010'''

import re

a = re.split(r'[_/, -]+', input())

res = []

for n in a:
    n = n.strip()
    if int(n, 2) % 5 == 0:
        res.append(n)

print(",".join(res))

---

'''Write a Python program that accepts a sentence and calculate the number of
letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''

s = input()

let = 0;
dig = 0;

for n in s:
  if n.isalpha():
    let+=1
  elif n.isdigit():
    dig+=1

print("LETTERS",let)
print("DIGITS",dig)
```
