# -*- coding: utf-8 -*-
# @Time    : 2020-09-11 20:59
# @Author  : XU
# @File    : demo2.py
# @Software: PyCharm
import re

html = '<p class="txt" node-type="feed_list_content" nick-name="人民日报">\n                    【<a href="http://s.weibo.com/weibo?q=" target="_blank">#13个求职新方向#</a>！有你心动的职业吗<img src="//img.t.sinajs.cn/t4/appstyle/expression/ext/normal/aa/2018new_bingbujiandan_org.png" title="[并不简单]" alt="[并不简单]" class="face">】近日，人社部、市场监管总局、统计局联合发布13个新职业，既有现在流行的人工智能、<em class="s-color-red">大</em><em class="s-color-red">数据</em>、云计算、物联网等工程技术人员，也有电子竞技员、无人机驾驶员等新颖工种…你心动了吗？哪些学校开设了相关专业值得关注？戳图了解↓↓转给正在求学的TA！                </p>'
pre = re.compile('>(.*?)<')
text = ''.join(pre.findall(html))
print(text)
