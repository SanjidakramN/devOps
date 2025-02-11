#bubble sort of dictionary

# def bubble_sort_dict(dict1):
#     for i in range(len(dict1)-1):
#         for j in range(len(dict1)-1):
#             if dict1[j]>dict1[j+1]:
#                 dict1[j],dict1[j+1]=dict1[j+1],dict1[j]
#     return dict1

# dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print(bubble_sort_dict(dict1))

# Bubble sort of dictionary by keys

def bubble_sort_dict(dict1):
    items = list(dict1.items())
    for i in range(len(items)-1):
        for j in range(len(items)-1):
            if items[j][0] > items[j+1][0]:
                items[j], items[j+1] = items[j+1], items[j]
    return dict(items)

dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(bubble_sort_dict(dict1))

