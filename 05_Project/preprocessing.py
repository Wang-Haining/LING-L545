#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: hw56@iu.edu

Created on Fri DEC 21 23:59:59 2019

"""
import re
from hanziconv import HanziConv


def text_handler(file_name):
    lines = ''
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()

    return content


def interceptor(text):
    import re
    # import nltk
    # import jieba
    # word_tokens = nltk.regexp_tokenize(text, pattern=r".")
    # re.findall(pattern=r'【[\u4e00-\u9fa5]+[\w\W]{0,100}】', string=origin)
    comments = re.findall(r".*【(.*?)】.*", origin)

    gc_txt = gc_txt.replace(u'\u3000\u3000', '\n')
    return None


# 《续金瓶梅》处理开始
xjpm = '/Users/hwang/Desktop/repo/Unmasking-XSYYZ/corpus/XJPM.txt'
xjpm_txt = text_handler(xjpm)


# 再去掉全角空格
xjpm_txt = xjpm_txt.replace(u'\u3000\u3000', '\n')
xjpm_txt = xjpm_txt.replace(u'\u3000', '\n')


# 去除"XX品"
ch_mark_set2 = re.findall(pattern=r"\s(游戏品|广仁品|广慧品|正法品|妙悟品|戒导品|正法品|净行品|庄严品|证入品|证人品|解脱品)\s",
                          string=xjpm_txt,
                          flags=re.S | re.M)
for mark in ch_mark_set2:
    xjpm_txt = xjpm_txt.replace(mark, "")

xjpm_txt = xjpm_txt.replace(u'\n', '')
xjpm_txt = xjpm_txt.replace(u' ', '')

# remove chapter markers
# ch_mark_set1 = re.findall(pattern=r"(第[一二三四五六七八九十]{1,3}回[ \n]{1,3}.{7,9}?[ \n]{1,3}.{7,9}?[ \n])",
#                           string=xjpm_txt,
#                           flags=re.S | re.M)
#
# for mark in ch_mark_set1:
#     xjpm_txt = xjpm_txt.replace(mark, "")

with open('/Users/hwang/Desktop/repo/Unmasking-XSYYZ/corpus/XJPM_1.txt', 'w', encoding='utf8') as f:
    f.write(xjpm_txt)
# 《续金瓶梅》处理结束
# 仍有"口口口口"未处理


# 《醒世姻缘传》处理开始
xsyyz = '/Users/hwang/Desktop/repo/Unmasking-XSYYZ/unknown/XSYYZ.txt'
xsyyz_txt = text_handler(xsyyz)

# 再去掉全角空格
xsyyz_txt = xsyyz_txt.replace(u'\u3000\u3000', '\n')
xsyyz_txt = xsyyz_txt.replace(u'\u3000', '\n')

# remove chapter markers
ch_mark_set1 = re.findall(pattern=r"(第[一二三四五六七八九十百]{1,3}回[ \n]{1,3}.{7,9}?[ \n]{1,3}.{7,9}?[ \n])",
                          string=xsyyz_txt,
                          flags=re.S | re.M)

for mark in ch_mark_set1:
    xsyyz_txt = xsyyz_txt.replace(mark, "")

xsyyz_txt = xsyyz_txt.replace(u'\n', '')
xsyyz_txt = xsyyz_txt.replace(u' ', '')

with open('/Users/hwang/Desktop/repo/Unmasking-XSYYZ/corpus/XSYYZ_1.txt', 'w', encoding='utf8') as f:
    f.write(xsyyz_txt)
# 《醒世姻缘传》处理结束


# 《女聊斋》处理开始
nlzzy = '/Users/hwang/Desktop/repo/Unmasking-XSYYZ/corpus/NLZZY.txt'
nlzzy_txt = text_handler(nlzzy)
nlzzy_txt = nlzzy_txt.replace(u'\u3000\u3000', '\n')
nlzzy_txt = nlzzy_txt.replace(u'\u3000', '\n')
nlzzy_txt = nlzzy_txt.replace(u'\n', '')
nlzzy_txt = nlzzy_txt.replace(u' ', '')

with open('/Users/hwang/Desktop/repo/Unmasking-XSYYZ/corpus/NLZZY_1.txt', 'w', encoding='utf8') as f:
    f.write(nlzzy_txt)
# 《女聊斋》处理结束


# 《聊斋》处理开始
lzzy = '/Users/hwang/Desktop/repo/Unmasking-XSYYZ/corpus/LZZY.txt'
lzzy_txt = text_handler(lzzy)
lzzy_txt = lzzy_txt.replace(u'\u3000\u3000', '\n')
lzzy_txt = lzzy_txt.replace(u'\u3000', '\n')
lzzy_txt = lzzy_txt.replace(u'\n', '')
lzzy_txt = lzzy_txt.replace(u' ', '')
lzzy_txt = lzzy_txt.replace(u'「', '“')
lzzy_txt = lzzy_txt.replace(u'」', '”')
lzzy_txt = lzzy_txt.replace(u'『', '“')
lzzy_txt = lzzy_txt.replace(u'』', '”')


with open('/Users/hwang/Desktop/repo/Unmasking-XSYYZ/corpus/LZZY_1.txt', 'w', encoding='utf8') as f:
    f.write(lzzy_txt)
# 《聊斋》处理结束


# 《金瓶梅》处理开始
jpm = '/Users/hwang/Desktop/repo/Unmasking-XSYYZ/LanlingXiaoxiaosheng/JPM.txt'
jpm_txt = text_handler(jpm)
jpm_txt = jpm_txt.replace(u'\u3000\u3000', '\n')
jpm_txt = jpm_txt.replace(u'\u3000', '\n')
jpm_txt = jpm_txt.replace(u'\n', '')
jpm_txt = jpm_txt.replace(u' ', '')
jpm_txt = jpm_txt.replace(u'「', '“')
jpm_txt = jpm_txt.replace(u'」', '”')
jpm_txt = jpm_txt.replace(u'『', '“')
jpm_txt = jpm_txt.replace(u'』', '”')


with open('/Users/hwang/Desktop/repo/Unmasking-XSYYZ/LanlingXiaoxiaosheng/JPM_1.txt', 'w', encoding='utf8') as f:
    f.write(jpm_txt)
# 《金瓶梅》处理结束


# 《天史》处理开始
ts = '/Users/hwang/Desktop/repo/Unmasking-XSYYZ/reference/TS.txt'
ts_txt = text_handler(ts)

from hanziconv import HanziConv
ts_txt = HanziConv.toSimplified(ts_txt)

ts_txt = ts_txt.replace(u'\u3000\u3000', '\n')
ts_txt = ts_txt.replace(u'\u3000', '\n')
ts_txt = ts_txt.replace(u'\n', '')
ts_txt = ts_txt.replace(u' ', '')
ts_txt = ts_txt.replace(u'「', '“')
ts_txt = ts_txt.replace(u'」', '”')
ts_txt = ts_txt.replace(u'『', '“')
ts_txt = ts_txt.replace(u'』', '”')

with open('/Users/hwang/Desktop/repo/Unmasking-XSYYZ/reference/TS_1.txt', 'w', encoding='utf8') as f:
    f.write(ts_txt)
# 《天史》处理结束


# 《木皮散人鼓词》处理开始
mpsrgc = '/Users/hwang/Desktop/repo/Unmasking-XSYYZ/JiaYingchong/MPSRGC.txt'
mpsrgc_txt = text_handler(mpsrgc)

# mpsrgc_txt = HanziConv.toSimplified(mpsrgc_txt)

mpsrgc_txt = mpsrgc_txt.replace(u'\u3000\u3000', '\n')
mpsrgc_txt = mpsrgc_txt.replace(u'\u3000', '\n')
mpsrgc_txt = mpsrgc_txt.replace(u'\n', '')
mpsrgc_txt = mpsrgc_txt.replace(u' ', '')
mpsrgc_txt = mpsrgc_txt.replace(u'「', '“')
mpsrgc_txt = mpsrgc_txt.replace(u'」', '”')
mpsrgc_txt = mpsrgc_txt.replace(u'『', '“')
mpsrgc_txt = mpsrgc_txt.replace(u'』', '”')

with open('/Users/hwang/Desktop/repo/Unmasking-XSYYZ/JiaYingchong/MPSRGC_1.txt', 'w', encoding='utf8') as f:
    f.write(mpsrgc_txt)
# 《木皮散人鼓词》处理结束


# 《悲伤逆流成河》处理开始
bsnlch = '/Users/hwang/Desktop/JFZ/corpus/GuoJingMing/BSNLCH.txt'
bsnlch_txt = text_handler(bsnlch)

# mpsrgc_txt = HanziConv.toSimplified(mpsrgc_txt)

bsnlch_txt = bsnlch_txt.replace(u'\u3000\u3000', '\n')
bsnlch_txt = bsnlch_txt.replace(u'\u3000', '\n')
bsnlch_txt = bsnlch_txt.replace(u'\n', '')
bsnlch_txt = bsnlch_txt.replace(u' ', '')
bsnlch_txt = bsnlch_txt.replace(u'「', '“')
bsnlch_txt = bsnlch_txt.replace(u'」', '”')
bsnlch_txt = bsnlch_txt.replace(u'『', '“')
bsnlch_txt = bsnlch_txt.replace(u'』', '”')

with open('/Users/hwang/Desktop/JFZ/corpus/GuoJingMing/BSNLCH_1.txt', 'w', encoding='utf8') as f:
    f.write(bsnlch_txt)
# 《悲伤逆流成河》处理结束


# 《永不原谅》处理开始
ybyl = '/Users/hwang/Desktop/JFZ/corpus/ShangAiLan/YBYL.txt'
ybyl_txt = text_handler(ybyl)

# mpsrgc_txt = HanziConv.toSimplified(mpsrgc_txt)

ybyl_txt = ybyl_txt.replace(u'\u3000\u3000', '\n')
ybyl_txt = ybyl_txt.replace(u'\u3000', '\n')
ybyl_txt = ybyl_txt.replace(u'\n', '')
ybyl_txt = ybyl_txt.replace(u' ', '')
ybyl_txt = ybyl_txt.replace(u'「', '“')
ybyl_txt = ybyl_txt.replace(u'」', '”')
ybyl_txt = ybyl_txt.replace(u'『', '“')
ybyl_txt = ybyl_txt.replace(u'』', '”')

with open('/Users/hwang/Desktop/JFZ/corpus/ShangAiLan/YBYL_1.txt', 'w', encoding='utf8') as f:
    f.write(ybyl_txt)
# 《永不原谅》处理结束


# 《打开天窗》处理开始
dktc = '/Users/hwang/Desktop/JFZ/corpus/unknown/DKTC.txt'
dktc_txt = text_handler(dktc)

# mpsrgc_txt = HanziConv.toSimplified(mpsrgc_txt)

dktc_txt = dktc_txt.replace(u'\u3000\u3000', '\n')
dktc_txt = dktc_txt.replace(u'\u3000', '\n')
dktc_txt = dktc_txt.replace(u'\n', '')
dktc_txt = dktc_txt.replace(u' ', '')
dktc_txt = dktc_txt.replace(u'「', '“')
dktc_txt = dktc_txt.replace(u'」', '”')
dktc_txt = dktc_txt.replace(u'『', '“')
dktc_txt = dktc_txt.replace(u'』', '”')

with open('/Users/hwang/Desktop/JFZ/corpus/unknown/DKTC_1.txt', 'w', encoding='utf8') as f:
    f.write(dktc_txt)
# 《打开天窗》处理结束


# 《他的国》处理开始
tdg = '/Users/hwang/Desktop/repo/Unmasking-JFZ/corpus/reference/他的国_韩寒.txt'
tdg_txt = text_handler(tdg)
tdg_txt = tdg_txt.replace(u'\u3000\u3000', '\n').replace(u'\u3000', '\n').replace(u'\n', '').replace(u' ', '').replace(u'「', '“').replace(u'」', '”').replace(u'『', '“').replace(u'』', '”').replace(u'\n',"")
with open(tdg, 'w', encoding='utf8') as f:
    f.write(tdg_txt)
# 《他的国》处理结束

# 《像少年啦飞驰_韩寒.txt》处理开始
xsnlfc = '/Users/hwang/Desktop/repo/Unmasking-JFZ/corpus/reference/像少年啦飞驰_韩寒.txt'
xsnlfc_txt = text_handler(xsnlfc)
xsnlfc_txt = xsnlfc_txt.replace(u'\u3000\u3000', '\n').replace(u'\u3000', '\n').replace(u'\n', '').replace(u' ', '').replace(u'「', '“').replace(u'」', '”').replace(u'『', '“').replace(u'』', '”').replace(u'\n',"")
with open(xsnlfc, 'w', encoding='utf8') as f:
    f.write(xsnlfc_txt)
# 《像少年啦飞驰_韩寒.txt》处理结束


# 《小王子_圣埃克苏佩里.txt》处理开始
xwz = '/Users/hwang/Desktop/repo/Unmasking-JFZ/corpus/reference/小王子_圣埃克苏佩里.txt'
xwz_txt = text_handler(xwz)
xwz_txt = xwz_txt.replace(u'\u3000\u3000', '\n').replace(u'\u3000', '\n').replace(u'\n', '').replace(u' ', '').replace(u'「', '“').replace(u'」', '”').replace(u'『', '“').replace(u'』', '”').replace(u'\n',"")
with open(xwz, 'w', encoding='utf8') as f:
    f.write(xwz_txt)
# 《小王子_圣埃克苏佩里.txt》处理结束


# 《按时长大_蒋方舟.txt》处理开始
aszd = '/Users/hwang/Desktop/repo/Unmasking-JFZ/corpus/reference/按时长大_蒋方舟.txt'
aszd_txt = text_handler(aszd)
aszd_txt = aszd_txt.replace(u'\u3000\u3000', '\n').replace(u'\u3000', '\n').replace(u'\n', '').replace(u' ', '').replace(u'「', '“').replace(u'」', '”').replace(u'『', '“').replace(u'』', '”').replace(u'\n',"")
with open(aszd, 'w', encoding='utf8') as f:
    f.write(aszd_txt)
# 《按时长大_蒋方舟.txt》处理结束

# 《梦里花落知多少_郭敬明.txt》处理开始
mlhlzds = '/Users/hwang/Desktop/repo/Unmasking-JFZ/corpus/reference/梦里花落知多少_郭敬明.txt'
mlhlzds_txt = text_handler(mlhlzds)
mlhlzds_txt = mlhlzds_txt.replace(u'\u3000\u3000', '\n').replace(u'\u3000', '\n').replace(u'\n', '').replace(u' ', '').replace(u'「', '“').replace(u'」', '”').replace(u'『', '“').replace(u'』', '”').replace(u'\n',"")
with open(mlhlzds, 'w', encoding='utf8') as f:
    f.write(mlhlzds_txt)
# 《梦里花落知多少_郭敬明.txt》处理结束


# 《檞寄生_蔡智恒.txt》处理开始
hjs = '/Users/hwang/Desktop/repo/Unmasking-JFZ/corpus/reference/檞寄生_蔡智恒.txt'
hjs_txt = text_handler(hjs)
hjs_txt = hjs_txt.replace(u'\u3000\u3000', '\n').replace(u'\u3000', '\n').replace(u'\n', '').replace(u' ', '').replace(u'「', '“').replace(u'」', '”').replace(u'『', '“').replace(u'』', '”').replace(u'\n',"")
with open(hjs, 'w', encoding='utf8') as f:
    f.write(hjs_txt)
# 《檞寄生_蔡智恒.txt》处理结束


# 《正在发育_蒋方舟.txt》处理开始
zzfy = '/Users/hwang/Desktop/repo/Unmasking-JFZ/corpus/reference/正在发育_蒋方舟.txt'
zzfy_txt = text_handler(zzfy).replace(u'\u3000\u3000', '\n').replace(u'\u3000', '\n').replace(u'\n', '').replace(u' ', '').replace(u'「', '“').replace(u'」', '”').replace(u'『', '“').replace(u'』', '”').replace(u'\n',"")
with open(zzfy, 'w', encoding='utf8') as f:
    f.write(zzfy_txt)
# 《正在发育_蒋方舟.txt》处理结束

# 《永不原谅_尚爱兰.txt》处理开始
ybyl = '/Users/hwang/Desktop/repo/Unmasking-JFZ/corpus/reference/永不原谅_尚爱兰.txt'
ybyl_txt = text_handler(ybyl).replace(u'\u3000\u3000', '\n').replace(u'\u3000', '\n').replace(u'\n', '').replace(u' ', '').replace(u'「', '“').replace(u'」', '”').replace(u'『', '“').replace(u'』', '”').replace(u'\n',"")
with open(ybyl, 'w', encoding='utf8') as f:
    f.write(ybyl_txt)
# 《永不原谅_尚爱兰.txt》处理结束

# 《没有人像我一样_饶雪漫.txt》处理开始
myrxwyy = '/Users/hwang/Desktop/repo/Unmasking-JFZ/corpus/reference/没有人像我一样_饶雪漫.txt'
myrxwyy_txt = text_handler(myrxwyy).replace(u'\u3000\u3000', '\n').replace(u'\u3000', '\n').replace(u'\n', '').replace(u' ', '').replace(u'「', '“').replace(u'」', '”').replace(u'『', '“').replace(u'』', '”').replace(u'\n',"")
with open(myrxwyy, 'w', encoding='utf8') as f:
    f.write(myrxwyy_txt)
# 《没有人像我一样_饶雪漫.txt》处理结束

# 《花季雨季_郁秀.txt》处理开始
hjyj = '/Users/hwang/Desktop/repo/Unmasking-JFZ/corpus/reference/花季雨季_郁秀.txt'
hjyj_txt = text_handler(hjyj).replace(u'\u3000\u3000', '\n').replace(u'\u3000', '\n').replace(u'\n', '').replace(u' ', '').replace(u'「', '“').replace(u'」', '”').replace(u'『', '“').replace(u'』', '”').replace(u'\n',"")
with open(hjyj, 'w', encoding='utf8') as f:
    f.write(hjyj_txt)
# 《花季雨季_郁秀.txt》处理结束

# 《草样年华_孙睿.txt》处理开始
cynh = '/Users/hwang/Desktop/repo/Unmasking-JFZ/corpus/reference/草样年华_孙睿.txt'
cynh_txt = text_handler(cynh).replace(u'\u3000\u3000', '\n').replace(u'\u3000', '\n').replace(u'\n', '').replace(u' ', '').replace(u'「', '“').replace(u'」', '”').replace(u'『', '“').replace(u'』', '”').replace(u'\n',"")
with open(cynh, 'w', encoding='utf8') as f:
    f.write(cynh_txt)
# 《草样年华_孙睿.txt》处理结束

# 《都往我这看_蒋方舟.txt》处理开始
dwwzk = '/Users/hwang/Desktop/repo/Unmasking-JFZ/corpus/reference/都往我这看_蒋方舟.txt'
dwwzk_txt = text_handler(dwwzk).replace(u'\u3000\u3000', '\n').replace(u'\u3000', '\n').replace(u'\n', '').replace(u' ', '').replace(u'「', '“').replace(u'」', '”').replace(u'『', '“').replace(u'』', '”').replace(u'\n',"")
with open(dwwzk, 'w', encoding='utf8') as f:
    f.write(dwwzk_txt)
# 《都往我这看_蒋方舟.txt》处理结束

# 《闹学记_三毛.txt》处理开始
nxj = '/Users/hwang/Desktop/repo/Unmasking-JFZ/corpus/reference/闹学记_三毛.txt'
nxj_txt = text_handler(nxj).replace(u'\u3000\u3000', '\n').replace(u'\u3000', '\n').replace(u'\n', '').replace(u' ', '').replace(u'「', '“').replace(u'」', '”').replace(u'『', '“').replace(u'』', '”').replace(u'\n',"")
with open(nxj, 'w', encoding='utf8') as f:
    f.write(nxj_txt)
# 《闹学记_三毛.txt》处理结束

# 《青春前期_蒋方舟.txt》处理开始
qcqq = '/Users/hwang/Desktop/repo/Unmasking-JFZ/corpus/reference/青春前期_蒋方舟.txt'
qcqq_txt = text_handler(qcqq).replace(u'\u3000\u3000', '\n').replace(u'\u3000', '\n').replace(u'\n', '').replace(u' ', '').replace(u'「', '“').replace(u'」', '”').replace(u'『', '“').replace(u'』', '”').replace(u'\n',"")
with open(qcqq, 'w', encoding='utf8') as f:
    f.write(qcqq_txt)
# 《青春前期_蒋方舟.txt》处理结束

# 《悲伤逆流成河_郭敬明.txt》处理开始
bsnlch = '/Users/hwang/Desktop/repo/Unmasking-JFZ/corpus/reference/悲伤逆流成河_郭敬明.txt'
bsnlch_txt = text_handler(bsnlch).replace(u'\u3000\u3000', '\n').replace(u'\u3000', '\n').replace(u'\n', '').replace(u' ', '').replace(u'「', '“').replace(u'」', '”').replace(u'『', '“').replace(u'』', '”').replace(u'\n',"")
with open(bsnlch, 'w', encoding='utf8') as f:
    f.write(bsnlch_txt)
# 《悲伤逆流成河_郭敬明.txt》处理结束

# 《打开天窗.txt》处理开始
dktc = '/Users/hwang/Desktop/repo/Unmasking-JFZ/corpus/target/打开天窗.txt'
dktc_txt = text_handler(dktc).replace(u'\u3000\u3000', '\n').replace(u'\u3000', '\n').replace(u'\n', '').replace(u' ', '').replace(u'「', '“').replace(u'」', '”').replace(u'『', '“').replace(u'』', '”').replace(u'\n',"")
with open(dktc, 'w', encoding='utf8') as f:
    f.write(dktc_txt)
# 《打开天窗.txt》处理结束
