def strQ2B(ustring):
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 12288:
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374):
            inside_code -= 65248
        rstring += chr(inside_code)
    return rstring

# a = '算法与复杂度（ＡｌｇｏｒｉｔｈｍｓａｎｄＣｏｍｐｌｅｘｉｔｙ，ＡＬ）'
# print(strQ2B(a))