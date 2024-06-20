from collections  import Counter, defaultdict,namedtuple
list = [1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,5]
counter_list = Counter(list)
print(Counter("Hello my name is nani and i love to program in python"))
print(counter_list)

counter = Counter("asssssssssssshdauuuuuuskjcbblashdauigsdha")
print(counter.most_common(5))

#defaultdict 
dict = {"a":5}
dict = defaultdict(lambda:"No exist")
print(dict["a"])

#namedtuple
Dog = namedtuple("Dog",["age","breed","name"])
puchi = Dog(age=6,breed="Chihuahua",name="Puchi")
print(f"He is {puchi.name}, has {puchi.age}, he is a {puchi.breed}")