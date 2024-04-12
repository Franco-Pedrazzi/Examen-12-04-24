def intersect(list1,list2):
    listFinal=[]
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                listFinal.append(list1[i])

    return listFinal
print(intersect([1,2,3,4,5],[3,4,5,6,7]))