import getpass
from nornir import InitNornir


# Prompt for password
PASSWORD = getpass.getpass()


# Assign user entered password to all hosts
def prompt_for_password(host):
    host.password = PASSWORD


def main():
    nr = InitNornir(
        inventory={
            "plugin": "nornir.plugins.inventory.simple.SimpleInventory",
            "options": {"host_file": "hosts.yaml", "group_file": ""},
            "transform_function": prompt_for_password,
        },
        core={"raise_on_error": False},
        logging={"file": ""},
    )
    # Confirm that host password got updated
    print(nr.inventory.hosts["localhost"].password)


if __name__ == "__main__":
    main()
