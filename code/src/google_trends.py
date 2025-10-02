import sys
from pytrends.request import TrendReq

def analyze_trends(keyword_list: list[str], timeframe: str, geography: str, timezone: int, category_id: int = 0):
    """
    Fetches Google Trends data for a list of keywords and generates a line chart.

    :param keywords: A list of strings with the keywords to compare.
    :param timeframe: The timeframe to fetch data for (e.g., 'today 3-m', 'now 7-d').
    :param geography: The two-letter country code (e.g., 'IN', 'US').
    :param timezone: Timezone Offset (e.g., US CST is '360', IST is 330;
                     NOTE: US CST is not -360, Google uses timezone this way...)
                     Refer: https://en.wikipedia.org/wiki/UTC_offset
    :param category_id: Category to narrow results, For getting the complete list of categories and their ids
                     refer: https://github.com/pat310/google-trends-api/wiki/Google-Trends-Categories
    """
    print(f"Connecting to Google Trends...")
    pytrends = TrendReq(hl='en-US', tz=timezone)

    print(f"Fetching data for keywords: {keyword_list} in region: {geography} for timeframe: {timeframe}")
    return pytrends.build_payload(
                kw_list=keyword_list,
                cat=category_id,
                timeframe=timeframe,
                geo=geography,
                gprop=''
            )