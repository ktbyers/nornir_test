import sys

from nornir.core import InitNornir
from nornir.plugins.tasks.networking import netmiko_file_transfer
from nornir.plugins.tasks.networking import netmiko_send_command

from nornir_test.nornir_utilities import nornir_set_creds, std_print


def os_upgrade(task):
    file_name = task.host.get("img")
    task.run(
        task=netmiko_file_transfer,
        source_file=file_name,
        dest_file=file_name,
        direction="put",
    )
    return ""


def continue_func(msg="Do you want to continue (y/n)? "):
    response = input(msg).lower()
    if "y" in response:
        return True
    else:
        sys.exit()


def main():

    # Initialize Nornir object using hosts.yaml and groups.yaml
    norn = InitNornir(config_file="nornir.yml")
    nornir_set_creds(norn)

    print("Transferring files")
    result = norn.run(task=os_upgrade, num_workers=20)
    std_print(result)

    # Filter to only a single device
    norn_ios = norn.filter(hostname="cisco1.twb-tech.com")

    # Verify the boot variable
    result = norn_ios.run(
        netmiko_send_command, command_string="show run | section boot", num_workers=20
    )
    std_print(result)
    continue_func()

    # Save the config
    result = norn_ios.run(
        netmiko_send_command, command_string="write mem", num_workers=20
    )
    std_print(result)

    # Reload
    continue_func(msg="Do you want to reload the device (y/n)? ")
    result = norn_ios.run(
        netmiko_send_command, use_timing=True, command_string="reload", num_workers=1
    )

    # Confirm the reload (if 'confirm' is in the output)
    for device_name, multi_result in result.items():
        if "confirm" in multi_result[0].result:
            result = norn_ios.run(
                netmiko_send_command, use_timing=True, command_string="y"
            )

    print("Devices reloaded")


if __name__ == "__main__":
    main()
