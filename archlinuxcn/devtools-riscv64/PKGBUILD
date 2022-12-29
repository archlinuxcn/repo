# Maintainer: Xeonacid <h.dwwwwww at gmail dot com>

pkgname=devtools-riscv64
pkgver=1.2.0
pkgrel=1
pkgdesc='Tools for Arch Linux RISC-V package maintainers'
arch=('x86_64' 'riscv64')
license=('GPL')
url='https://github.com/felixonmars/archriscv-packages'
depends=('devtools')
depends_x86_64=('qemu-user-static')
source=(makepkg-riscv64.conf
        pacman-extra-riscv64.conf
        sogrep-riscv64)
source_x86_64=('z-archriscv-qemu-riscv64.conf')
sha256sums=('c8842d83460d44b873ff56c9ee0c982963ff76e5ed13897e5d7b8d7f0ea7c206'
            'fc933f164d21774e7a1435d9fccf87cb05f7b601e89a2ba54b899b2ce1e809df'
            '3721d7ca08eae58ef2a9de6d8f9ccf2fae1f330949bbf5f566db4c2efbd06105')
sha256sums_x86_64=('c59273c423e815e4c27e8486632d80a768adddd172119035d48f7c2fac98a87a')

package() {
  install -Dm755 sogrep-riscv64 -t "$pkgdir"/usr/bin/
  ln -s /usr/bin/archbuild "$pkgdir"/usr/bin/extra-riscv64-build

  install -Dm644 makepkg-riscv64.conf pacman-extra-riscv64.conf -t "$pkgdir"/usr/share/devtools/

  if [[ ! "$CARCH" =~ riscv ]]; then
    install -dm755 "$pkgdir"/usr/share/devtools/setarch-aliases.d
    echo "$CARCH" > "$pkgdir"/usr/share/devtools/setarch-aliases.d/riscv64

    # binfmt-qemu-static, but with P flag
    install -Dm644 z-archriscv-qemu-riscv64.conf -t "$pkgdir"/usr/lib/binfmt.d/
  fi
}

# vim: ts=2 sw=2 et:
