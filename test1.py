import pandas as odi

data = {
        'name' : ["afthab","hafis","ajmal"],
        'age': [22,23,24],
        'skills' : ['C++','Python','C++,Python']
    }

df = odi.DataFrame(data)

print(df)
print("\n\n")
print(df.loc[1])

