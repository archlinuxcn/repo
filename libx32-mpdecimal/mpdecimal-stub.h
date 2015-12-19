// This is replaced by libx32-mpdecimal.
// Old file is renamed to mpdecimal-64.h.

#if !defined __x86_64__
# include "mpdecimal-x32.h" // no lib32-mpdecimal yet
#endif
#if defined __x86_64__ && defined __LP64__
# include "mpdecimal-64.h"
#endif
#if defined __x86_64__ && defined __ILP32__
# include "mpdecimal-x32.h"
#endif

