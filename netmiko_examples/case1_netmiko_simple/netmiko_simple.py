from getpass import getpass

from nornir.core import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result


def nornir_set_creds(brg, username=None, password=None):
    """Handler so credentials don't need stored in clear in inventory."""
    if not username:
        username = input("Enter username: ")
    if not password:
        password = getpass()

    for host_obj in brg.inventory.hosts.values():
        # host_obj.username = username
        # host_obj.password = password
        host_obj.data["nornir_username"] = username
        host_obj.data["nornir_password"] = password


def main():

    # Initialize Nornir object using hosts.yaml and groups.yaml
    brg = InitNornir(config_file="./nornir.yml")
    nornir_set_creds(brg)

    result = brg.run(
        netmiko_send_command,
        num_workers=60,
        command_string="show ip int brief",
        use_textfsm=True,
    )

    print_result(result)


if __name__ == "__main__":
    main()
