length=int(input("ingrese numero de sublistas "))
listas=[]
def completarLista():
    lista=list(input("inserte una serie de numeros para la nueva sublista "))
    return lista
def uniqueValues(listas,num):
    listFinal=[]
    ob={}
    
    for i in range(len(listas)):
        for j in range(len(listas)):
           ob[listas[i][j]]=1
    
    for i in range(len(listas)-1):
        j=0
        index=0
        while j<len(listas[i]):

            if listas[i][index]==listas[i+1][j]:
                
                ob[listas[i][index]]+=1
            j+=1
            if index<len(listas[i])-1 and j==len(listas[i]):
                j=0
                index+=1
        
    for i in ob:
        if ob[i]==num:
            listFinal.append(i)

    return listFinal
for i in range(length):
    listas.append(completarLista())
print( uniqueValues(listas,length))