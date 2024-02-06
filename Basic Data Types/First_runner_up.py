if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maxi=max(arr)
    x=-101
    for ind in arr:
        #print(ind)
        if ind>x and ind<maxi:
            #print(ind)
            x=ind
    
    print(x)
