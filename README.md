# HackerRank-Nested-Lists
Solve Algorithm Example

link here 
[HackerRanks](https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=false)

Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Sample Input 0


```
5

37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0

Berry
Harry
```
--------------------------------------
# Algorithm
```ruby
name_List =[]
score_List =[]

for _ in range(int(input())):
  name= input ()
  score = float(input ())
  name_List.append(name)
  score_List.append(score)

score_List.sort()
name_List.sort()
print (name_List)
print (score_List)
```
