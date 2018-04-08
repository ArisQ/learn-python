#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from xml.parsers.expat import ParserCreate
from urllib import request
import datetime
import urllib


class WeatherSaxHandler(object):
    def __init__(self):
        self.city = ''
        self.forecast = []

    def start_element(self, name, attrs):
        if name == 'yweather:location':
            self.city = attrs['city']
        elif name == 'yweather:forecast':
            forecast = {'date': datetime.datetime.strptime(attrs['date'], '%d %b %Y'),
                        'high': attrs['high'],
                        'low': attrs['low']}
            self.forecast.append(forecast)

    def end_element(self, name):
        pass

    def char_data(self, text):
        pass


def parseXml(xml_str):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    return {
        'city': handler.city,
        'forecast': handler.forecast
    }


# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
try:
    with request.urlopen(URL) as f:
        data = f.read()
except urllib.error.URLError:
    print('Network error, using cache')
    data = rb'''<?xml version="1.0" encoding="UTF-8"?>
<query xmlns:yahoo="http://www.yahooapis.com/v1/base.rng" yahoo:count="1" yahoo:created="2018-04-08T13:50:55Z" yahoo:lang="en-US"><results><channel><yweather:units xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" distance="mi" pressure="in" speed="mph" temperature="F"/><title>Yahoo! Weather - Beijing, Beijing, CN</title><link>http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/</link><description>Yahoo! Weather for Beijing, Beijing, CN</description><language>en-us</language><lastBuildDate>Sun, 08 Apr 2018 09:50 PM CST</lastBuildDate><ttl>60</ttl><yweather:location xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" city="Beijing" country="China" region=" Beijing"/><yweather:wind xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" chill="54" direction="185" speed="14"/><yweather:atmosphere xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" humidity="34" pressure="1006.0" rising="0" visibility="16.1"/><yweather:astronomy xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" sunrise="5:47 am" sunset="6:46 pm"/><image><title>Yahoo! Weather</title><width>142</width><height>18</height><link>http://weather.yahoo.com</link><url>http://l.yimg.com/a/i/brand/purplelogo//uh/us/news-wea.gif</url></image><item><title>Conditions for Beijing, Beijing, CN at 09:00 PM CST</title><geo:lat xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">39.90601</geo:lat><geo:long xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">116.387909</geo:long><link>http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/</link><pubDate>Sun, 08 Apr 2018 09:00 PM CST</pubDate><yweather:condition xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="33" date="Sun, 08 Apr 2018 09:00 PM CST" temp="55" text="Mostly Clear"/><yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="34" date="08 Apr 2018" day="Sun" high="69" low="34" text="Mostly Sunny"/><yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="09 Apr 2018" day="Mon" high="67" low="41" text="Partly Cloudy"/><yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="32" date="10 Apr 2018" day="Tue" high="73" low="50" text="Sunny"/><yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="11 Apr 2018" day="Wed" high="74" low="47" text="Partly Cloudy"/><yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="28" date="12 Apr 2018" day="Thu" high="71" low="53" text="Mostly Cloudy"/><yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="26" date="13 Apr 2018" day="Fri" high="57" low="51" text="Cloudy"/><yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="14 Apr 2018" day="Sat" high="64" low="47" text="Partly Cloudy"/><yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="34" date="15 Apr 2018" day="Sun" high="70" low="50" text="Mostly Sunny"/><yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="32" date="16 Apr 2018" day="Mon" high="75" low="47" text="Sunny"/><yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="34" date="17 Apr 2018" day="Tue" high="75" low="52" text="Mostly Sunny"/><description>&lt;![CDATA[&lt;img src="http://l.yimg.com/a/i/us/we/52/33.gif"/&gt;
&lt;BR /&gt;
&lt;b&gt;Current Conditions:&lt;/b&gt;
&lt;BR /&gt;Mostly Clear
&lt;BR /&gt;
&lt;BR /&gt;
&lt;b&gt;Forecast:&lt;/b&gt;
&lt;BR /&gt; Sun - Mostly Sunny. High: 69Low: 34
&lt;BR /&gt; Mon - Partly Cloudy. High: 67Low: 41
&lt;BR /&gt; Tue - Sunny. High: 73Low: 50
&lt;BR /&gt; Wed - Partly Cloudy. High: 74Low: 47
&lt;BR /&gt; Thu - Mostly Cloudy. High: 71Low: 53
&lt;BR /&gt;
&lt;BR /&gt;
&lt;a href="http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/"&gt;Full Forecast at Yahoo! Weather&lt;/a&gt;
&lt;BR /&gt;
&lt;BR /&gt;
&lt;BR /&gt;
]]&gt;</description><guid isPermaLink="false"/></item></channel></results></query><!-- total: 5 -->
'''
result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'