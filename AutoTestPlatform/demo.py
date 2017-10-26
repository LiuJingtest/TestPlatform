import requests, json

#
# test = requests.get("https://securitiesapi.stocks666.com",params="/api/securities/stock/913256409/recommendation", verify=False)
# print(test.json())
#
#
# if "hdjead".find("a"):
#     print(2)
#
# test = {"rating": "1.7", "trends": [{"age": "OneWeekAgo", "numberOfAnalysts": 35, "distributionList": [{"Recommendation": 1, "NumberOfAnalysts": 11}, {"Recommendation": 2, "NumberOfAnalysts": 22}, {"Recommendation": 3, "NumberOfAnalysts": 2}, {"Recommendation": 4, "NumberOfAnalysts": 0}, {"Recommendation": 5, "NumberOfAnalysts": 0}]}, {"age": "ThirtyDaysAgo", "numberOfAnalysts": 34, "distributionList": [{"Recommendation": 1, "NumberOfAnalysts": 10}, {"Recommendation": 2, "NumberOfAnalysts": 22}, {"Recommendation": 3, "NumberOfAnalysts": 1}, {"Recommendation": 4, "NumberOfAnalysts": 0}, {"Recommendation": 5, "NumberOfAnalysts": 1}]}, {"age": "SixtyDaysAgo", "numberOfAnalysts": 33, "distributionList": [{"Recommendation": 1, "NumberOfAnalysts": 10}, {"Recommendation": 2, "NumberOfAnalysts": 22}, {"Recommendation": 3, "NumberOfAnalysts": 1}, {"Recommendation": 4, "NumberOfAnalysts": 0}, {"Recommendation": 5, "NumberOfAnalysts": 0}]}, {"age": "NinetyDaysAgo", "numberOfAnalysts": 31, "distributionList": [{"Recommendation": 1, "NumberOfAnalysts": 10}, {"Recommendation": 2, "NumberOfAnalysts": 20}, {"Recommendation": 3, "NumberOfAnalysts": 1}, {"Recommendation": 4, "NumberOfAnalysts": 0}, {"Recommendation": 5, "NumberOfAnalysts": 0}]}], "priceTarget": {"low": "150.61", "current": "277.40", "high": "313.40", "mean": "265.88"}, "measures": [{"attr": "eps", "title": "EPS Estimate", "value": "6.2008", "numberOfAnalysts": 36}, {"attr": "cps", "title": "Cashflow Estimate", "value": "10.1677", "numberOfAnalysts": 9}]}
# test_str = json.dumps(test)
# if "rating" in test_str:
#     print(2)

test = "{'url': 'https://securitiesapi.stocks666.com/api/securities/stock/913256409/recommendation', 'body': ''}"

print(eval(test))