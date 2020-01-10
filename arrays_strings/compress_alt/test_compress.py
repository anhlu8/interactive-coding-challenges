from nose.tools import assert_equal

#TODO: To Be Continued

def compress_string(string):
    if not string:
        return string
    else:
        string_array = string.split()
        for i in string_array:
            count = 0
            prev_char = ""
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
        assert_equal(func('AABBCC'), 'AABBCC')
        assert_equal(func('AAABCCDDDD'), 'A3BCCD4')
        assert_equal(func('aaBCCEFFFFKKMMMMMMP taaammanlaarrrr seeeeeeeeek tooo'), 'aaBCCEF4KKM6P ta3mmanlaar4 se9k to3')
        print('Success: test_compress')


def main():
    test = TestCompress()
    test.test_compress(compress_string)


if __name__ == '__main__':
    main()