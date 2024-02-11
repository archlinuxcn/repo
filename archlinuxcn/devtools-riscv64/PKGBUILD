# Maintainer: Xeonacid <h.dwwwwww at gmail dot com>

pkgname=devtools-riscv64
epoch=1
pkgver=1.1.0+patch1
pkgrel=1
pkgdesc='Tools for Arch Linux RISC-V package maintainers'
arch=('x86_64' 'riscv64')
license=('GPL-3.0-or-later')
url='https://github.com/felixonmars/archriscv-packages'
depends=(devtools)
depends_x86_64=(qemu-user-static)
source=(makepkg-riscv64.patch
        pacman-extra-riscv64.patch
        sogrep-riscv64.patch
        valid-repos-riscv64.sh)
source_x86_64=(z-archriscv-qemu-riscv64.conf)
sha256sums=('9125ba2f479e57d634deea76ee036569dbd3d8a54d81e8d0f5a4e7aef75b9a48'
            '5c80d7f727c4cca6c3ae515dbcb9b9a69d2cae952aa520a82df97cf37432c9cc'
            'c8e9bfc390e42d358007578ca54212bda1d44c754c976be9ef262944d4a0d83c'
            '94ee35597de8e46b1f0c09f95ced34c47ece2f95f92d1a7f2415373f2d129c63')
sha256sums_x86_64=('c59273c423e815e4c27e8486632d80a768adddd172119035d48f7c2fac98a87a')

package() {
  install -Dm644 valid-repos-riscv64.sh -t "$pkgdir"/usr/share/devtools/lib
  patch /usr/bin/sogrep -i sogrep-riscv64.patch -o sogrep-riscv64
  install -Dm755 sogrep-riscv64 -t "$pkgdir"/usr/bin/

  ln -s /usr/bin/archbuild "$pkgdir"/usr/bin/extra-riscv64-build

  patch /usr/share/devtools/makepkg.conf.d/x86_64.conf -i makepkg-riscv64.patch -o riscv64.conf
  install -Dm644 riscv64.conf -t "$pkgdir"/usr/share/devtools/makepkg.conf.d
  patch /usr/share/devtools/pacman.conf.d/extra.conf -i pacman-extra-riscv64.patch -o extra-riscv64.conf
  install -Dm644 extra-riscv64.conf -t "$pkgdir"/usr/share/devtools/pacman.conf.d

  if [[ ! "$CARCH" =~ riscv ]]; then
    install -dm755 "$pkgdir"/usr/share/devtools/setarch-aliases.d
    echo "$CARCH" > "$pkgdir"/usr/share/devtools/setarch-aliases.d/riscv64

    # qemu-user-static-binfmt, but with C flag
    install -Dm644 z-archriscv-qemu-riscv64.conf -t "$pkgdir"/usr/lib/binfmt.d/
  fi
}

# vim: ts=2 sw=2 et:
