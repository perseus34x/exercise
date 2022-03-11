import heapq

def data():
    tuple_entry = (1, 3, 2, 4)
    list_entry = [1, 2, 4, 3]
    print('tuple count is %d and list count is %d' % (len(tuple_entry), len(list_entry)))
    (a, *_) = tuple_entry
    (*_, b) = list_entry
    print("a is %d and b is %d" % (a, b))

    list_entry.sort()
    list_entry.append(5)
    (*_, b) = list_entry
    print("a is %d and b is %d" % (a, b))
    print('-'*20)


    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))
    print(sorted(nums)[:4])
    print(sorted(nums)[-2:])

    portfolio = [
             {'name': 'IBM', 'shares': 100, 'price': 91.1},
             {'name': 'AAPL', 'shares': 50, 'price': 543.22},
             {'name': 'FB', 'shares': 200, 'price': 21.09},
             {'name': 'HPQ', 'shares': 35, 'price': 31.75},
             {'name': 'YHOO', 'shares': 45, 'price': 16.35},
             {'name': 'ACME', 'shares': 75, 'price': 115.65}
             ]
    cheap = heapq.nsmallest(3, portfolio, key=lambda s:s['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda s:s['price'])
    print(cheap, expensive)


    list_entry = [1, 4, 3, 2, 1, 6]
    unique_list = list(set(list_entry))
    print(unique_list)
    print(sorted(unique_list, reverse=True))

    # set operation
    dataScientist = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
    dataEngineer = {'Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'}
    print(dataScientist)
    print(dataEngineer)
    print(dataScientist.union(dataEngineer))
    print(dataScientist.intersection(dataEngineer))
    print(dataScientist.difference(dataEngineer))
    print(dataScientist.symmetric_difference(dataEngineer))

    # dictionary
    # From string in countries and capitals, create dictionary europe
    europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo'}
    print(europe)

if __name__ == '__main__':
    data()

