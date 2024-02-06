if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l=[name,score]
        records.append(l)
    lowest=1000000000
    second_lowest=lowest
    output=[]
    l=len(records)
    for i in range(0,l):
        if records[i][1]<lowest:
            second_lowest=lowest
            lowest=records[i][1]
        elif records[i][1]<second_lowest and records[i][1]!=lowest:
            second_lowest=records[i][1]
    for i in range(0, l):
       if records[i][1]==second_lowest:
           output.append(records[i][0])
    
    output.sort()     
    for i in output:
        print(i)
