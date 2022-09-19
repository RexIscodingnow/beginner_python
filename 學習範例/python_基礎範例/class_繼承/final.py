from happen import HappenThing

chinese = int(input("國文分數: "))
math = int(input("數學分數: "))

score = HappenThing.Add(chinese, math)
decision = HappenThing.someThing(score)

HappenThing.food(decision)