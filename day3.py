# import pdb # for debugging

# # aList = [1,2,3,4,5]

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f = f*i
#     return f

# pdb.set_trace()

# fact(5)

# while(True):
#     aList.pop()
#     print(aList)

import logging

logging.basicConfig(level=logging.DEBUG,
                    format = "%(asctime) s %(levelname) s %(message) s",
                    filename="Day5.log",filemode="a") # debug is the lowest level in order: debug, info, warning, error, critical

logging.info("THIS IS A INFO")
logging.debug("THIS IS A DEBUG VALUE")
logging.warning("THIS IS A WARNING")
logging.error("THIS IS AN ERROR")
logging.critical("DANGEROUS")