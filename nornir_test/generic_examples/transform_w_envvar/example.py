from nornir import InitNornir


# export NORNIR_INVENTORY_TRANSFORM_FUNCTION_OPTIONS='{"password": "carl"}'


def prompt_for_password(host, password):
    host.password = password


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
