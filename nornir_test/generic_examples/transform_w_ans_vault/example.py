import yaml
from ansible import constants as C
from ansible.parsing.vault import VaultLib
from ansible.cli import CLI
from ansible.parsing.dataloader import DataLoader
from nornir import InitNornir


# vault password = 'password'
loader = DataLoader()
vault_secret = CLI.setup_vault_secrets(
    loader=loader, vault_ids=C.DEFAULT_VAULT_IDENTITY_LIST
)
vault = VaultLib(vault_secret)


# This will prompt for *each* host in the inventory so its somewhat not ideal
# We could also just use vault to set a group or default password in a similar fashion,
# we wouldnt need the transform function for that
def vault_password(host):
    insecure_yaml = vault.decrypt(open("vaulted_pass").read())
    insecure_yaml = yaml.safe_load(insecure_yaml)
    host.password = insecure_yaml["password"]


def main():
    # instantiate nornir object w/ transform function to set password from vault
    nr = InitNornir(
        inventory={
            "plugin": "nornir.plugins.inventory.simple.SimpleInventory",
            "options": {"host_file": "hosts.yaml", "group_file": ""},
            "transform_function": vault_password,
        },
        core={"raise_on_error": False},
        logging={"file": ""},
    )
    # Confirm that host password got updated
    print(nr.inventory.hosts["localhost"].password)


if __name__ == "__main__":
    main()
