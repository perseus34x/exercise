import heapq
import json
from collections import OrderedDict

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
    print("-"*20)

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
    print("-"*20)

    list_entry = [1, 4, 3, 2, 1, 6]
    unique_list = list(set(list_entry))
    print(unique_list)
    print(sorted(unique_list, reverse=True))
    print("-"*20)

    # set operation
    dataScientist = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
    dataEngineer = {'Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'}
    print(dataScientist)
    print(dataEngineer)
    print(dataScientist.union(dataEngineer))
    print(dataScientist.intersection(dataEngineer))
    print(dataScientist.difference(dataEngineer))
    print(dataScientist.symmetric_difference(dataEngineer))
    print("-"*20)

    # dictionary
    # From string in countries and capitals, create dictionary europe
    europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo'}
    print(europe)
    print("-"*20)

    #1.7 ordered dictionary
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    with open("dict_to_json_file.txt", 'w') as f:
      dump_string = json.dumps(d, indent=4)
      print(dump_string, file=f)
    print("-"*20)

    #1.8 calc with dictionary
    prices = {
      'ACME': 45.23,
      'AAPL': 612.78,
      'IBM': 205.55,
      'HPQ': 37.20,
      'FB': 10.75
    }
    min_price = min(prices, key=lambda k:prices[k])
    print(min_price, prices[min_price])
    print(min(zip(prices.values(), prices.keys())))
    print("-"*20)

    #1.9 commonalities in 2 dicts
    a={'x' : 1, 'y' : 2, 'z' : 3 }
    b={'w' : 10, 'x' : 11, 'y' : 2 }
    print(a.keys() & b.keys())
    print(a.items() & b.items()) 
    print(a.keys() - b.keys())
    print({key:a[key] for key in a.keys() - {'y'}})
    print(a.keys() | b.keys())
    print(a.keys() & b.keys())
    print(a.keys() ^ b.keys())
    print(a.keys() - b.keys())
    print("-"*20)

    #1.10 

if __name__ == '__main__':
    data()

