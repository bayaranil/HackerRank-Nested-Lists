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
