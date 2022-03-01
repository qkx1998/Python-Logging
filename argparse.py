'''
argparse: 用于解析命令行参数和选项的标准模块。其使用主要分为以下四步：

1 import argparse

2 parser = argparse.ArgumentParser() : 创建一个解析对象

3 parser.add_argument() ：向对象中添加需要关注的命令行参数和选项

4 parser.parser_args() ： 进行解析
'''

import argparse

def get_para(seed):
    parser = argparse.ArgumentParser(description='help info')
    parser.add_argument('--FOLDS', default=5, type=int)
    parser.add_argument('--tfidf_size', default=10, type=int)
    parser.add_argument('--SEED', default=1116, type=int)
    #parser.print_help()
    
    # 命令行中写法，但在jupyter中运行会报错
    # args = parser.parse_args()
    # 由于在jupyter notebook中，args不为空。将上面代码中的最后一行修改如下即可
    args = parser.parse_args(args=[])
  
    print('\n')
    print('-'*10+'params'+'-'*10)
    # 遍历打印所有的参数
    for arg in args._get_kwargs():
        print(f'{arg[0]} : {arg[1]}')
    return args
  
# 参数实例化
args = get_para(2)
print(args.FOLDS, args.tfidf_size, args.SEED) # 返回 5 10 1116

args.FOLDS = 7 # 进行重新赋值，改变参数
print(args.FOLDS) # 返回 7

# 函数调用时
model(seed = args.SEED, fold=args.FOLD, tfidf_size = args.tfidf_size, ...)

# 在命令行中运行程序时，可以按照以下的格式：
python 程序名.py --FOLDS 10 --SEED 2 

# 如果不想使用--标签，就必须保证按照参数输入的先后顺序进行赋值，且赋值的参数数量要等于args的参数数量
python 程序名.py 10 2 10
