# code-server-aur

Arch User Repository package for [code-server](https://github.com/cdr/code-server).
Feel free to file issues here or comment on the AUR page.

Previously maintained by [KSXGitHub](https://github.com/KSXGitHub)

## Updating

Make sure you run these commands on an Arch machine. If you're a Coder employee, we suggest using your dogfooding environment.

1. Run `sh update.sh` and type in the new version
1. Push changes to GitHub: `git push`
1. Push changes to `aur`: `git push aur`
	- If you don't have this set up, run `git remote add aur ssh://aur@aur.archlinux.org/code-server.git`
	- Run `git push aur`

### SSH Key

In order to publish updates to AUR, you'll need to have an SSH key pair setup.

1. Create a config file file `~/.ssh/config`
```text
Host aur.archlinux.org
	IdentityFile ~/.ssh/aur
	User aur
```
2. Create a new key pair by running: 
```shell
ssh-keygen -f ~/.ssh/aur
```
3. This will create a new public key at `.ssh/aur.pub`. Copy this and add to your AUR account under [My Account](https://aur.archlinux.org/account/yourusername/edit/) > SSH Public Key
4. You may also need to be added by the package maintainer (@coadler)

Read more: https://wiki.archlinux.org/index.php/AUR_submission_guidelines

### New Maintainers

If a new maintainer joins the project, please add them to the top of `PKGBUILD`.

### Removing Old Maintainers

Instead of removing them completely, change their title from "Maintainer" to "Contributor".
