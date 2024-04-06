# Arch Linux package for The Lounge

This is a clone of the repository [already available](https://aur.archlinux.org/packages/thelounge/) on the [AUR](https://wiki.archlinux.org/index.php/Arch_User_Repository).

This repository is to be used to track Arch Linux's specific issues with this package and allow users to contribute to it.

## Installation

Please follow the usual Arch Linux documentation to install this package from the AUR either manually or using your favorite AUR helper. These instructions are only provided as a quick example, but as typical with Arch Linux you are strongly encouraged to read the approprite documentation.

### Manually
```
$ git clone https://github.com/thelounge/thelounge-archlinux.git
$ cd arch-lounge
$ # optional: select your release (experimental, master, stable)
$ git checkout stable
$ makepkg
# pacman -U thelounge-*.pkg.*
```

### With an AUR helper
with pacaur:
```
$ pacaur -aS thelounge
```

or with yaourt:
```
$ yaourt -aS thelounge
```

### Configuration
The default system-wide documentation file is located at `/etc/thelounge/config.js`. Please note that user profiles and their IRC passwords are also stored there (moving to `/var/lib/thelounge` is planned but not yet done), so the directory is only readable by the `thelounge` user.

### Running
The Lounge provides both a system-wide and per-user systemd unit.

#### System
Simply enable the `thelounge.service` unit, and your server should be up and running:

```
# systemctl enable --now thelounge.service
```

#### User
If you do not want to run the software system-wide, or host multiple users that wish to host their own instance of The Lounge, it can also be launched per user:

```
$ systemctl --user enable --now thelounge.service
```

Please note that for The Lounge to start on boot in this scenario, you will also require to have [lingering](https://wiki.archlinux.org/index.php/Systemd/User#Automatic_start-up_of_systemd_user_instances) enabled for this user:

```
# loginctl enable-linger $username
```

