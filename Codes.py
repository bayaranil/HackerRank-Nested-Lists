if __name__ == '__main__':
    name_List =[]
    score_List =[]
    my_List = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_List.append(name)
        score_List.append(score) 
    score_List.sort()
    name_List.sort()
    print (name_List)
    print (score_List)
    for _ in score_List:
        if _ == int(max(score_List)):
            score_List.remove(int(max(score_List)))
    for _ in score_List:
        if _ == score_List[0]:
            my_List.append(_)
            print (_)
        else:
            my_List.append(name_List[0])
            print (name_List[1])
        
  
 
  

