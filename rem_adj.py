#D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.

test1 = [1, 2, 2, 3]
test2 = [2, 2, 3, 3, 3]
test3 = []

def remove_adjacent(lists):
    n=0
    for numb in lists:
        if n < len(lists):
            while lists[n] == lists[n+1]:
                lists.pop(n+1)
                print(lists)
        else:
            n=n+1


def main():
    remove_adjacent(test1)
    remove_adjacent(test2)
    remove_adjacent(test3)

if __name__ == '__main__':
    main()




