# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang
pkgname=(rime-wanxiang-base)
pkgver=7.1.2
pkgrel=1
pkgdesc="万象拼音：带声调的拼音词库，万象拼音系列方案基础版，可扩展全拼、双拼、中英混输、语言模型"
arch=(any)
license=('CC-BY-4.0')

url="https://github.com/amzxyz/rime_wanxiang"
source=("${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('959c58e246030190ddb5edfe1c23f255c490bc74461f8a561894b28858b74e01')

makedepends=("librime" "rime-prelude" "rime-essay" "sed")

prepare() {
    cd "${srcdir}/rime_wanxiang-${pkgver}"

    # 清理文件
    rm squirrel.yaml weasel.yaml ./*.trime.yaml ./*.md custom_phrase.txt LICENSE
    rm -r .github custom

    mv default.yaml wanxiang_suggestion.yaml
}

build() {
    cd "${srcdir}/rime_wanxiang-${pkgver}"

    rm -rf build/*

    for _f in $(pacman -Qql rime-prelude rime-essay | grep -v "/$"); do ln -sf "${_f}" .; done

    # 预编译除 wanxiang 主方案外的其他依赖方案
    for _s in *.schema.yaml; do
        [[ $_s == wanxiang.schema.yaml ]] && continue
        rime_deployer --compile "${_s}"
    done

    find . -type l -delete
    rm build/*.txt
}

package_rime-wanxiang-base() {
    pkgdesc="万象拼音基础版基础文件"
    depends=(lua librime rime-wanxiang-gram-zh-hans "rime-wanxiang-dict-cn=${pkgver}")
    optdepends=('libnotify: notification support in lua scripts')

    cd "${srcdir}/rime_wanxiang-${pkgver}"

    for _f in *.db *.yaml; do
        [[ $_f == wanxiang.schema.yaml ]] && continue
        [[ $_f == wanxiang_radical.schema.yaml ]] && continue
        [[ $_f == wanxiang_en.schema.yaml ]] && continue

        install -Dm644 "${_f}" -t "${pkgdir}"/usr/share/rime-data
    done

    for _f in build/*; do
        [[ $_f == build/wanxiang.* ]] && continue
        [[ $_f == build/wanxiang_radical.schema.yaml ]] && continue
        [[ $_f == build/wanxiang_en.schema.yaml ]] && continue

        install -Dm644 "${_f}" -t "${pkgdir}"/usr/share/rime-data/build
    done

    for _d in en_dicts jm_dicts lua opencc; do
        find $_d -type f -exec install -Dm664 {} "${pkgdir}"/usr/share/rime-data/{} \;
    done
}

_schemas=('pinyin  全拼'
          'zrm     自然码'
          # 'zrlong  自然龙'
          # 'abc     智能ABC'
          'flypy   小鹤双拼'
          'sogou   搜狗双拼'
          # 'ziguang 紫光双拼'
          'mspy    微软双拼')

_conflicts=()
for _line in "${_schemas[@]}"; do
    _schema=${_line%% *}
    _conflicts+=("${pkgbase}-${_schema,,}")
done

for _line in "${_schemas[@]}"; do
    _schema=${_line%% *}
    _pkgname=${pkgbase}-${_schema,,}

    _pkgconflicts=()
    for _c in "${_conflicts[@]}"; do
        [[ $_c != "$_pkgname" ]] && _pkgconflicts+=("${_c}")
    done

    pkgname+=("${_pkgname}")
    _name=${_line##* }
    eval "package_$_pkgname() {
        depends=('rime-wanxiang-base')
        pkgdesc='万象拼音基础版（${_name}方案）'
        conflicts=(${_pkgconflicts[*]})
        install='post.install'

        _package $_line
    }"
done

_rime_deploy() {
    for _f in $(pacman -Qql rime-prelude rime-essay | grep -v "/$"); do ln -sf "${_f}" .; done

    for _s in "$@"; do rime_deployer --compile "${_s}"; done

    find . -type l -delete
    rm build/*.txt
}

_package() {
    local _schema=$1
    local _name=$2

    cd "${srcdir}/rime_wanxiang-${pkgver}"

    local _cn_en_user_dict=en_dicts/"${_schema}"
    sed -Ei \
        -e "/^set_shuru_schema:/,/^[^[:space:]]/ { s|^(\s+__include:\s*)\S+(\s*.*)|\1${_name}\2| }" \
        -e "/^set_cn_en:/,/^[^[:space:]]/ { s|^(\s+user_dict:\s*)\S+(\s*.*)|\1${_cn_en_user_dict}\2| }" \
        "wanxiang.schema.yaml"

    for _s in wanxiang_{radical,en}.schema.yaml; do
        sed -Ei \
            -e "/^set_shuru_schema:/,/^[^[:space:]]/ { s|^(\s+__include:\s*)\S+(\s*.*)|\1${_name}\2| }" \
            "${_s}"
    done

    _rime_deploy {wanxiang,wanxiang_radical,wanxiang_en}.schema.yaml

    for _f in {wanxiang,wanxiang_radical,wanxiang_en}.schema.yaml; do
        install -Dm664 "${_f}"       -t "${pkgdir}"/usr/share/rime-data
        install -Dm664 "build/${_f}" -t "${pkgdir}"/usr/share/rime-data/build
    done
}
