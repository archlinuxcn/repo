# Maintainer: Petrus <petrus@null.local>

pkgname=oama-bin
_pkgname="${pkgname%-bin}"
pkgver=0.22.0
pkgrel=2
pkgdesc="Provide OAuth2 renewal and authorization capabilities"
arch=(x86_64 aarch64)
url="https://github.com/pdobsan/${_pkgname}"
license=('BSD-3-Clause')
groups=()
depends=('gpgme' 'libsecret' 'libgirepository')
makedepends=()
optdepends=(
            'gnome-keyring: Stores passwords and encryption keys'
            'kwallet: Secure and unified container for user passwords'
            'keepassxc: Cross-platform community-driven port of Keepass password manager'
            'gnupg: OpenPGP encryption and signing tool'
            'mutt: Small but very powerful text-based mail client'
            'neomutt: A version of mutt with added features'
            'msmtp: an SMTP client'
            'fdm: fetch and deliver mail'
            'offlineimap: Synchronizes emails between two repositories'
            'isync: IMAP and MailDir mailbox synchronizer'
           )
provides=(${_pkgname})
conflicts=(mailctl-bin ${_pkgname} ${_pkgname}-git )
replaces=(mailctl-bin)
release=$_pkgname-$pkgver-Linux

source_x86_64=(https://github.com/pdobsan/oama/releases/download/${pkgver}/$release-x86_64.tar.gz)
source_aarch64=(https://github.com/pdobsan/oama/releases/download/${pkgver}/$release-aarch64.tar.gz)
sha256sums_x86_64=('63596bb58471448aa3c63a35e17aa4e4c086c35730d98bcca230fec18779a620')
sha256sums_aarch64=('3d38f4be1b02c7dcca518a39f055c5ef896127baa3797e60305cff1c8269537a')

install=.INSTALL

package() {
  cd $release-$CARCH
  install -Dm755 ${_pkgname} ${pkgdir}/usr/bin/${_pkgname}

  install -Dm644 LICENSE ${pkgdir}/usr/share/${_pkgname}/LICENSE
  install -Dm644 README.md ${pkgdir}/usr/share/${_pkgname}
  # install -Dm644 Build-info.txt ${pkgdir}/usr/share/${_pkgname}
  # install -Dm644 cabal.project.freeze ${pkgdir}/usr/share/${_pkgname}
  cp -r configs ${pkgdir}/usr/share/${_pkgname}

  install -Dm644 completions/${_pkgname}.bash ${pkgdir}/usr/share/bash-completion/completions/${_pkgname}.bash
  install -Dm644 completions/${_pkgname}.fish ${pkgdir}/usr/share/fish/vendor_completions.d/${_pkgname}.fish
  install -Dm644 completions/${_pkgname}.zsh ${pkgdir}/usr/share/zsh/site-functions/_${_pkgname}
}
