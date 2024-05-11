def areSamosasSufficient(guests, doughSheets, mincedMeat, kiriCheese, requests):
    Samosas_Meat_Amount = min(doughSheets,(mincedMeat/5))
    Samosas_Cheese_Amount = kiriCheese*2
    Samosas_Meat_wanted = sum([request[0] for request in requests])
    Samosas_Cheese_wanted = sum([request[1] for request in requests])

    if (Samosas_Meat_wanted +Samosas_Cheese_wanted<= doughSheets):
        if (Samosas_Meat_wanted <= Samosas_Meat_Amount) and (Samosas_Cheese_wanted <= Samosas_Cheese_Amount):
            return("يكفي")
        else:
            print("ما يكفي")
    else:
        print("ما يكفي")

print(areSamosasSufficient(5,20,50,14,[[1,1],[3,2],[2,3],[2,1],[2,2]]))
print(areSamosasSufficient(5,5,50,14,[[1,1],[3,2],[2,3],[2,1],[2,2]]))
print(areSamosasSufficient(5,20,50,4,[[1,1],[3,2],[2,3],[2,1],[2,2]]))
print(areSamosasSufficient(5,20,40,5,[[1,1],[3,2],[2,3],[2,1],[2,2]]))
print(areSamosasSufficient(5,20,40,5,[[0,2],[0,5],[0,5],[0,3],[0,4]]))
print(areSamosasSufficient(5,20,40,9,[[0,2],[0,5],[0,5],[0,3],[0,4]]))
print(areSamosasSufficient(5,20,40,10,[[0,2],[0,5],[0,5],[0,3],[0,4]]))
