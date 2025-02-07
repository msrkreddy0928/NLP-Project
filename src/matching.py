from mysqldb import retrieve_all_candidates


def skill_matcher(job_desc):
    
    job_des_skill_set = job_desc.lower().split(",")
    
    no_of_skills = len(job_des_skill_set)
    
    
    candidates_list = retrieve_all_candidates()
    
    candidates_dict = {}
    
    for candidate in candidates_list:
        candidates_dict[candidate[2]] = candidate[3:]
        
        
    for num,skills in candidates_dict.items():
        list1=[]
        for skill in skills:
            list1 += [sk.lower() for sk in skill.split(",") if sk!="None"]
            candidates_dict[num]=list1    
    

    # for num,skills in candidates_dict.items():
        # print(num,skills)
        
    dict1={}    
    
    for num,skills in candidates_dict.items():
        k=0
        str1=""
        for word in job_des_skill_set:
            print(skills)
            if word in skills:
                k+=1
            else:
                str1=str1+","+word    
        if k!=0:
            dict1[num]=[k,str1]
    
        
    dict1 =  dict(sorted(dict1.items(),key=lambda item: item[1][0],reverse=True))
    
    
    for num,matched_skills in dict1.items():
        if matched_skills[0]!=0:
            dict1[num][0] = (matched_skills[0]/no_of_skills)*100
            
         
    return_dict={}
    
    k=0
    for i,(key,match) in enumerate(list(dict1.items())[:3]):
        list1=[]
        for candiate in candidates_list:
            k=candiate[2]
            if k==key:
                list1.append(candiate[0])
                list1.append(candiate[1])
                list1.append(candiate[2])
                list1.append(match[0])
                list1.append(match[1])
                break
                
        return_dict[i]=list1         
    print(return_dict)    
        
    return return_dict
        

job_desc =  "SQL,Feature Engineering,Machine Learning,TensorFlow,GPT,Generative AI,Deep Learning,Data Science" 

skill_matcher(job_desc)