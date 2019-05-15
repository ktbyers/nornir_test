from nornir import InitNornir
from nornir.plugins.tasks import commands
from nornir.plugins.functions.text import print_result


def main():
    nr = InitNornir(
        inventory={
            "plugin": "nornir.plugins.inventory.simple.SimpleInventory",
            "options": {"host_file": "hosts.yaml", "group_file": ""},
        },
        core={"raise_on_error": False},
        logging={"file": ""},
    )

    # Execute command that will fail
    result = nr.run(task=commands.command, command="touch /etc/_hosts")
    print_result(result)
    # Confirm host is in failed_hosts
    print(nr.data.failed_hosts)

    # Can reset all failed hosts like this:
    # nr.data.reset_failed_hosts()
    # Or individual hosts like this:
    nr.data.recover_host("localhost")

    # Confirm no more failed hosts
    print(nr.data.failed_hosts)

    # Optionally run task again to confirm that hosts are not in failed state
    # result = nr.run(task=commands.command, command='sudo touch /etc/_hosts')
    # print_result(result)


if __name__ == "__main__":
    main()
