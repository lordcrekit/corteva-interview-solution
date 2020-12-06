import os
import unittest
import json
import tempfile
import filecmp
from   src.converter import Converter

class TestConverter(unittest.TestCase):
    '''
    Empty for tests created by make_test.
    '''
    pass

def make_test(fname):
    '''Create a testcase for a given path'''
    def test(self):
        try:
            converter = Converter()
            fullpath  = os.path.join(os.path.split(__file__)[0], 'res', 'testcases', fname)
            inputs    = os.listdir(os.path.join(fullpath, 'input'))
            inputs    = map(lambda x: os.path.join(fullpath, 'input', x), inputs)

            expected     = os.path.join(fullpath, 'expected.json')
            fhandle, got = tempfile.mkstemp()

            c = Converter()
            c.convert(inputs, got)

            with open(expected, 'r') as exf:
                exj  = json.load(exf)
            with open(got, 'r') as gotf:
                gotj = json.load(gotf)

            self.assertEquals(exj['user_list_size'], gotj['user_list_size'])
            self.assertListEqual(exj['user_list'], gotj['user_list'])
            self.assertDictEqual(exj, gotj)

        finally:
            os.close(fhandle)
            os.remove(got)

    return test

## Create all testcases and add them to the TestConverter.
for path in os.listdir(os.path.join(os.path.split(__file__)[0], 'res', 'testcases')):
    test_func = make_test(path)
    setattr(TestConverter, 'test_%s' % path, test_func)

