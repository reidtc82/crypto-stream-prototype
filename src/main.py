import cryptowatch as cw
import logging
import time

logging.basicConfig()
logging.getLogger("cryptowatch").setLevel(logging.DEBUG)

# Set your API Key
cw.api_key = "8OPDUPOO1J7M0KNU2Q02"

cw.stream.subscriptions = ["markets:*:trades", "markets:*:ohlc"]
# cw.stream.subscriptions = ["assets:60:book:snapshots"]
# cw.stream.subscriptions = ["assets:60:book:spread"]
# cw.stream.subscriptions = ["assets:60:book:deltas"]
# cw.stream.subscriptions = ["markets:*:ohlc"]
# cw.stream.subscriptions = ["markets:*:trades"]


# What to do with each trade update
def handle_trades_update(trade_update):
    print(trade_update)


cw.stream.on_trades_update = handle_trades_update


# What to do with each candle update
def handle_intervals_update(interval_update):
    print(interval_update)


cw.stream.on_intervals_update = handle_intervals_update


# What to do with each orderbook spread update
def handle_orderbook_snapshot_updates(orderbook_snapshot_update):
    print(orderbook_snapshot_update)


cw.stream.on_orderbook_snapshot_update = handle_orderbook_snapshot_updates


# What to do with each orderbook spread update
def handle_orderbook_spread_updates(orderbook_spread_update):
    print(orderbook_spread_update)


cw.stream.on_orderbook_spread_update = handle_orderbook_spread_updates


# What to do with each orderbook delta update
def handle_orderbook_delta_updates(orderbook_delta_update):
    print(orderbook_delta_update)


cw.stream.on_orderbook_delta_update = handle_orderbook_delta_updates


# Start receiving
cw.stream.connect()

time.sleep(1)

# Stop receiving
cw.stream.disconnect()
