def MaxRecurs():
    try:
        num = int(input())
        if num == 0:
            raise Exception("Конец последовательности")
        maxfar = MaxRecurs()
        return max(num, maxfar)
    
    except Exception as e:
        if str(e) == "Конец последовательности":
            return -1
        else:
            raise

MaxValue = MaxRecurs()
if MaxValue != -1:
    print(MaxValue)