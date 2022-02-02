# Maintainer: Xeonacid <h.dwwwwww at gmail dot com>

pkgname=devtools-riscv64
pkgver=1.0.0
pkgrel=2
pkgdesc='Tools for Arch Linux RISC-V package maintainers'
arch=('x86_64')
license=('GPL')
url='https://github.com/felixonmars/archriscv-packages'
depends=('devtools' 'qemu-user-static' 'binfmt-qemu-static')
source=(makepkg-riscv64.conf
        pacman-extra-riscv64.conf)
sha256sums=('d0eda35a669f0015c6f6bacf146145c821dffba42de663901da08d2c35a4c148'
            'fc933f164d21774e7a1435d9fccf87cb05f7b601e89a2ba54b899b2ce1e809df')

package() {
  install -dm755 "$pkgdir"/usr/bin
  ln -s /usr/bin/archbuild "$pkgdir"/usr/bin/extra-riscv64-build

  install -Dm644 makepkg-riscv64.conf pacman-extra-riscv64.conf -t "$pkgdir"/usr/share/devtools/

  if [[ ! "$CARCH" =~ riscv ]]; then
    install -dm755 "$pkgdir"/usr/share/devtools/setarch-aliases.d
    echo "$CARCH" > "$pkgdir"/usr/share/devtools/setarch-aliases.d/riscv64
  fi
}

# vim: ts=2 sw=2 et:
