# -*- coding: utf-8 -*-
"""
@author:XuMing（xuming624@qq.com)
@description: 
"""
import pycorrector

# 做为一个合格的小仙女	作为一个合格的小仙女
# 得发展	的发展
# 概是2000万	大概是2000万
# 好百年家具	好百年家居
# 有吃泄药的	有吃泻药的
# 电气的电压不超过12v	电器的电压不超过12v
# 也被称做“非洲之星”	也被称作"非洲之星”
# 年收入大概20w	年收入大概20万
# 老婆问我吃饿了不	老婆问我吃饭了不
# 有很长的路要走”	有长长的路要走”
# 主要化学成份氯化钠	主要化学成分氯化钠
# 天地无垠	天地无限
# 方大碳素等等	方大炭素等等
# 耐得住欲妄	耐得住欲望
# 真真的讽刺	真正的讽刺
# 交通先行	交通限行
# 母子平爱	母子平安
# 打到敌人三次之后	打倒敌人三次之后
# 热的满头大汉	热的满头大汗
# 最不成才	最不成材
# 或被暂扣、吊销或撤消的	或被暂扣 吊销或撤销的
# 不由的感叹道	不由得感叹道
# 你想随意而安	你想随遇而安
# 到目前为之	到目前为止
# 吹唐人记忆	吹糖人记忆
# 一阙词牌名	一阕词牌名

error_sentences = [
    '我兴高彩列地去公园游玩',
    '吹唐人记忆',
    '老师工作非常幸苦,我们要遵敬老师',
    ' 我兴高彩列地去公园游玩',
]
for line in error_sentences:
    print(pycorrector.detect(line))
    correct_sent = pycorrector.correct(line)
    print("original sentence:{} => correct sentence:{}".format(line, correct_sent))
