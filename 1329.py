while(True):
    N = input();
    if N == '0':
        break
    else:
        entries = input().split();
        count_m, count_j = 0,0

        for res in entries:
            if res == '0':
                count_m+=1
            elif res == '1':
                count_j+=1

        print("Mary won",count_m,"times and John won",count_j,"times")
