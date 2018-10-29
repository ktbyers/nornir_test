from nornir import InitNornir
from nornir.plugins.tasks.networking import napalm_get

from nornir_test.nornir_utilities import nornir_set_creds, std_print

# Turn off self-signed cert warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def main():
    norn = InitNornir(config_file="./nornir.yml")
    nornir_set_creds(norn)

    result = norn.run(task=napalm_get, getters=["facts"])

    std_print(result)


if __name__ == "__main__":
    main()
