# Maintainer: Puqns67 <me@puqns67.icu>

pkgname='dufs'
pkgver='0.43.0'
pkgrel=2
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

b2sums=('a35eeb62e3aa4404a7ed5d2ffc2db12bb9f039d7e097fd7b9bc9c8b3aff592026b5b7a337da2596aa7ae5f2f73d5933938252c80d09c6b66c8177a7e429fbde6'
        'feb7356eb197aaff9f4715e67110f8487e69eb942f50813cc172eb0465d87058867edc410307f5983ae7bf2ccfebb49c9da5bfc3de2cc880b1197c8d8d0ca260'
        '29ca7c0b0768e339adfe9e20c1a9d9439444319ca420227e5b0e577cf69fd6e80f36eff79ab98ca0d9354aedb9d5503e468fa89251331e9480fd1465bbb8ea51'
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
