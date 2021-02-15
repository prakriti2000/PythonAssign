models = [{'make':'samsung', 'model':216, 'color':'Blue'}, {'make':'mi', 'model':'2', 'color':'black'}, {'make':'iphone', 'model': 7, 'color':'grey'}]
print("Original list of dictionaries :")
print(models)
sorted_models = sorted(models, key = lambda x: x['color'])
print("\nSorting the List of dictionaries :")
print(sorted_models)