from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_config
from nornir.plugins.functions.text import print_result

from nornir_test.nornir_utilities import nornir_set_creds


def main():

    # Initialize Nornir object using hosts.yaml and groups.yaml
    brg = InitNornir(config_file="./nornir.yml")
    nornir_set_creds(brg)

    result = brg.run(
        netmiko_send_config, num_workers=60, config_commands=["logging buffered 20000"]
    )

    print_result(result)


if __name__ == "__main__":
    main()
