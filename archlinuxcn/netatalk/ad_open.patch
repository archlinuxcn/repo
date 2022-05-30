--- libatalk/adouble/ad_open.c.orig	2022-03-22 04:44:25 UTC
+++ libatalk/adouble/ad_open.c
@@ -1574,6 +1574,8 @@ static bool ad_entry_check_size(uint32_t eid,
     uint32_t required_len;
 
 	if (eid >= ADEID_MAX) {
+		LOG(log_error, logtype_ad, "ad_entry_check_size %d is greater than %d",
+        	    eid, ADEID_MAX);
 		return false;
 	}
 	if (got_len == 0) {
@@ -1585,6 +1587,7 @@ static bool ad_entry_check_size(uint32_t eid,
 		 * Shouldn't happen: implicitly initialized to zero because
 		 * explicit initializer missing.
 		 */
+		LOG(log_error, logtype_ad, "ad_entry_check_size explicit initializer missing");
 		return false;
 	}
 	if (ad_checks[eid].expected_len == -1) {
@@ -1594,6 +1597,8 @@ static bool ad_entry_check_size(uint32_t eid,
 	if (ad_checks[eid].fixed_size) {
 		if (ad_checks[eid].expected_len != got_len) {
 			/* Wrong size fo fixed size entry. */
+			LOG(log_error, logtype_ad, "ad_entry_check_size wrong size to fixed size entry (%d != %d)",
+        	    	    ad_checks[eid].expected_len, got_len);
 			return false;
 		}
         required_len = got_len;
@@ -1604,12 +1609,16 @@ static bool ad_entry_check_size(uint32_t eid,
 				 * Too small for variable sized entry with
 				 * minimum size.
 				 */
+				LOG(log_error, logtype_ad, "ad_entry_check_size too small for variable sized entry (%d < %d)",
+        	    	    	    got_len, ad_checks[eid].expected_len);
 				return false;
 			}
         required_len = got_len;
 		} else {
 			if (got_len > ad_checks[eid].expected_len) {
 				/* Too big for variable sized entry. */
+				LOG(log_error, logtype_ad, "ad_entry_check_size too big for variable sized entry (%d > %d)",
+                                    got_len, ad_checks[eid].expected_len);
 				return false;
 			}
             /*
@@ -1621,10 +1630,14 @@ static bool ad_entry_check_size(uint32_t eid,
 	}
 	if (off + required_len < off) {
 		/* wrap around */
+		LOG(log_error, logtype_ad, "ad_entry_check_size wrap around (%d + %d < %d)",
+                    off, required_len, off);
 		return false;
 	}
 	if (off + required_len > bufsize) {
 		/* overflow */
+		LOG(log_error, logtype_ad, "ad_entry_check_size overflow (%d + %d > %d)",
+                    off, required_len, bufsize);
 		return false;
 	}
 	return true;
@@ -1637,14 +1650,21 @@ void *ad_entry(const struct adouble *ad, int eid)
 	size_t len = ad_getentrylen(ad, eid);
 	bool valid;
 
+	if (bufsize == 0) {
+		bufsize = sizeof(ad->ad_data) - (off + len);
+	}
+
 	valid = ad_entry_check_size(eid, bufsize, off, len);
 	if (!valid) {
+		LOG(log_error, logtype_ad, "ad_entry: not valid");
 		return NULL;
 	}
 
-	if (off == 0 || len == 0) {
+	/*if (off == 0 || len == 0) {
+		LOG(log_error, logtype_ad, "ad_entry: off or len is 0 (off: %d, len: %d)",
+                    off, len);
 		return NULL;
-	}
+	}*/
 
 	return ((struct adouble *)ad)->ad_data + off;
 }
