from text_cleaner import remove, keep

from text_cleaner.processor.common import ASCII
from text_cleaner.processor.chinese import CHINESE, CHINESE_SYMBOLS_AND_PUNCTUATION
from text_cleaner.processor.misc import RESTRICT_URL

# remove url and ascii characters.
# return: u'点击  查看 '
a = remove(
    '点击http://t.cn/RtU0mZ1 查看,123456,test',
    [RESTRICT_URL, ASCII],
)

# remove only Chinese punctuation.
# return: u'点击 http://t.cn/RtU0mZ1  查看,123456,test '
b = remove(
    '点击：http://t.cn/RtU0mZ1， 查看,123456,test。！？',
    [RESTRICT_URL, ASCII],
)

# keep chinese characters and url.
# return: u'点击 http://t.cn/RtU0mZ1 查看'
c = keep(
    '点击http://t.cn/RtU0mZ1 查看,123456,test',
    [CHINESE, RESTRICT_URL],
)

# use processor directly.
# return: u'点击  查看'
d = RESTRICT_URL.remove('点击http://t.cn/RtU0mZ1 查看')
# return: u'点击<URL> 查看'
e = RESTRICT_URL.replace('<URL>').remove('点击http://t.cn/RtU0mZ1 查看')
print(a)
print(b)
print(c)
print(d)
print(e)