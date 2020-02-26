import aiohttp, asyncio, json, time

gevent_counts = asyncio.Semaphore(5)
url = 'https://www3.wipo.int/branddb/jsp/select.jsp'
headers = {
    'Host': 'www3.wipo.int',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://www3.wipo.int/branddb/en/',
    'X-Requested-With': 'XMLHttpRequest'
}


async def get_result(qz):
    '''
    :param qz: type list,example -> [ {"q": "a","qz": "N4cgDiBcAEoM4FMCGAnAxgCyrEcCO2A2qAC4LYhIgA00IAZgJYUBCASgIIByAIiAL4Bdfv1q5soACaM4FegBsA9gHcBYkgE8w5GCABGKJADtJNOvKq6ERsyDzNdABgC0LEgGkA8svcmAbgDsANRgALIAtgDiAOZcAIyeAB6JJAD0QZEBAFaSAQDq0X6hAMpgAJKO7AEAzI4AmgC8tngArght2HFiAPoUcY5x1XECQAA="}]
    :return: result
    '''
    async with gevent_counts:
        async with aiohttp.ClientSession() as sess:
            async with sess.request('POST', url, headers=headers, data=qz) as res:
                resp = await res.json(content_type='text/html', encoding='utf-8')
                msg = await resp.get('message')
                if msg:
                    await asyncio.sleep(50)
                else:
                    await print(msg)
                    '''
                    :return 相关处理
                    '''


if __name__ == '__main__':
    query_words = [
        {
            "qz": "N4cgDiBcAEoM4FMCGAnAxgCyrEcCO2A2qAC4LYhIgA00IAZgJYUBCASgIIByAIiAL4Bdfv1q5soACaM4FegBsA9gHcBYkgE8w5GCABGKJADtJNOvKq6ERsyDzNdABgC0LEgGkA8svcmAbgDsANRgALIAtgDiAOZcAIyeAB6JJAD0QZEBAFaSAQDq0X6hAMpgAJKO7AEAzI4AmgC8tngArght2HFiAPoUcY5x1XECQAA="
        },
        {
            "qz": "N4cgDiBcAEoM4FMCGAnAxgCyrEcCO2A2qAC4LYgBGIANNCAGYCWFAQgEoCCAcgCIgBfALoCBdXNlAATJnAoMANgHsA7oPEkAnmHIwqKJADsptegqQUEh0yDws9ABgC0rEgGkA8irfGAbgHYAajAAWQBbAHEAc24ARg8ADwSSAHpAiP8AKyl/AHUo3xCAZTAASQcOfwBmBwBNAF4bPABXBFbsWPEAfQpYh1iq2MEgAAA="
        }
    ]
    loop = asyncio.get_event_loop()
    tasks = [get_result(qz) for qz in query_words]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
