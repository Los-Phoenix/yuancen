#这个脚本把cs2013zh转换成更友好的形式
#但是换行和空格没有处理
import codecs

from text_cleaner import keep
from text_cleaner.processor.common import ASCII
from text_cleaner.processor.chinese import CHINESE

from utils.q2b import strQ2B as q2b




inp = '../../MoocLocal/data/2013C.txt'
inl = list(codecs.open(inp, "r", 'utf-8').readlines())
outp = oup = '../../MoocLocal/data/2013C2.txt'
output = codecs.open(oup, 'w', 'utf-8')

for i in inl:
    rst = keep(q2b(i), [ASCII, CHINESE]) + '\n'
    output.write(rst)

output.close()