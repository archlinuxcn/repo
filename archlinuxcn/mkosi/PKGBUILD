# Maintainer: Lucas Werkmeister <mail@lucaswerkmeister.de>
# Contributor: Dave Reisner <dreisner@archlinux.org>

pkgname=mkosi
pkgver=4
pkgrel=1
pkgdesc='Build Legacy-Free OS Images'
arch=('any')
url='https://github.com/systemd/mkosi'
license=('LGPL2.1')
depends=('python')
makedepends=('python-setuptools')
optdepends=('dnf: build Fedora or Mageia images'
            'debootstrap: build Debian or Ubuntu images'
            'debian-archive-keyring: build Debian images'
            'ubuntu-keyring: build Ubuntu images'
            'arch-install-scripts: build Arch images'
            'zypper-git: build openSUSE images'
            'gnupg: sign images'
            'xz: compress images with xz'
            'btrfs-progs: raw_btrfs and subvolume output formats'
            'dosfstools: build bootable images'
            'squashfs-tools: raw_squashfs output format'
            'tar: tar output format'
            'cryptsetup: add dm-verity partitions'
            'edk2-ovmf: run bootable images in QEMU'
            'qemu: run bootable images in QEMU'
            'qemu-kvm: run bootable images in QEMU'
            'sbsigntools: sign EFI binaries for UEFI SecureBoot')
source=("https://github.com/systemd/mkosi/archive/v$pkgver.tar.gz")
sha256sums=('855666aa7a16fcc41b0a2e5f12dc1916d19e03c9d174332ef0fd53cb137da8f2')

package() {
  cd "mkosi-$pkgver"
  python setup.py install --root="$pkgdir"
}
