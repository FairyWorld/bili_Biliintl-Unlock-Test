# -*- coding: utf-8 -*-
# @Time： 2023/2/18 22:07 
# @FileName: main.py
# @Software： PyCharm
# @GitHub: KimmyXYC
import requests

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"


def get_requests(season_id):
    url = f"https://api.bilibili.tv/intl/gateway/v2/ogv/view/app/season"
    headers = {'User-Agent': USER_AGENT}
    params = {'season_id': season_id, 's_locale': "zh_SG", 'mobi_app': "bstar_a", 'build': 1080003}
    response = requests.get(url, headers=headers, params=params)
    json_data = response.json()
    print(json_data)
    if json_data["code"] == 0:
        if json_data["result"]["limit"]:
            return False
        else:
            return True
    else:
        return False


def main():
    link_click = get_requests("1006275")
    if link_click:
        spy_family = get_requests("1048837")
        if spy_family:
            spy_family_th = get_requests("1057120")
            spy_family_vn = get_requests("1057175")
            spy_family_id = get_requests("1057318")
            if spy_family_th:
                print("Yes: TH")
            elif spy_family_vn:
                print("Yes: VN")
            elif spy_family_id:
                print("Yes: ID")
            else:
                print("Yes: SEA")
        else:
            print("Chinese Animation Only")
    else:
        print("No")


if __name__ == '__main__':
    main()
