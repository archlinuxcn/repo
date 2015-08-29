# Maintainer: Gavin Costello <gavcos at gmail dot com>
# Contributor:
pkgname=underscorejs
_script=underscore
pkgver=1.8.3
pkgrel=2
pkgdesc="Underscore is a utility-belt library for JavaScript that provides a lot of the functional programming support that you would expect in Prototype.js (or Ruby), but without extending any of the built-in JavaScript objects."
arch=(any)
url=http://underscorejs.org
license=('MIT')
source=("${url}/${_script}.js" "${url}/${_script}-min.js")
md5sums=('f893e294cde60c2462cb19b35aac431b'
  '543feb1ecaf06ea516f8cec5f9f3f279')

package() {
  cd "${srcdir}"
  mkdir -p "${pkgdir}/usr/share/${pkgname}"
  install -Dm644 "${_script}-min.js" "${pkgdir}/usr/share/${pkgname}/${_script}-min.js"
  install -Dm644 "${_script}.js" "${pkgdir}/usr/share/${pkgname}/${_script}.js"
}

# vim:set ts=2 sw=2 et:
