from tradersbot import *

from time import sleep
from time import time

import blackscholes
import numpy as np
from scipy.stats import norm
import math
import copy

t = TradersBot('127.0.0.1', 'trader0', 'trader0')

class BaseBot():
    def __init__(self):
        self.count = 0
        self.deltas = 0
        self.vegas = 0
        self.elapsedTime = 0
        self.topBid = {}
        self.topAsk = {}
        self.avgAsk = {}
        self.avgBid = {}
        self.lastPrices = {"TMXFUT": 100,
                           'T80P': 0,
                           'T80C': 0,
                           'T81P': 0,
                           'T81C': 0,
                           'T82P': 0,
                           'T82C': 0,
                           'T83P': 0,
                           'T83C': 0,
                           'T84P': 0,
                           'T84C': 0,
                           'T85P': 0,
                           'T85C': 0,
                           'T86P': 0,
                           'T86C': 0,
                           'T87P': 0,
                           'T87C': 0,
                           'T88P': 0,
                           'T88C': 0,
                           'T89P': 0,
                           'T89C': 0,
                           'T90P': 0,
                           'T90C': 0,
                           'T91P': 0,
                           'T91C': 0,
                           'T92P': 0,
                           'T92C': 0,
                           'T93P': 0,
                           'T93C': 0,
                           'T94P': 0,
                           'T94C': 0,
                           'T95P': 0,
                           'T95C': 0,
                           'T96P': 0,
                           'T96C': 0,
                           'T97P': 0,
                           'T97C': 0,
                           'T98P': 0,
                           'T98C': 0,
                           'T99P': 0,
                           'T99C': 0,
                           'T100P': 0,
                           'T100C': 0,
                           'T101P': 0,
                           'T101C': 0,
                           'T102P': 0,
                           'T102C': 0,
                           'T103P': 0,
                           'T103C': 0,
                           'T104P': 0,
                           'T104C': 0,
                           'T105P': 0,
                           'T105C': 0,
                           'T106P': 0,
                           'T106C': 0,
                           'T107P': 0,
                           'T107C': 0,
                           'T108P': 0,
                           'T108C': 0,
                           'T109P': 0,
                           'T109C': 0,
                           'T110P': 0,
                           'T110C': 0,
                           'T111P': 0,
                           'T111C': 0,
                           'T112P': 0,
                           'T112C': 0,
                           'T113P': 0,
                           'T113C': 0,
                           'T114P': 0,
                           'T114C': 0,
                           'T115P': 0,
                           'T115C': 0,
                           'T116P': 0,
                           'T116C': 0,
                           'T117P': 0,
                           'T117C': 0,
                           'T118P': 0,
                           'T118C': 0,
                           'T119P': 0,
                           'T119C': 0,
                           'T120P': 0,
                           'T120C': 0, }
        self.positions = {'T80P': 0,
                          'T80C': 0,
                          'T81P': 0,
                          'T81C': 0,
                          'T82P': 0,
                          'T82C': 0,
                          'T83P': 0,
                          'T83C': 0,
                          'T84P': 0,
                          'T84C': 0,
                          'T85P': 0,
                          'T85C': 0,
                          'T86P': 0,
                          'T86C': 0,
                          'T87P': 0,
                          'T87C': 0,
                          'T88P': 0,
                          'T88C': 0,
                          'T89P': 0,
                          'T89C': 0,
                          'T90P': 0,
                          'T90C': 0,
                          'T91P': 0,
                          'T91C': 0,
                          'T92P': 0,
                          'T92C': 0,
                          'T93P': 0,
                          'T93C': 0,
                          'T94P': 0,
                          'T94C': 0,
                          'T95P': 0,
                          'T95C': 0,
                          'T96P': 0,
                          'T96C': 0,
                          'T97P': 0,
                          'T97C': 0,
                          'T98P': 0,
                          'T98C': 0,
                          'T99P': 0,
                          'T99C': 0,
                          'T100P': 0,
                          'T100C': 0,
                          'T101P': 0,
                          'T101C': 0,
                          'T102P': 0,
                          'T102C': 0,
                          'T103P': 0,
                          'T103C': 0,
                          'T104P': 0,
                          'T104C': 0,
                          'T105P': 0,
                          'T105C': 0,
                          'T106P': 0,
                          'T106C': 0,
                          'T107P': 0,
                          'T107C': 0,
                          'T108P': 0,
                          'T108C': 0,
                          'T109P': 0,
                          'T109C': 0,
                          'T110P': 0,
                          'T110C': 0,
                          'T111P': 0,
                          'T111C': 0,
                          'T112P': 0,
                          'T112C': 0,
                          'T113P': 0,
                          'T113C': 0,
                          'T114P': 0,
                          'T114C': 0,
                          'T115P': 0,
                          'T115C': 0,
                          'T116P': 0,
                          'T116C': 0,
                          'T117P': 0,
                          'T117C': 0,
                          'T118P': 0,
                          'T118C': 0,
                          'T119P': 0,
                          'T119C': 0,
                          'T120P': 0,
                          'T120C': 0,
                          'TMXFUT': 0, }
        self.expect_positions = {'T80P': 0,
                                 'T80C': 0,
                                 'T81P': 0,
                                 'T81C': 0,
                                 'T82P': 0,
                                 'T82C': 0,
                                 'T83P': 0,
                                 'T83C': 0,
                                 'T84P': 0,
                                 'T84C': 0,
                                 'T85P': 0,
                                 'T85C': 0,
                                 'T86P': 0,
                                 'T86C': 0,
                                 'T87P': 0,
                                 'T87C': 0,
                                 'T88P': 0,
                                 'T88C': 0,
                                 'T89P': 0,
                                 'T89C': 0,
                                 'T90P': 0,
                                 'T90C': 0,
                                 'T91P': 0,
                                 'T91C': 0,
                                 'T92P': 0,
                                 'T92C': 0,
                                 'T93P': 0,
                                 'T93C': 0,
                                 'T94P': 0,
                                 'T94C': 0,
                                 'T95P': 0,
                                 'T95C': 0,
                                 'T96P': 0,
                                 'T96C': 0,
                                 'T97P': 0,
                                 'T97C': 0,
                                 'T98P': 0,
                                 'T98C': 0,
                                 'T99P': 0,
                                 'T99C': 0,
                                 'T100P': 0,
                                 'T100C': 0,
                                 'T101P': 0,
                                 'T101C': 0,
                                 'T102P': 0,
                                 'T102C': 0,
                                 'T103P': 0,
                                 'T103C': 0,
                                 'T104P': 0,
                                 'T104C': 0,
                                 'T105P': 0,
                                 'T105C': 0,
                                 'T106P': 0,
                                 'T106C': 0,
                                 'T107P': 0,
                                 'T107C': 0,
                                 'T108P': 0,
                                 'T108C': 0,
                                 'T109P': 0,
                                 'T109C': 0,
                                 'T110P': 0,
                                 'T110C': 0,
                                 'T111P': 0,
                                 'T111C': 0,
                                 'T112P': 0,
                                 'T112C': 0,
                                 'T113P': 0,
                                 'T113C': 0,
                                 'T114P': 0,
                                 'T114C': 0,
                                 'T115P': 0,
                                 'T115C': 0,
                                 'T116P': 0,
                                 'T116C': 0,
                                 'T117P': 0,
                                 'T117C': 0,
                                 'T118P': 0,
                                 'T118C': 0,
                                 'T119P': 0,
                                 'T119C': 0,
                                 'T120P': 0,
                                 'T120C': 0,
                                 'TMXFUT': 0, }
        self.maxPos = 20000
        self.priceChange = {}
        self.pnl = 0

        self.iv_diff_threshold = 0.0001

    def volatility_smile(self):
        prices = []
        for i in range(41):
            prices.append(80.+i)
        ivs = []
        deltas = []
        vegas = []
        calls = []
        puts = []
        if 'TMXFUT' in self.lastPrices:
            for p in prices:
                s = self.lastPrices['TMXFUT']
                k = p
                r = 0
                t = self.elapsedTime
                big_T = 900
                call = self.lastPrices['T' + str(int(p)) + 'C']
                put = self.lastPrices['T' + str(int(p)) + 'P']
                eps = .000001
                o = blackscholes.invert_scalar(s, k, r, t, big_T, call, put, eps)
                ivs.append(o)
                d1 = (math.log(s / k) + (r + o * o / 2) * (big_T - t)) / (o * math.sqrt(big_T - t))
                deltas.append(norm.cdf(d1))
                vegas.append(s * norm.pdf(d1) * math.sqrt(big_T - t))
                calls.append(call)
                puts.append(put)
            return prices, ivs, deltas, vegas, calls, puts
        pass

    def delta(self):
        delta = 0
        prices = []
        for i in range(41):
            prices.append(80.+i)
        deltas = self.volatility_smile()[2]
        for p in prices:
            call_name = 'T' + str(int(p)) + 'C'
            put_name = 'T' + str(int(p)) + 'P'
            delta -= self.positions[put_name] * deltas[prices.index(p)]
            delta += self.positions[call_name] * deltas[prices.index(p)]
        delta += self.positions["TMXFUT"]
        return delta

    def arbitrage(self,msg,order):

        mindiscrep = 0.05

        prices = []
        for i in range(41):
            prices.append(80.+i)

        ivs = self.volatility_smile()[1]

        coefs = self.fitIvs(ivs)

        expected = []
        excall = []
        exput = []
        for i in range(80,121):
            expected.append(coefs[0]*i**4+coefs[1]*i**3+coefs[2]*i*i+coefs[3]*i+coefs[4])

        for i in range(len(prices)):
            s = self.lastPrices['TMXFUT']
            k = prices[i]
            r = 0
            t = self.elapsedTime
            big_T = 900
            excall.append(blackscholes.blackscholes_scalar(s,k,r,expected[i],t,big_T))
            exput.append(excall[i] - self.lastPrices['TMXFUT'] + prices[i])

        for i in range(len(excall)):
            call_name = 'T' + str(int(i + 80)) + 'C'
            put_name = 'T' + str(int(i + 80)) + 'P'
            if call_name in self.topAsk:
                if (1+mindiscrep)*self.topAsk[call_name] < excall[i]:
                    order.addBuy(call_name,1,(1+mindiscrep)*self.topAsk[call_name])
            if call_name in self.topBid:
                if (1-mindiscrep)*self.topBid[call_name] > excall[i]:
                    order.addSell(call_name,1,(1-mindiscrep)*self.topBid[call_name])
            if put_name in self.topAsk:
                if (1+mindiscrep)*self.topAsk[put_name] < exput[i]:
                    order.addBuy(put_name,1,(1+mindiscrep)*self.topAsk[put_name])
            if put_name in self.topBid:
                if (1-mindiscrep)*self.topBid[put_name] > exput[i]:
                    order.addSell(put_name,1,(1-mindiscrep)*self.topAsk[put_name])

    def update(self, msg):
        if type(msg.get('elapsed_time')) == int:
            self.elapsedTime = msg.get('elapsed_time')

        if msg.get('market_states'):
            raise KeyError
            for ticker, state in msg['market_states'].iteritems():
                if len(state['bids']):
                    self.topBid[ticker] = max(map(float, state['bids'].keys()))
                if len(state['asks']):
                    self.topAsk[ticker] = min(map(float, state['asks'].keys()))
                self.lastPrices[ticker] = state['last_price']
                self.priceChange[ticker] = 0

        # Update internal book for a single ticker

        if msg.get('market_state'):
            state = msg['market_state']
            ticker = state['ticker']
            if len(state['bids']):
                self.topBid[ticker] = max(map(float, state['bids'].keys()))
                self.avgBid[ticker] = round(np.mean(list(map(float, state['bids'].keys()))), 2)
            if len(state['asks']):
                self.topAsk[ticker] = min(map(float, state['asks'].keys()))
                self.avgAsk[ticker] = round(np.mean(list(map(float, state['asks'].keys()))), 2)

            self.lastPrices[ticker] = state['last_price']
        else:
            return None

    def update_positions(self, msg,order):
        if msg.get('trader_state'):
            self.positions = msg['trader_state']['positions']
        if msg.get('message_type') == 'TRADER UPDATE':
            self.cash = msg["trader_state"]["cash"]["USD"]
            self.pnl = msg["trader_state"]["pnl"]["USD"]

    def process(self, msg, order):
        ##if msg.get('market_state') or msg.get('trader_state') or msg.get('market_states'):
        self.update(msg)
        self.update_positions(msg,order)
        d = 0
        if self.count >= 300 and self.count%300==0:
            d = self.delta()
            print(d)
        if self.count > 600 and self.count%600 == 0:
            self.better_delta_hedge(d, msg, order)
        if self.count >= 300 and self.count%600==0:
            d = self.delta()
        if self.count % 300 == 0:
            if d < 120:
                self.make_better_call_market(msg, order)
            if d > -120:
                self.make_better_put_market(msg, order)
        print(self.pnl)

        self.count += 1

    def fitIvs(self, ivs):
        x = []
        for i in range(41):
            x.append(80.+i)
        return np.polyfit(x,ivs,4)

    def make_market(self, msg, order):
        for option in self.positions.keys():
            quantity = 25
            shift = 0
            if option in self.topAsk and option in self.topBid:
                if d < 300:
                    order.addBuy(option, quantity, self.avgBid[option]+shift)
                if d > -300:
                    order.addSell(option, quantity, self.avgAsk[option]-shift)
            

    def make_call_market(self, msg, order):
        for i in range(41):
            option = 'T' + str(int(i + 80)) + 'C'
            quantity = 25
            shift = 0
            if option in self.topAsk and option in self.topBid:
                order.addBuy(option, quantity, self.avgBid[option]+shift)
                order.addSell(option, quantity, self.avgAsk[option]-shift)
            else:
                print('-------------------------------------')

    def make_put_market(self, msg, order):
        for i in range(41):
            option = 'T' + str(int(i + 80)) + 'P'
            quantity = 25
            shift = 0
            if option in self.topAsk and option in self.topBid:
                order.addBuy(option, quantity, self.avgBid[option]+shift)
                order.addSell(option, quantity, self.avgAsk[option]-shift)
            else:
                print('-------------------------------------')

    def make_better_call_market(self, msg, order):
        for i in range(41):
            c_option = 'T' + str(int(i + 80)) + 'C'
            p_option = 'T' + str(int(i + 80)) + 'P'
            quantity = 10
            shift = 0
            if c_option in self.topAsk and c_option in self.topBid:
                order.addBuy(c_option, quantity, self.avgBid[c_option]+shift)
            if p_option in self.topAsk and p_option in self.topBid:
                order.addSell(p_option, quantity, self.avgAsk[p_option]-shift)
            
    def make_better_put_market(self, msg, order):
        for i in range(41):
            c_option = 'T' + str(int(i + 80)) + 'C'
            p_option = 'T' + str(int(i + 80)) + 'P'
            quantity = 10
            shift = 0
            if p_option in self.topAsk and p_option in self.topBid:
                order.addBuy(p_option, quantity, self.avgBid[p_option]+shift)
            if c_option in self.topAsk and c_option in self.topBid:
                order.addSell(c_option, quantity, self.avgAsk[c_option]-shift)
           

    def delta_hedge(self, msg, order):
        d = self.delta()
        if abs(d) > 120:
            print(d)
            quantity = int(abs(d) - 100)
            print(self.topAsk['TMXFUT'])
            order.addBuy('TMXFUT', quantity, self.topAsk['TMXFUT']+10)
            
        if d > 150:
            print(d)
            quantity = int(d)-100
            order.addSell('TMXFUT', quantity, self.topAsk['TMXFUT']-10)

    def better_delta_hedge(self, d, msg, order):
        if d < -120:
            print(d)
            quantity = min(int(abs(d) - 100), 400)
            order.addBuy('TMXFUT', quantity, self.topAsk['TMXFUT']+10)
            
        if d > 120:
            print(d)
            quantity = min(int(d)-100, 400)
            order.addSell('TMXFUT', quantity, self.topBid['TMXFUT']-10)



b = BaseBot()

t.onMarketUpdate = b.process
t.onTraderUpdate = b.update_positions
t.run()

#changed avgAsk, Bid, make_market