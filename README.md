# Automation-Anywhere-Credential-Attribute-Updater
Uses the Automation Anywhere API to update a credential attribute value in Credential Valut.

## How to run
- Update the `credentials.py` file with your own username and password.
- This program is made to be run at the command line. The template to run it is **`python credential_updater.py [base_url] [credential_name] [attribute_name] [new_value]`**
- What each parameter is:
  - **`base_url`**: The URL used to navigate to your Control Panel. For example: `http://control_room_url/`.
  - **`credential_name`**: The name of the credential you want updated. This is the `Name` field in Credential Vault.
  - **`attribute_name`**: The name of the attribute you want updated. This is the `Attribute Name` field in Credential Vault.
  - **`new_value`**: The value you want the attribute updated to. This will update the `Value` field in Credential Vault for the parameter `attribute_name`.
