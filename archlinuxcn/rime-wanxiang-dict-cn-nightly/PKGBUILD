# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgname=rime-wanxiang-dict-cn-nightly
_pkgbase=${pkgname%-nightly}
_schema_version=6.8.9
pkgver=6.8.9+r20250530.135537
pkgrel=1
epoch=1
pkgdesc="万象中文词库"
arch=(any)
license=('CC-BY-4.0')
url="https://github.com/amzxyz/rime_wanxiang"
_dict_url="${url}/releases/download/dict-nightly/cn_dicts.zip"
source=("${url}/releases/download/dict-nightly/cn_dicts.zip"
        "${url}/archive/refs/tags/v${_schema_version}.tar.gz")
b2sums=('SKIP'
        'ba64857a484028b505c845cca9512a385edc3e8c0838aaa8a1081c635ace4d99810e06399406e8c14b2369667e0ecf804491f1b8645680e96eba59f3543e31b3')
provides=("${_pkgbase}=${_schema_version}")

makedepends=(curl rsync librime rime-prelude rime-essay)

pkgver() {
    _last_modified=$(curl -ILs -o /dev/null -w '%header{last-modified}' ${_dict_url})
    _dict_version=$(date -d "${_last_modified}" +%Y%m%d.%H%M%S)
    
    printf "%s+r%s" "${_schema_version}" "${_dict_version}"
}

build() {
    cd "${srcdir}/rime_wanxiang-${_schema_version}"

    rsync -a --existing --update "${srcdir}/cn_dicts/" cn_dicts

    for _f in $(pacman -Qql rime-prelude rime-essay | grep -v "/$"); do ln -sf "${_f}" .; done

    rime_deployer --compile wanxiang.schema.yaml

    find . -type l -delete
}

package() {
    cd "${srcdir}/rime_wanxiang-${_schema_version}"

    find cn_dicts -type f -exec install -Dm664 {} "${pkgdir}"/usr/share/rime-data/{} \;

    install -Dm664 ./build/wanxiang.*.bin -t "${pkgdir}"/usr/share/rime-data/build
}
