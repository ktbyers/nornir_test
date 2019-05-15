import getpass
from nornir import InitNornir


# Will prompt for a password PER host
# Could add logic to only prompt if password doesnt exist
# Or obviously whatever logic you want in here
def prompt_for_password(host):
    host.password = getpass.getpass()


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
