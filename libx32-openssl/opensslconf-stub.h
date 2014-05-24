// This is replaced by libx32-openssl.
// Old file is renamed to opensslconf-64.h.

#if !defined __x86_64__
# include "opensslconf-64.h" // lib32-openssl did not deliver opensslconf-32.h yet
#endif
#if defined __x86_64__ && defined __LP64__
# include "opensslconf-64.h"
#endif
#if defined __x86_64__ && defined __ILP32__
# include "opensslconf-x32.h"
#endif

