_uuu_autocomplete()
{
     COMPREPLY=($(/usr/bin/uuu $1 $2 $3))
}
complete -o nospace -F _uuu_autocomplete  uuu
