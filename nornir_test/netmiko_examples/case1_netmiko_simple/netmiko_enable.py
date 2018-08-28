from nornir.core import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result


def netmiko_test(task):
    net_connect = task.host.get_connection("netmiko")
    net_connect.enable()
    task.run(
        netmiko_send_command,
        command_string="show ip int brief",
        use_textfsm=True,
    )


def main():
    brg = InitNornir(config_file="./nornir.yml")
    result = brg.run(
        netmiko_test,
    )
    print_result(result)


if __name__ == "__main__":
    main()
