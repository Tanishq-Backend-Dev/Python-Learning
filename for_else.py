nums = [1220,1352,18,21,16,208,257]

for i in nums:
    if i%5==0:
        print(i)
        break # To come out of the loop as we are printing only first element.
else:
    print("not found")

# it is necessary to use break with for else
