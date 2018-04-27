while True:
    try:
        nums = input().split(" ")
        b1, b2 = nums
        
        b1 = int(b1)
        b2 = int(b2)
        
        result = b1 ^ b2
        
        print(result)
    except EOFError:
        break
