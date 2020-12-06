import csv
import collections
import json


class Converter():
    '''
    Converts csv files into a single formatted json file.
    '''

    def __init__(self):
        self._counter = 1
        self._userlist = []

    def convert(self, csvpaths, destpath):
        '''
        Convert all provided csvpaths into the proper json at the destpath.
        '''
        for csvpath in csvpaths:
            with open(csvpath, 'r') as csvfile:
                csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                category = None
                for row in csvreader:
                    if category is None:
                        category = row
                    else:
                        self._consume(category, row)

        self._resolve(destpath)

    def _consume(self, cats, row):
        '''Consume a single row of a csv file'''
        if not len(row) == 2:
            self._miss(cats, row, 'wrong number of rows')
            return

        name = row[0].split(' ')
        email = row[1]

        if not len(name) == 2:
            self._miss(cats, row, 'namecount missed')
            return

        first, last = name
        self._userlist.append({
            'list_id':    self._counter,
            'first name': first,
            'last name':  last,
            'email':      email,
        })
        self._counter += 1

    def _miss(self, cats, row, reason):
        '''
        Call when a row cannot be resolved.

        Nothing is done with this for now, but this should be sent to a failure / backup.
        '''
        print('%s : %s : %s' % (reason, cats, row))

    def _resolve(self, destpath):
        '''Resolve all converted rows, write output'''

        assert self._counter - 1 == len(self._userlist)

        data = {
            'user_list_size': len(self._userlist),
            'user_list': self._userlist,
        }

        with open(destpath, 'w') as destfile:
            json.dump(data, destfile, indent=4, sort_keys=True)
