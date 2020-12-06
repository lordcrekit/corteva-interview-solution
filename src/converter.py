import csv
import collections
import json

class converter():
    '''
    '''

    def __init__(self):
        self._counter  = 1;
        self._missed   = []
        self._userlist = []

    def convert(self, csvpaths, destpath, errpath):
        '''
        Convert all provided csvpaths into the proper json at the destpath.

        Any rows that cannot be converted (do not adhere to expected format) are sent to errpath (unless None).
        '''
        for csvpath in csvpaths:
            with open(csvpath, 'r') as csvfile:
                csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                category = None
                for row in csvreader:
                    if category is None:
                        category = row
                    else:
                        self._consume(csvpath, row)

        self._resolve(destpath, None)

    def _consume(self, csvpath, row):
        '''Consume a single row of a csv file'''
        if not len(row) == 2:
            self._missed(csvpath, row)
            return

        name = row[0].split(' ')
        email = row[1]

        if not len(name) == 2:
            self._miss(csvpath, row, 'namecount missed')
            return

        first, last = name
        self._userlist.append({
            'list_id':    self._counter,
            'first name': first,
            'last name':  last,
            'email':      email,
        })
        self._counter += 1

    def _miss(self, csvpath, row, reason):
        '''Call when a row cannot be resolved'''
        print('%s : %s' % (reason, row))

    def _resolve(self, destpath, errpath):
        '''Resolve all converted rows, write output'''

        assert self._counter -1 == len(self._userlist)

        data = {
            'user_list_size': len(self._userlist),
            'user_list': self._userlist,
        }

        with open(destpath, 'w') as destfile:
            json.dump(data, destfile, indent=4)
