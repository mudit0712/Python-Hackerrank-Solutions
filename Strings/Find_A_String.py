def count_substring(string, sub_string):
    ans=0
    ind=0
    for i in range(0,len(string)):
        if string[i]==sub_string[ind]:
            ind+=1
            if ind==len(sub_string):
                ans+=1
                if(sub_string[0]==sub_string[ind-1]):
                    ind=1
                else:
                    ind=0
        else:
            ind=0        
    return ans

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)