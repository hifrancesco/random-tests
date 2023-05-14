### Generate and Add SSH Keys and Test Connection

---

```bash
sh-keygen -t ed25519 -C "email@outlook.com"
```

<details>
    <summary><b>sh-keygen -t ed25519 -C "email@outlook.com"</b></summary>

This command is used to generate a new SSH key pair using the Ed25519 algorithm, with an optional comment. The generated key pair consists of a public and private key.

Here's what each part of the command does:

- `ssh-keygen`: This is the command to generate a new SSH key pair.
- `-t ed25519`: This option specifies the type of key to generate, in this case, the Ed25519 algorithm.
- `-C` "email@outlook.com": This option adds a comment to the key, which can be helpful for identifying the key later. Replace "email@outlook.com" with your actual email address.

When you run this command, the ssh-keygen utility will prompt you to enter a file name to save the key pair under. The default file name is id_ed25519, which will be saved in the .ssh directory in your home directory. If you want to save the key pair with a different file name or in a different location, you can specify that with the -f option followed by the file name and path.

After generating the key pair, you can add the public key to the authorized_keys file on the remote server to enable passwordless SSH authentication. To do this, copy the contents of the id_ed25519.pub file to the authorized_keys file on the server. The private key (id_ed25519) should be kept secure on your local machine and not shared with anyone else.

</details>

---

```bash
eval "$(ssh-agent -s)"
```

<details>
    <summary><b>eval "$(ssh-agent -s)"</b></summary>

This command is used to start the SSH agent in the current shell session. The SSH agent is a program that manages SSH keys and allows for passwordless authentication when connecting to remote servers via SSH.

Here's what each part of the command does:

- `ssh-agent`: This is the command to start the SSH agent program.
- `-s`: This option tells the SSH agent to output the necessary shell commands to set the appropriate environment variables.

The eval command is used to execute the output of the ssh-agent -s command in the current shell session. This will set the appropriate environment variables that allow the SSH agent to function correctly.

After running this command, you can use the ssh-add command to add your SSH key to the agent. This allows you to authenticate with remote servers using your SSH key without having to enter your passphrase each time.

Replace id_ed25519 with the file name of your private key if it's named differently. This will add your private key to the SSH agent so that it can be used for authentication.

Note that if you have a passphrase set for your SSH key, you will be prompted to enter it the first time you use it after adding it to the SSH agent.

</details>

---

```bash
touch ~/.ssh/config
```

<details>
    <summary><b>touch ~/.ssh/config</b></summary>

The touch ~/.ssh/config command creates a new empty configuration file for the SSH client on your local machine. This file is located in the .ssh directory in your home directory and is used to specify options for SSH connections.

Here's what each part of the command does:

- `touch`: This is a command to create a new file with the specified name if it doesn't already exist, or to update the modification time if the file already exists.
- `~/.ssh/config`: This is the path and filename of the file to create, which is config in the .ssh directory in your home directory.

After running this command, you can open the ~/.ssh/config file in a text editor to add configuration options for SSH connections. Some examples of options you can set in this file include:

```
Hostname: The hostname or IP address of the remote server you want to connect to.
  User: The username to use when connecting to the remote server.
  Port: The port number to use for the SSH connection.
  IdentityFile: The path and filename of the private key to use for the SSH connection.
```

</details>

---

```bash
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

<details>
    <summary><b>Host github.com</b></summary>
This is an example of an SSH config file entry for connecting to the github.com host with the id_ed25519 private key.

Here's what each part of the entry does:

- Host github.com: This line specifies the host that this configuration applies to. In this case, it's the github.com host.
- AddKeysToAgent yes: This line tells SSH to automatically add the private key to the SSH agent when you use the ssh command to connect to the host. This means that you only need to enter the passphrase for the private key once per session, rather than every time you use it.
- UseKeychain yes: This line tells macOS to store the passphrase for the private key in the system keychain. This means that you won't be prompted for the passphrase when you use the key, and it also allows other macOS applications to use the key without prompting you for the passphrase.
- IdentityFile ~/.ssh/id_ed25519: This line specifies the path and filename of the private key file that should be used to authenticate with the host. In this case, it's the id_ed25519 private key in the .ssh directory in your home directory.

When you have an SSH config file with this entry and you run the ssh command to connect to github.com, SSH will automatically add the private key to the SSH agent and use it to authenticate with the host. This makes it much easier to connect to the host and use Git and other tools to interact with your repositories on GitHub.

</details>

---

```bash
open ~/.ssh/config
```

<details>
    <summary><b>open ~/.ssh/config</b></summary>

- `open`: This is the command to open a file or directory using the default application on macOS.
- `~/.ssh/config`: This is the path and filename of the file to open, which is config in the .ssh directory in your home directory.

</details>

---

```bash
ssh-add -K ~/.ssh/id_ed25519
```

<details>
    <summary><b>ssh-add -K ~/.ssh/id_ed25519</b></summary>

The ssh-add -K ~/.ssh/id_ed25519 command adds your private SSH key to the SSH agent on a macOS system, and the -K option instructs the agent to store the passphrase for the key in the keychain.

Here's what each part of the command does:

- `ssh-add`: This is the command to add your SSH key to the SSH agent.
- `-K`: This option instructs the agent to store the passphrase for the key in the keychain. This means that you will only have to enter the passphrase once per session, rather than every time you use the key.
- `~/.ssh/id_ed25519`: This is the path and filename of the private key file you want to add to the agent. Replace id_ed25519 with the filename of your private key if it's named differently.

After running this command, you will be prompted to enter the passphrase for your private key. Once you've entered it, the key will be added to the SSH agent and you can use it to authenticate with remote servers without having to enter your passphrase each time.

Note that if you do not specify the -K option, the passphrase for the key will not be stored in the keychain and you will be prompted to enter it each time you use the key.


</details>

---

```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

<details>
    <summary><b>pbcopy < ~/.ssh/id_ed25519.pub</b></summary>

The pbcopy < ~/.ssh/id_ed25519.pub command copies the contents of your SSH public key file (id_ed25519.pub) to the system clipboard on a macOS system.

Here's what each part of the command does:

- `pbcopy`: This is the command to copy the contents of a file or text to the system clipboard on macOS.
- `<`: This is a shell redirection operator that tells the pbcopy command to take its input from a file instead of from standard input.

</details>

---

```bash
ssh -T git@github.com
```

<details>
    <summary><b>ssh -T git@github.com</b></summary>

The ssh -T git@github.com command tests your SSH connection to GitHub and verifies that you are authenticated with your GitHub account.

Here's what each part of the command does:

- `ssh`: This is the command to establish an SSH connection to a remote server.
- `-T`: This option tells SSH not to allocate a pseudo-terminal on the remote server, but to just test the connection and exit.
- `git@github.com`: This is the username and hostname of the remote server you want to connect to. In this case, you're connecting to the GitHub server using the git user account.

</details>

---

### References

1. [Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

2. [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

3. [Testing your SSH connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)