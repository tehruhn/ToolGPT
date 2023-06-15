from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["Blockchain"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 1-m', geo='', gprop='')
iot = pytrends.interest_over_time()
print(iot[kw_list[0]])