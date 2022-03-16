import heapq
import json
from collections import OrderedDict

def main():
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
    print('###1.6')
    # From string in countries and capitals, create dictionary europe
    europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo'}
    print(europe)
    print("-"*20)

    #1.7 ordered dictionary
    print('###1.7')
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
    print('###1.8')
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
    print('###1.9')
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
    print('###1.10')
    def dedupe(items): 
      seen = set()
      for item in items:
        if item not in seen:
          yield item 
          seen.add(item)
    def dedupe(items, key=None): 
      seen = set()
      for item in items:
        val = item if key is None else key(item) 
        if val not in seen:
          yield item 
          seen.add(val)

    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(a)
    print(list(dedupe(a)))
    b = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
    print(b)
    print(list(dedupe(b, key= lambda d: (d['x'], d['y']))))
    print(list(dedupe(b, key= lambda d: d['x'])))

    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(a)
    print(list(set(a)))
    print("-"*20)

    #1.11
    print('###1.11')
    record = '.12.................100          .......513.25     ..........'
    abc = slice(1,3)
    print(int(record[abc])*int(record[abc]))
    print(abc.start, abc.stop, abc.step)
    print("-"*20)

    #1.12
    import collections

    #1.13
    print('###1.13')
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]
    from operator import itemgetter
    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_uid = sorted(rows, key=itemgetter('uid')) 
    rows_by_flname = sorted(rows, key=itemgetter('fname', 'lname')) 
    print(rows_by_fname)
    print(rows_by_uid)
    print(rows_by_flname)
    print('-'*20)

    #1.14
    print('###1.14')
    class User:
        def __init__(self, user_id):
            self.user_id = user_id
        def __repr__(self):
            return 'User({})'.format(self.user_id)

    users = [User(2), User(3), User(99)]
    sorted(users, key=lambda s:s.user_id)
    print(users)
    from operator import attrgetter
    users.sort(key=attrgetter('user_id'))
    print(users)
    print('-'*20)

    #1.15
    print('###1.15')
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},]
    from operator import itemgetter
    from itertools import groupby
    rows.sort(key=itemgetter('date'))
    for date, items in groupby(rows, key=itemgetter('date')):
      print(date)
      for item in items:
        print('    ', item)
    print('-'*20)

    #1.16
    print('###1.16')
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]
    print(list(i for i in mylist if i> 0))
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]
    import math


    values = ['1', '2', '-3', '-', '4', 'N/A', '5']
    def is_int(val):
        try:
            x=int(val)
            return True
        except ValueError:
            return False
    print(list(filter(is_int, values)))
    print(list(math.sqrt(i) if i>0 else math.sqrt(-i) for i in mylist))

    addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK',
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE']
    counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
    from itertools import compress
    more5 = [n > 5 for n in counts]
    print(list(compress(addresses, more5)))
    print('-'*20)

    #1.17
    print('###1.17')
    prices = {
       'ACME': 45.23,
       'AAPL': 612.78,
       'IBM': 205.55,
       'HPQ': 37.20,
       'FB': 10.75
    }
    p1 = { key:value for key, value in prices.items() if value > 200 }
    print(p1)
    p1 = dict((key, value) for key, value in prices.items() if value > 200)
    print(p1)
    print('-'*20)

    #1.19
    print('###1.19')
    nums = [1, 2, 3, 4, 5]
    print(sum([x * x for x in nums]))
    print(sum(x * x for x in nums))

    portfolio = [
       {'name':'GOOG', 'shares': 50},
       {'name':'YHOO', 'shares': 75},
       {'name':'AOL', 'shares': 20},
       {'name':'SCOX', 'shares': 65}]
    print(min(s['shares'] for s in portfolio))
    print(min(portfolio, key= lambda s:s['shares']))
    print('-'*20)

    #1.20
    print('###1.20')
    a = {'x': 1, 'z': 3 }
    b = {'y': 2, 'z': 4 }
    merged = dict(a)
    merged.update(b)
    print(merged)
    from collections import ChainMap
    merge_chain = ChainMap(a, b)
    print(merge_chain)

    a['x'] = 11
    print(merged)
    print(merge_chain)

    print('-'*20)

if __name__ == '__main__':
    main()

