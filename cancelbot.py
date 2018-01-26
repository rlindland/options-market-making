from tradersbot import *

t = TradersBot('127.0.0.1', 'trader0', 'trader0')
current_log = [[],[]]
old_log = [[],[]]
old_log2 = [[],[]]
old_log3 = [[],[]]

def process(msg, order):

    print("updated")

    global current_log, old_log, old_log2, old_log3

    old_log3 = old_log2
    old_log2 = old_log
    old_log = current_log

    current_log = [[],[]]

    for order_id in msg['trader_state']['open_orders']:
        current_log[0].append(msg['trader_state']['open_orders'][order_id]['order_id'])
        print(msg['trader_state']['open_orders'][order_id]['ticker'])
        current_log[1].append(msg['trader_state']['open_orders'][order_id]['ticker'])

    for i in range(len(old_log3[0])):
        order.addCancel(old_log3[1][i], old_log3[0][i])
        print("cancelled")

    print(msg['trader_state']['open_orders'])

t.onTraderUpdate = process
t.run()