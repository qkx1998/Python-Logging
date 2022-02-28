import logging

'''
使用basicConfig()来指定日志级别和相关信息
DEBUG：详细的信息,通常只出现在诊断问题上
INFO：确认一切按预期运行
WARNING：一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”)。这个软件还能按预期工作。
ERROR：更严重的问题,软件没能执行一些功能
CRITICAL：一个严重的错误,这表明程序本身可能无法继续运行

'''
logging.basicConfig(level=logging.DEBUG 
                    
                    #log日志输出的文件位置和文件名
                    ,filename="demo.log" 
                    
                    #文件的写入格式，w为重新写入文件，默认是追加
                    ,filemode="w" 
                    
                    #日志输出的格式,-8表示占位符，让输出左对齐，输出长度都为8位
                    ,format="%(asctime)s - %(name)s - %(levelname)-9s - %(filename)-8s : %(lineno)s line - %(message)s" 
                    
                    # #时间输出的格式
                    ,datefmt="%Y-%m-%d %H:%M:%S" 
                    )

logging.debug("This is  DEBUG !!")
logging.info("This is  INFO !!")
logging.warning("This is  WARNING !!")
logging.error("This is  ERROR !!")
logging.critical("This is  CRITICAL !!")

# 使用logging.exception(e)去记录报错和报错的原因
try:
    3/0
except Exception as e:
    logging.exception(e)
