if __name__ == '__main__':
    N = int(input())
    my_list=[]
    for i in range(0, N):
        s = input()
        #print(s)
        if "append" in s:
            temp=s.split()
            x=int(temp[1])
            my_list.append(x)
        elif "insert" in s:
            temp=s.split()
            pos=int(temp[1])
            x=int(temp[2])
            my_list.insert(pos, x)
        elif "sort" in s:
            my_list.sort()
        elif "print" in s:
            print(my_list)
        elif "pop" in s:
            my_list.pop()
        elif "reverse" in s:
            my_list.reverse()
        elif "remove" in s:
            temp=s.split()
            x=int(temp[1])
            my_list.remove(x)
            
                
              
