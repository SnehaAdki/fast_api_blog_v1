import time
import requests


def main():
    request_count = 10
    url = "https://httpbin.org/get"
    session = requests.Session()
    for i in range(0,request_count):
        print(f"making request {i}")
        res = session.get(url)
        if res.status_code ==200:
            pass

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Total time taken" , end-start)

