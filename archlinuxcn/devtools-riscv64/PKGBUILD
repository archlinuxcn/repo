# Maintainer: Xeonacid <h.dwwwwww at gmail dot com>

pkgname=devtools-riscv64
epoch=1
pkgver=1.0.0+patch1
pkgrel=1
pkgdesc='Tools for Arch Linux RISC-V package maintainers'
arch=('x86_64' 'riscv64')
license=('GPL')
url='https://github.com/felixonmars/archriscv-packages'
depends=(devtools)
depends_x86_64=(qemu-user-static)
source=(makepkg-riscv64.patch
        pacman-extra-riscv64.patch
        sogrep-riscv64)
source_x86_64=(z-archriscv-qemu-riscv64.conf)
sha256sums=('2abae300509c2fbae0246f195fb7ffa17c4ad240052f1e60b0bc504de6149685'
            '5c80d7f727c4cca6c3ae515dbcb9b9a69d2cae952aa520a82df97cf37432c9cc'
            '3721d7ca08eae58ef2a9de6d8f9ccf2fae1f330949bbf5f566db4c2efbd06105')
sha256sums_x86_64=('c59273c423e815e4c27e8486632d80a768adddd172119035d48f7c2fac98a87a')

package() {
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
