// This is replaced by libx32-curl.
// Old file is renamed to curlbuild.h.bak.

#if !defined __x86_64__
# include "curlbuild-32.h"
#endif
#if defined __x86_64__ && defined __LP64__
# include "curlbuild-64.h"
#endif
#if defined __x86_64__ && defined __ILP32__
# include "curlbuild-x32.h"
#endif

