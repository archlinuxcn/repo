# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgname=rime-wanxiang-dict-cn-nightly
_pkgbase=${pkgname%-nightly}
_schema_version=6.9
pkgver=6.9+r20250530.113742
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
        '11ed0ccb714e789ace8ae9d266799e3653837926c5c06d3d608b0798904ff10c9163056d9538d3add6e9818fd1582eaadb533a380ccae1a0b09849b6df8e7e1e')
provides=("${_pkgbase}=${_schema_version}")
replaces=("${_pkgbase}")

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
