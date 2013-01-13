# -*- coding: utf-8 -*-

"""
Copyright (c) 2013 wgx731 <wgx731@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

""" Visit plugin test

    Test Cases for xiaohuangji visit plugin
"""

__author__ = 'wgx731'
__copyright__ = 'Copyright (c) 2013 wgx731'
__license__ = 'MIT'
__version__ = '0.1'
__maintainer__ = 'wgx731'
__email__ = 'wgx731@gmail.com'
__status__ = 'development'

from nose.tools import ok_
from nose.tools import eq_
from test_config import *
from ..plugins import visit

sys.path = [TEST_DIR] + sys.path


class TestVisit(TestBase):

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_visit_test_1(self):
        eq_(False, visit.test({'message': '别来访'}, None), WRONG_KEY_WORD_ERROR)

    def test_visit_test_2(self):
        eq_(True, visit.test({'message': '求来访'}, None), WRONG_RESULT_ERROR)

    def test_visit_handle_1(self):
        eq_(True, visit.handle({'message': '求来访'}, None) in ['我来也', '马上就到', '来啦', '在路上了'], WRONG_RESULT_FORMAT_ERROR)
