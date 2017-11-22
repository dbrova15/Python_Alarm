from pprint import pprint

import requests
import psutil
import os
import time
from settings import DEBAG, API_KEY, NAMBER_TEL, PATH, PROG_N, MESEG


if DEBAG:
    test = 1
else:
    test = 0


def main():
    while True:
        p = list(prog for prog in psutil.process_iter() if prog.name() == PROG_N)

        if p:
            # print("OK")
            if DEBAG:
                break
        else:
            print("BAD")
            try:
                os.startfile(PATH)
            except Exception as e:
                print(e)
                time.sleep(5)
            try:
                response = requests.get("https://sms.ru/sms/send",
                                        params={"api_id": API_KEY, "to": NAMBER_TEL, "msg": MESEG, "json": 1,
                                                "test": test}).text
                print(response)
            except Exception as e:
                print(e)
            try:
                while True:
                    p = list(prog for prog in psutil.process_iter() if prog.name() == PROG_N)
                    if p:
                        print("OK")
                        break
                    else:
                        print("BAD")
                if DEBAG:
                    break
            except Exception as e:
                print(e)
                if DEBAG:
                    break

if __name__ == '__main__':
    print("START")
    main()