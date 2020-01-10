from nose.tools import assert_equal

class CompressString(object):
    def compress(self, string):
        if string is None or not string:
            return string
        else:
            prev_char = ""
            count = 0
            for index, value in enumerate(string):
                if prev_char != "" and value == prev_char[-2]:
                    count += 1
                    prev_char = prev_char.replace(prev_char[-2:], "")
                    prev_char += value + str(count)
                else:
                    count = 1
                    prev_char += value + " "
            return prev_char.replace(" ", "") if len(prev_char) < len(string) else string
        
class TestCompress(object):

    def test_compress(self, func):
        assert_equal(func(None), None)
        assert_equal(func(''), '')
        assert_equal(func('ABC'), 'ABC')
        assert_equal(func('AABBCC'), 'AABBCC')
        assert_equal(func('AAABCCDDDDE'), 'A3BC2D4E')
        assert_equal(func('BAAACCDDDD'), 'BA3C2D4')
        assert_equal(func('AAABAACCDDDD'), 'A3BA2C2D4')
        print('Success: test_compress')


def main():
    test = TestCompress()
    compress_string = CompressString()
    test.test_compress(compress_string.compress)


if __name__ == '__main__':
    main()
