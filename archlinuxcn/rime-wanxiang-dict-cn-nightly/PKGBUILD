# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgname=rime-wanxiang-dict-cn-nightly
_pkgbase=${pkgname%-nightly}
_schema_version=8.1.3
pkgver=8.1.3+r20250621.000025
pkgrel=1
epoch=1
pkgdesc="万象中文词库"
arch=(any)
license=('CC-BY-4.0')
url="https://github.com/amzxyz/rime_wanxiang"
_dict_url="${url}/releases/download/dict-nightly/9-base-zh-dicts.zip"
source=("schema-${_schema_version}.zip::${url}/releases/download/v${_schema_version}/rime-wanxiang-base.zip"
        "${_dict_url}")
b2sums=('SKIP'
        'fbbb696e1bbdcc5a5f2740d44cf956feddd7b8889bc3c45d8b41dedb69bca98748c0f90cc9cb61902c9c62f53a02c4a9120f799c3cdd6582d51f522d3bf79a3f')
provides=("${_pkgbase}=${_schema_version}")
replaces=("${_pkgbase}")

makedepends=(curl rsync librime rime-prelude rime-essay)

pkgver() {
    _last_modified=$(curl -ILs -o /dev/null -w '%header{last-modified}' ${_dict_url})
    _dict_version=$(TZ="Asia/Shanghai" date -d "${_last_modified}" +%Y%m%d.%H%M%S)

    printf "%s+r%s" "${_schema_version}" "${_dict_version}"
}

_schema_folder_name="万象拼音标准版"
build() {
    cd "${srcdir}"

    for _f in $(pacman -Qql rime-prelude rime-essay | grep -v "/$"); do ln -sf "${_f}" .; done

    rime_deployer --compile wanxiang.schema.yaml

    find . -type l -delete
}

package() {
    cd "${srcdir}"

    find zh_dicts -type f -exec install -Dm664 {} "${pkgdir}"/usr/share/rime-data/{} \;

    install -Dm664 ./build/wanxiang.*.bin -t "${pkgdir}"/usr/share/rime-data/build
}
