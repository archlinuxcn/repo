# Maintainer: Jianfeng Zhang <swordfeng123@gmail.com> 5A11FEDDF991B901B98FF2C3732AFCA703D1198A
# Maintainer: Sébastien Luttringer
# Contributor: Balwinder S "bsd" Dheeman (bdheeman AT gmail.com)

pkgname=dkms-sorted
pkgver=2.5
pkgrel=2
pkgdesc='Dynamic Kernel Modules System (modified alpm hook to handle dependencies) - experimental'
arch=('any')
url='https://github.com/dell/dkms'
license=('GPL2')
depends=('bash' 'kmod' 'gcc' 'make' 'patch')
makedepends=('git')
optdepends=('linux-headers: build modules against the Arch kernel'
            'linux-lts-headers: build modules against the LTS kernel'
            'linux-zen-headers: build modules against the ZEN kernel'
            'linux-hardened-headers: build modules against the HARDENED kernel')
backup=('etc/dkms/framework.conf')
source=("git+https://github.com/dell/dkms.git#tag=v${pkgver}"
        'dkms-install.hook'
        'dkms-remove.hook'
        'alpm-hook'
        '0001-Revert-Make-newly-installed-modules-available-immedi.patch')
provides=("dkms=${pkgver}")
conflicts=('dkms')
sha256sums=('SKIP'
            '6f2fe43f98cd3e043330e599689d3471108e5022ca7edf69ad645f609ccc33ac'
            'a145a3a8880449a8bc824374b8409750f3cb7c003395fff5a8b9e5ff803c1328'
            '6ca388b4f3a65cc18a737946090ef96d56a832cc0f531bf2adbbc15545ca8cdc'
            '124b821b1b44ba365d915945825bcf32c1077655c3a98eb1644de56b6abfcd09')


prepare() {
  cd dkms

  # apply patch from the source array (should be a pacman feature)
  local filename
  for filename in "${source[@]}"; do
    if [[ "$filename" =~ \.patch$ ]]; then
      msg2 "Applying patch ${filename##*/}"
      patch -p1 -N -i "$srcdir/${filename##*/}"
    fi
  done

  # /usr move
  msg2 '/usr move patching'
  for i in dkms{,_framework.conf,.bash-completion,.8,_common.postinst}; do
    sed -ri 's,/lib/modules,/usr/lib/modules,g' "$i"
  done
}

package() {
  # alpm hook
  install -D -m 644 dkms-install.hook "$pkgdir/usr/share/libalpm/hooks/70-dkms-install.hook"
  install -D -m 644 dkms-remove.hook "$pkgdir/usr/share/libalpm/hooks/70-dkms-remove.hook"
  install -D -m 755 alpm-hook "$pkgdir/usr/lib/dkms/alpm-hook"
  # upstream installer
  cd dkms
  # we don't need kconf files, so we install them outside $pkgdir
  make \
    DESTDIR="$pkgdir" \
    SBIN="$pkgdir/usr/bin" \
    BASHDIR="$pkgdir/usr/share/bash-completion/completions" \
    KCONF="$srcdir"/kconf \
    install
}
