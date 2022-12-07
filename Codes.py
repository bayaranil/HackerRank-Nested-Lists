if __name__ == '__main__':
    name_List = []
    score_List = []
   
    my_List = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_List.append(name)
        score_List.append(score) 
    #score_List.sort()
    #name_List.sort()
    #print(name_List)
    #score_List.remove(min(score_List))
    
    
    for _ in range(len(score_List)):
        min_Values = min(score_List)
        if min_Values == score_List[_]:
            for i in name_List:
                name_List.remove(name_List[_]) 
            #score_List.remove(_)
            continue
        my_List.append(score_List[_])    
    name_List.sort()
    #print(my_List)
    #print(name_List)          
    for j in name_List:
        print(j)
