#!/usr/bin/env python
import string


class Assert(object):

    @classmethod
    def equal(self, first, second, msg=None):
        """
        Asserts that 2 elements are the same

        :Args:
         - First object to be tested
         - Second object to be tested
         - Message that will be printed if it fails
        """
        assert first == second, msg

    @classmethod
    def not_equal(self, first, second, msg=None):
        """
        Asserts that 2 elements are the same

        :Args:
         - First object to be tested
         - Second object to be tested
         - Message that will be printed if it fails
        """
        assert first != second, msg

    @classmethod
    def true(self, first, msg=None):
        """
        Asserts that what is given is equal to True

        :Args:
         - First object to be tested
         - Message that will be printed if it fails
        """

        assert bool(first) is True, msg

    @classmethod
    def false(self, first, msg=None):
        """
        Asserts that what is given is equal to False

        :Args:
         - First object to be tested
         - Message that will be printed if it fails
        """

        assert bool(first) is False, msg

    @classmethod
    def none(self, first, msg=None):
        """
        Asserts that what is given is equal to None

        :Args:
         - First object to be tested
         - Message that will be printed if it fails
        """

        assert first is None, msg

    @classmethod
    def not_none(self, first, msg=None):
        """
        Asserts that what is given is not equal to None

        :Args:
         - First object to be tested
         - Message that will be printed if it fails
        """

        assert first is not None, msg

    @classmethod
    def fail(self, msg):
        """
        Raises an assertion error with a message passed in

        :Args:
         - Message that will be printed
        """
        raise AssertionError(msg)

    @classmethod
    def is_ascending(self, iterable, msg='', icase=False):
        """
        Goes through a list and asserts that items in the list are sorted ascendingly

        :Args:
         - List that will be asserted against
         - Message that will be printed if it fails
         - Whether or not to ignore case
        """
        if icase:
            iterable = map(string.lower, iterable)

        for i, item in enumerate(iterable[:-1]):
            assert iterable[i] <= iterable[i + 1], '. '.join(['%s is not before %s' % (iterable[i + 1], iterable[i]), msg])

    @classmethod
    def is_descending(self, iterable, msg='', icase=False):
        """
        Goes through a list and asserts that items in the list are sorted descendingly

        :Args:
         - List that will be asserted against
         - Message that will be printed if it fails
         - Whether or not to ignore case
        """
        if icase:
            iterable = map(string.lower, iterable)

        for i, item in enumerate(iterable[:-1]):
            assert iterable[i] >= iterable[i + 1], '. '.join(['%s is not before %s' % (iterable[i], iterable[i + 1]), msg])

    @classmethod
    def raises(self, exception, caller, *args, **kwargs):
        """
        Asserts that an Error is raised when calling a method

        :Args:
         - Error class
         - method to be called
         - args that will be passed to the caller
         - kwargs that will be passed to the caller
         - msg named arg - text that will be printed if it fails,
           will not be sent to caller
        """
        msg = kwargs.get('msg', '')

        try:
            caller(*args, **kwargs)
        except exception:
            return

        if hasattr(exception, '__name__'):
            excName = exception.__name__
        else:
            excName = str(exception)

        raise AssertionError("%s was not raised. %s" % (excName, msg))

    @classmethod
    def contains(self, needle, haystack, msg=''):
        try:
            assert needle in haystack
        except AssertionError:
            raise AssertionError('%s is not found in %s. %s' % (needle, haystack, msg))

    @classmethod
    def is_less(self, first, second, msg=None):
        """
        Asserts that first element is < the second element

        :Args:
         - First object to be tested
         - Second object to be tested
         - Message that will be printed if it fails
        """
        assert first < second, msg

    @classmethod
    def is_greater(self, first, second, msg=None):
        """
        Asserts that first element is greater than the second element

        :Args:
         - First object to be tested
         - Second object to be tested
         - Message that will be printed if it fails
        """

        assert first > second, msg

    @classmethod
    def is_less_or_equal(self, first, second, msg=None):
        """
        Asserts that the first element is <= to the second element

        :Args:
         - First object to be tested
         - Second object to be tested
         - Message that will be printed if it fails
        """

        assert first <= second, msg

    @classmethod
    def is_greater_or_equal(self, first, second, msg=None):
        """
        Asserts that first element is >= to the second element

        :Args:
         - First object to be tested
         - Second object to be tested
         - Message that will be printed if it fails
        """

        assert first >= second, msg

    @classmethod
    def endswith(self, string, suffix, msg=None):
        """
        Asserts that first string ends with the second suffix

        :Args:
         - String to test
         - String suffix should be at the end of the string
         - Message that will be printed if it fails
        """

        assert string.endswith(suffix), msg
