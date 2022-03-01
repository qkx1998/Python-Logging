import random

# 一个0-1的随机数
random.random()

#一个范围内的随机浮点数
random.uniform(1,2)

#一个范围内的随机整数
random.randint(1,5)

#从序列中随机选择一个元素
random.choice([1,2,3])
random.choice(['1','2','3'])

# 随机打乱列表
list = [1,2,4,5]
random.shuffle(list)

# 随机获取指定长度的序列
list2 = random.sample(list, 2)

import numpy as np

# 生成5个随机数(均匀分布) 貌似都是0-1的
np.random.rand(5)

# 生成5个随机数(正太分布) 有小于0的数 也有大于1的数
np.random.randn(5)

# 随机5个指定范围(1-100)内的整数
np.random.randint(1, 100, 5)

# 随机0或1的10个数
np.random.randint(0,2,10)

# 随机N个偶数 :这里的N需要自己再控制一下
[x for x in np.random.randint(1,100, 10) if x % 2 == 0]
