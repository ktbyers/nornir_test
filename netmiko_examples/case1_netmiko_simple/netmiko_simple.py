from nornir.core import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result


def main():

    # Initialize Nornir object using hosts.yaml and groups.yaml
    brg = InitNornir(config_file="./nornir.yml")
    result = brg.run(
        netmiko_send_command,
        num_workers=60,
        command_string="show ip int brief",
        use_textfsm=True,
    )

    print_result(result)


if __name__ == "__main__":
    main()
