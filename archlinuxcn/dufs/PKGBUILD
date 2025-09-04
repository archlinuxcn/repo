# Maintainer: Puqns67 <me@puqns67.icu>

pkgname='dufs'
pkgver=0.45.0
pkgrel=1
pkgdesc='A distinctive utility file server that supports static serving, uploading, searching, accessing control, webdav...'
arch=('x86_64')
url='https://github.com/sigoden/dufs'
license=('MIT OR Apache-2.0')
depends=('bzip2' 'gcc-libs' 'glibc' 'xz')
makedepends=('cargo')
backup=("etc/${pkgname}/config.yaml")
options=('!lto')

source=("${pkgname}-${pkgver}.tar.gz"::"${url}/archive/refs/tags/v${pkgver}.tar.gz"
        "${pkgname}.service"
        "${pkgname}@.service"
        "${pkgname}-sysusers.conf"
        "${pkgname}-tmpfiles.conf"
        "${pkgname}-config.yaml")

b2sums=('5f7c2e4d0a8b67c8d611acfe5964957abf669924d8a3f67c2991cacded4b9dc521788f8ee43a30e7411a26f2705c9164b868cc7566b703ff5299a5e49f763e60'
        '5929a74b6898709884df766c94e6a0c30d18e632aece2a36d57bc41f05c5a8d23da036a6a0773fb7c13df7f149c001abfaab647a09593b84e85cb13026eb11a2'
        '004aaa2c669860830ee63ad413b4eec224863f30a2087fa1ea9079ab517576ad95609e6daddfeab7a2c2821290f081545d03ad31e5b27cb4e9e6cc37c9040284'
        '4a647e5365e8e4d101470960cd72317b29dae68cff2331031aeccfc8bf860e72662febbda6673ddde09944555847a3b4598b3f3389fc6e67bccf9d08ab8cca4e'
        '8eb56d81a056e9c177f84dc72485d6f4dfd29e8687229d12873b68d305f81cc3cf065dcbf69ff3f66bf87d399618f155facabfc0547c49f181d07f6ee6eb6d06'
        '1e52a77fd3cb1a8734a73b70e680cfccf6648174e8fbced30e4494b78b155a36923d28e29a301fc3b480838dd4c7ad0944bb078af59541cafac2a6a98fd09b47')

prepare() {
  export RUSTUP_TOOLCHAIN=stable

  cd "${srcdir}/${pkgname}-${pkgver}"

  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target

  cd "${srcdir}/${pkgname}-${pkgver}"

  cargo build --frozen --release --all-features

  mkdir -p "${srcdir}/completions"
  "target/release/${pkgname}" --completions bash > "${srcdir}/completions/${pkgname}"
  "target/release/${pkgname}" --completions fish > "${srcdir}/completions/${pkgname}.fish"
  "target/release/${pkgname}" --completions zsh > "${srcdir}/completions/_${pkgname}"
}

package() {
  install -Dm755 "${srcdir}/${pkgname}-${pkgver}/target/release/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"

  install -Dm644 "${srcdir}/${pkgname}.service" "${pkgdir}/usr/lib/systemd/system/${pkgname}.service"
  install -Dm644 "${srcdir}/${pkgname}@.service" "${pkgdir}/usr/lib/systemd/system/${pkgname}@.service"
  install -Dm644 "${srcdir}/${pkgname}-sysusers.conf" "${pkgdir}/usr/lib/sysusers.d/${pkgname}.conf"
  install -Dm644 "${srcdir}/${pkgname}-tmpfiles.conf" "${pkgdir}/usr/lib/tmpfiles.d/${pkgname}.conf"
  install -Dm644 "${srcdir}/${pkgname}-config.yaml" "${pkgdir}/etc/${pkgname}/config.yaml"

  install -Dm644 "${srcdir}/completions/${pkgname}" "${pkgdir}/usr/share/bash-completion/completions/${pkgname}"
  install -Dm644 "${srcdir}/completions/${pkgname}.fish" "${pkgdir}/usr/share/fish/vendor_completions.d/${pkgname}.fish"
  install -Dm644 "${srcdir}/completions/_${pkgname}" "${pkgdir}/usr/share/zsh/site-functions/_${pkgname}"

  # license
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/LICENSE-MIT" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
