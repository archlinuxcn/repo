# <p align="center">kernel-modules-hook</p>

Tired of missing modules when updating the kernel?<br/>
Annoyed by `modprobe: FATAL: Module smth not found in directory /lib/modules/new-kernel`?<br/>
Losing uptime after reboots due to kernel update?

*The solution is here.*

* Save.<br/>
![Save](https://i.imgur.com/3YHtBRB.png)<br/>
* Update.<br/>
![Update](https://i.imgur.com/uxySEMY.png)<br/>
* Restore.<br/>
![Restore](https://i.imgur.com/AJeBw0n.png)<br/>
* Enjoy.<br/>
![Enjoy](https://i.imgur.com/WQAYSSR.png)

Do not worry, backups are automatically cleaned.

## Installation
[AUR link](https://aur.archlinux.org/packages/kernel-modules-hook/)
```bash
$ ${your_aur_helper} -S kernel-modules-hook

# Or from git:

$ git clone https://github.com/saber-nyan/kernel-modules-hook.git kmh
$ cd kmh
$ makepkg -sci
$ sudo systemctl daemon-reload
$ sudo systemctl enable linux-modules-cleanup
```
