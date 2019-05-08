import requests

def get_weather(code):
    url = 'http://www.weather.com.cn/data/sk/%s.html' % code
    r = requests.get(url)
    r.encoding = 'utf8'
    data = r.json()
    # print(data)
    inner = data['weatherinfo']
    output = 'city:%s, wind：%s, temp:%s' % (inner['city'], inner['WD'], inner['temp'])
    return output

if __name__ == '__main__':
    code  = 101121301
    result = get_weather(code)
    print(result)
