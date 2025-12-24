
# import order
# import pay
#
# print(order.max_amount)
#
# order.create_order()
# order.cancel_order()
# order.info()
#
# print(pay.timeout)
# pay.alipay_pay()
# pay.wechat_pay()
# pay.info()
##############################
# import order as o
# import pay as p
#
# print(o.max_amount)
# o.create_order()
# o.cancel_order()
# o.info()
#
# print(p.timeout)
# p.alipay_pay()
# p.wechat_pay()
# p.info()
#
#############################
#
# from order import max_amount, create_order, cancel_order, info
# from pay import timeout, wechat_pay, alipay_pay, info
#
# max_amount = 10
#
# print(max_amount)
# print(timeout)
#
# create_order()
# cancel_order()
# alipay_pay()
# wechat_pay()
# info()


#############################

# from order import  info as o_info
# from pay import info as p_info
#
# o_info()
# p_info()
#
# timeout = 0
#

#############################
# from order import *
#
# print(max_amount)
# create_order()
# cancel_order()
# info()

############

import son

print('主模块执行-开始')

print(__name__)

son.fun()

