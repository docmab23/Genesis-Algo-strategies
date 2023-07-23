import pybroker as pyb
from datetime import datetime
from pybroker import ExecContext, Strategy, YFinance, StrategyConfig

pyb.enable_data_source_cache('rebalancing')
config = StrategyConfig(initial_cash=500_000)




def start_of_month(dt: datetime) -> bool:
    if dt.month != pyb.param('current_month'):
        pyb.param('current_month', dt.month)
        return True
    return False

def set_target_shares(
    ctxs: dict[str, ExecContext],
    targets: dict[str, float]
):
    #print(ctxs)
    for symbol, target in targets.items():
        ctx = ctxs[symbol]
        target_shares = ctx.calc_target_shares(target)
        print(target_shares)
        pos = ctx.long_pos()
        if pos is None:
            ctx.buy_shares = target_shares
        elif pos.shares < target_shares:
            ctx.buy_shares = target_shares - pos.shares
        elif pos.shares > target_shares:
            ctx.sell_shares = pos.shares - target_shares

def rebalance(ctxs: dict[str, ExecContext]):
    dt = tuple(ctxs.values())[0].dt
    #print(dt)
    if start_of_month(dt):
        target = 1 / len(ctxs)
        set_target_shares(ctxs, {symbol: target for symbol in ctxs.keys()})

    #print(((ctxs["TSLA"]._curr_date)))
def buy_low(ctx):
    # If shares were already purchased and are currently being held, then return.
    if ctx.long_pos():
        print(dir(ctx))
        return
    # If the latest close price is less than the previous day's low price,
    # then place a buy order.
    if ctx.bars >= 2 and ctx.close[-1] < ctx.low[-2]:
        # Buy a number of shares that is equal to 25% the portfolio.
        #print(ctx)
        ctx.buy_shares = ctx.calc_target_shares(0.25)
        # Set the limit price of the order.
        ctx.buy_limit_price = ctx.close[-1] - 0.01
        # Hold the position for 3 bars before liquidating (in this case, 3 days).
        ctx.hold_bars = 3
        


strategy = Strategy(YFinance(), start_date='1/1/2018', end_date='1/1/2023')
strategy.set_after_exec(rebalance)
strategy.add_execution(buy_low, ['TSLA','NFLX','AAPL','NVDA','AMZN'])

#strategy.add_execution(short_high, ['MSFT'])

result = strategy.backtest()

#print(result.orders)
import matplotlib.pyplot as plt
chart = plt.subplot2grid((3, 2), (0, 0), rowspan=3, colspan=2)
chart.plot(result.portfolio.index, result.portfolio['market_value'])


p

