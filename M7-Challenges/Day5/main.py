def func(guests, jugSize, cupSize):
    jugSize_l = jugSize
    cupSize_l = cupSize/1000

    if guests == 0:
        return {"total Served": "0.000", "remaining": f"{jugSize_l:.3f}"}
    if jugSize_l == cupSize_l:
        return {"total Served": f"{jugSize_l:.3f}", "remaining": "0.000", "note": "not enough"}

    total_served_l = cupSize_l * (1 - (0.5 ** guests)) / (1 - 0.5)
    remaining_l = max(jugSize_l - total_served_l, 0)
    
    return {"total Served": f"{total_served_l:.3f}", "remaining": f"{remaining_l:.3f}"}

print(func(3, 2, 1000))  
print(func(4, 2, 1000))
print(func(5, 2, 1000))
print(func(0, 2, 1000))
print(func(3, 1, 1000))
