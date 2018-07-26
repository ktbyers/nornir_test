from nornir.core import InitNornir
from nornir.plugins.tasks.networking import napalm_get

from pprint import pprint

# Turn off self-signed cert warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def std_print(agg_result):
    print()
    for k, multi_result in agg_result.items():
        print('-' * 50)
        print(k)
        for result_obj in multi_result:
            pprint(result_obj.result)
        print('-' * 50)
        print()
    print()


def main():
    brg = InitNornir(config_file="./nornir.yml")
    result = brg.run(
        task=napalm_get,
        getters=["facts"],
    )

    std_print(result)


if __name__ == "__main__":
    main()
