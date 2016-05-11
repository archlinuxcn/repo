# linux-surfacepro3
Arch Linux package to compile the Linux kernel with patches designed to improve user experience on the Surface Pro 3.

This is based on the offical Linux kernel package provided by Arch Linux at: https://projects.archlinux.org/svntogit/packages.git/tree/trunk?h=packages/linux .

This AUR package adds the following patches to the official Linux kernel package:
 - Camera patch from https://github.com/nuclearsandwich/surface3-archlinux/issues/12 (patch from `colorprint`)
 - Multitouch patches from https://raw.githubusercontent.com/shvr/fedora-surface-pro-3-kernel/master/Add-multitouch-support-for-Microsoft-Type-Cover-3.patch .

Most of the functionality required for the Surface Pro 3 has now been mainlined, so hopefully this package will no longer be required within the next few kernel releases.

## Building

You will need to have imported gpg keys for the Linux kernel maintainers:

For Linus Torvalds (the major release key):

	gpg --recv-keys 79BE3E4300411886

For Greg Kroah-Hartman's key (the stable patch release key):

	gpg --recv-keys 38DBBDC86092693E

Then, to build the package, simply run (as usual):

	makepkg
