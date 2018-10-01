from nornir import InitNornir
from nornir.plugins.tasks.networking import napalm_get
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.core.filter import F

from nornir_test.nornir_utilities import nornir_set_creds, std_print

# Turn off self-signed cert warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def main():
    norn = InitNornir(config_file="./nornir.yml")

    f = F(groups__contains="ios")
    napalm_hosts = norn.filter(f)

    result = napalm_hosts.run(
        task=napalm_get,
        getters=["facts"],
    )

    std_print(result)

    netmiko_hosts = norn.filter(F(groups__contains="asa"))
    result = netmiko_hosts.run(
        netmiko_send_command,
        num_workers=60,
        command_string="show ip arp",
        use_textfsm=True,
    )

    std_print(result)


if __name__ == "__main__":
    main()
