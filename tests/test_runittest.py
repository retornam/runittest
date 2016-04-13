#!/usr/bin/env python
from runittest import Assert


def raises_(expected_exc, fun, *args, **kwargs):
    try:
        fun(*args, **kwargs)
    except Exception as exc:
        assert type(exc) == expected_exc
        return
    raise AssertionError("Exception %s not raised" % expected_exc.__name__)


class TestRunittest(object):
    def test_that_are_equal(self):
        Assert.equal("1", "1")
        Assert.equal(1, 1)

    def test_that_are_not_equal_throws_error(self):
        raises_(AssertionError, Assert.equal, "1", "2")

    def test_that_items_are_not_equal(self):
        Assert.not_equal("a", "b")
        Assert.not_equal(1, 2)

    def test_that_we_can_check_for_true(self):
        Assert.true(True)
        Assert.true("a" in "bad")
        Assert.true(1 == 1)

    def test_that_get_an_exception_if_not_true(self):
        raises_(AssertionError, Assert.true, False)

    def test_that_we_can_check_for_false(self):
        Assert.false(False)
        Assert.false("z" in "bad")
        Assert.false(1 == 2)

    def test_that_we_get_an_exception_if_not_false(self):
        raises_(AssertionError, Assert.false, True)

    def test_that_something_is_none(self):
        Assert.none(None)

    def test_that_if_not_none_exception_thrown(self):
        raises_(AssertionError, Assert.none, 1)

    def test_that_not_none_passes(self):
        Assert.not_none(1)
        Assert.not_none("a")
        Assert.not_none("a" in "bad")

    def that_we_can_throw_when_we_fail(self):
        raises_(AssertionError, Assert.fail, "omg!!!!")

    def test_is_ascending_success_1(self):
        Assert.is_ascending([1])

    def test_is_ascending_success_3(self):
        Assert.is_ascending([1, 2, 3])

    def test_is_ascending_icase(self):
        args = ['a', 'B', 'c']
        raises_(AssertionError, Assert.is_ascending, args)
        Assert.is_ascending(args, icase=True)

    def test_is_ascending_fail(self):
        try:
            Assert.is_ascending([1, 3, 2], "failure message")
        except AssertionError as e:
            assert e.msg == "2 is not before 3. failure message"

    def test_is_ascending_fail_no_message(self):
        try:
            Assert.is_ascending([1, 3, 2])
        except AssertionError as e:
            assert e.msg == "2 is not before 3. "

    def test_is_ascending_empty(self):
        Assert.is_ascending([])

    def test_is_ascending_none(self):
        raises_(TypeError, Assert.is_ascending, None)

    def test_is_descending_success_1(self):
        Assert.is_descending([1])

    def test_is_descending_success_3(self):
        Assert.is_descending([3, 2, 1])

    def test_is_descending_icase(self):
        args = ['c', 'B', 'a']
        raises_(AssertionError, Assert.is_descending, args)
        Assert.is_descending(args, icase=True)

    def test_is_descending_fail(self):
        try:
            Assert.is_descending([3, 1, 2], "failure message")
        except AssertionError as e:
            assert e.msg == "1 is not before 2. failure message"

    def test_is_descending_fail_no_message(self):
        try:
            Assert.is_descending([3, 1, 2])
        except AssertionError as e:
            assert e.msg == "1 is not before 2. "

    def test_is_descending_empty(self):
        Assert.is_descending([])

    def test_is_descending_none(self):
        raises_(TypeError, Assert.is_descending, None)

    def test_that_assert_raises_catches_exceptions(self):
        Assert.raises(ZeroDivisionError, self._divide_by_zero)

    def test_that_we_raise_when_error_not_thrown(self):
        raises_(AssertionError, Assert.raises, Exception, self._add_num, 5, 4)

    def test_raises_failure_with_message(self):
        try:
            Assert.raises(Exception, self._add_num, 5, 4, msg="failure message")
        except AssertionError as e:
            Assert.equal(e.msg, "Exception was not raised. failure message")

    def test_raises_failure_without_message(self):
        try:
            Assert.raises(Exception, self._add_num, 5, 4,)
        except AssertionError as e:
            Assert.equal(e.msg, "Exception was not raised. ")

    def test_that_we_can_check_items_contain_something(self):
        Assert.contains("a", "bad")
        Assert.contains("a", ["a", "b", "c"])
        Assert.contains("dog", {"dog": "poodle", "cat": "siamese", "horse": "arabian"})

    def test_that_string_does_not_contain_letter(self):
        raises_(AssertionError, Assert.contains, "a", "cde")

    def test_that_list_does_not_contain_element_failure_no_message(self):
        try:
            Assert.contains("d", ["a", "b", "c"])
        except AssertionError as e:
            Assert.equal(e.msg, "d is not found in ['a', 'b', 'c']. ")

    def test_dict_does_not_contain_key_failure_with_message(self):
        try:
            Assert.contains("dog", {"cat": "siamese", "horse": "arabian"},
                            msg="failure message")
        except AssertionError as e:
            Assert.equal(e.msg,
                         "dog is not found in {'horse': 'arabian', 'cat': 'siamese'}. failure message")

    def test_is_less_success(self):
        Assert.is_less("1", "2")
        Assert.is_less(1, 2)

    def test_is_less_fail_string(self):
        raises_(AssertionError, Assert.is_less, "2", "1")

    def test_is_less_fail_int(self):
        raises_(AssertionError, Assert.is_less, 2, 1)

    def test_is_less_fail_string_message(self):
        try:
            Assert.is_less("2", "1", "message")
        except AssertionError as e:
            Assert.equal(e.msg, "message")

    def test_is_less_fail_int_message(self):
        try:
            Assert.is_less(2, 1, "message")
        except AssertionError as e:
            Assert.equal(e.msg, "message")

    def test_is_greater_success(self):
        Assert.is_greater("2", "1")
        Assert.is_greater(2, 1)

    def test_is_greater_fail_string(self):
        raises_(AssertionError, Assert.is_greater, "1", "2")

    def test_is_greater_fail_int(self):
        raises_(AssertionError, Assert.is_greater, 1, 2)

    def test_is_greater_fail_string_message(self):
        try:
            Assert.is_greater("1", "2", "message")
        except AssertionError as e:
            Assert.equal(e.msg, "message")

    def test_is_greater_fail_int_message(self):
        try:
            Assert.is_greater(1, 2, "message")
        except AssertionError as e:
            Assert.equal(e.msg, "message")

    def test_is_greater_or_equal_success(self):
        Assert.is_greater_or_equal("2", "1")
        Assert.is_greater_or_equal(2, 1)
        Assert.is_greater_or_equal("1", "1")
        Assert.is_greater_or_equal(1, 1)

    def test_is_greater_or_equal_fail_string(self):
        raises_(AssertionError, Assert.is_greater_or_equal, "1", "2")

    def test_is_greater_or_equal_fail_int(self):
        raises_(AssertionError, Assert.is_greater_or_equal, 1, 2)

    def test_is_greater_or_equal_fail_string_message(self):
        try:
            Assert.is_greater_or_equal("1", "2", "message")
        except AssertionError as e:
            Assert.equal(e.msg, "message")

    def test_is_greater_or_equal_fail_int_message(self):
        try:
            Assert.is_greater_or_equal(1, 2, "message")
        except AssertionError as e:
            Assert.equal(e.msg, "message")

    def test_is_less_or_equal_success(self):
        Assert.is_less_or_equal("1", "2")
        Assert.is_less_or_equal(1, 2)
        Assert.is_less_or_equal("1", "1")
        Assert.is_less_or_equal(1, 1)

    def test_is_less_or_equal_fail_string(self):
        raises_(AssertionError, Assert.is_less_or_equal, "2", "1")

    def test_is_less_or_equal_fail_int(self):
        raises_(AssertionError, Assert.is_less_or_equal, 2, 1)

    def test_is_less_or_equal_fail_string_message(self):
        try:
            Assert.is_less_or_equal("2", "1", "message")
        except AssertionError as e:
            Assert.equal(e.msg, "message")

    def test_is_less_or_equal_fail_int_message(self):
        try:
            Assert.is_less_or_equal(2, 1, "message")
        except AssertionError as e:
            Assert.equal(e.msg, "message")

    def test_endswith_success(self):
        Assert.endswith("abcde", "de")
        Assert.endswith("abcde", "abcde")

    def test_endswith_fail(self):
        raises_(AssertionError, Assert.endswith, "abcde", "abc")

    def test_that_objects_asserted_for_bool_return_correctly(self):
        mydict = {"mykey":"123"}
        Assert.true(mydict['mykey'])

    def _divide_by_zero(self):
        return 1 / 0

    def _add_num(self, first, second):
        return first + second
