from nornir import InitNornir
from nornir.plugins.tasks.networking import napalm_get

from nornir_test.nornir_utilities import nornir_set_creds, std_print

# Turn off self-signed cert warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_and_close(task):
    result = task.run(
        task=napalm_get,
        getters=["facts"],
    )
    task.host.close_connection("napalm")
    return result


def main():
    brg = InitNornir(config_file="./nornir.yml")
    nornir_set_creds(brg)
    result = brg.run(
        task=get_and_close,
        num_workers=20,
    )
    std_print(result)


if __name__ == "__main__":
    main()
