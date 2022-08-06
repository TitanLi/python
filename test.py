import twstock
stock = twstock.Stock('1101')
data = stock.sid
print(data)
# 取得日期
stock.fetch(2021, 11)
# 取得價錢
priceByDay = stock.price
print(priceByDay)
# 計算五日平均價格
move5DayAveragePrice = stock.moving_average(stock.price, 5)
print(move5DayAveragePrice)
# 計算五日平均交易量
move5DayAverageCapacity = stock.moving_average(stock.capacity, 5)
print(move5DayAverageCapacity)
# 計算五日、十日乖離值
ma5DayRatio = stock.ma_bias_ratio(1, 5)
print(ma5DayRatio)

# 量大收紅 / 量大收黑
# 量縮價不跌 / 量縮價跌
# 三日均價由下往上 / 三日均價由上往下
# 三日均價大於六日均價 / 三日均價小於六日均價
bfp = twstock.BestFourPoint(stock)
# 判斷是否為四大買點
best4BuyPoint = bfp.best_four_point_to_buy()
# 判斷是否為四大賣點
best4SellPoint = bfp.best_four_point_to_sell()
# 綜合判斷
comprehensive = bfp.best_four_point()
print(best4BuyPoint)
print(best4SellPoint)
print(comprehensive)