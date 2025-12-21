
import order
import pay

print(order.max_amount)

order.create_order()
order.cancel_order()
order.info()

print(pay.timeout)
pay.alipay_pay()
pay.wechat_pay()
pay.info()

