from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

from nornir_test.nornir_utilities import nornir_set_creds


def main():

    # Initialize Nornir object using hosts.yaml and groups.yaml
    norn = InitNornir(config_file="./nornir.yml")
    nornir_set_creds(norn)

    result = norn.run(
        netmiko_send_command,
        num_workers=1,
        command_string="show ip int brief",
        use_textfsm=True,
    )
    print_result(result)


if __name__ == "__main__":
    main()
