# linux-vfio

## What is this?

linux-vfio is the kernel for Arch linux, with the ACS Override and i915 VGA Arbiter patches applied. These patches, originally written by Alex Williamson and updated by Mark Weiman, allow certain motherboards to split PCIe IOMMU groups where it would not otherwise be possible. This is often used to allow a specific PCIe card (often a video card) to be assigned to the `vfio` driver, and attached to a virtual machine.

## Using this repository

This repository is used to track the AUR [linux-vfio](https://aur.archlinux.org/pkgbase/linux-vfio/) package, along with (hopeful) automation thereof. The official AUR repository is still hosted by Arch: https://aur.archlinux.org/cgit/aur.git/log/?h=linux-vfio

## See Also

https://aur.archlinux.org/pkgbase/linux-vfio/

https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF

https://www.kernel.org/doc/Documentation/vfio.txt
