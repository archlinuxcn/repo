=========
 CHANGES
=========

Only (unlikely) intentional breaking changes and new/added non-trivial
functionality is listed here, no bugfixes or commit messages.

Each entry is a package version which change first appears in,
followed by description of the change itself.

Last synced/updated: 22.3.2

---------------------------------------------------------------------------

- 21.10.4: Add channel_list_enum to compare channel_list values with something
  in a typo-free way, expose channel_list_raw with C enum values [#66].

- 21.5.0: Fix PA_VOLUME_MAX and PA_VOLUME_UI_MAX values, both were incorrect [#53].

- 21.3.4: Add timeout= option for connect() method [#48].

- 21.3.1: There is now https://pypi.org/project/pulsectl-asyncio/ module [#46].

  It is maintained separately, and should provide similar bindings to use with async apps.

- 20.2.4: Add pulse.get_card_by_name() wrapper [#38].

- 20.1.1: Add pulse.play_sample() - server-side stored sample playback [#36].

  Loading is not implemented, would suggest something like libcanberra for that.

- 19.9.1: Add pulse.get_peak_sample() func for getting volume peak within timespan [#33].

- 18.10.5: pulse.connect() can now be used to reconnect to same server.

- 17.12.2: Use pa_card_profile_info2 / profiles2 introspection API [#19].

  Only adds one "available" property to PulseCardProfileInfo.
  Requires pulseaudio/libpulse 5.0+.

- 17.9.3: Add wrappers for Pulse.get_sink_by_name / Pulse.get_source_by_name [#17].

  More efficient alternative for sink_input_list / source_output_list filtering.

- 17.6.0: Add PulseCardInfo.port_list [#15].

  These ports are different from sink/source ports in that they have proplist,
  card profiles and some other parameters associated with them, implemented as
  PulseCardPortInfo instances.

- 17.1.3: Add wrappers for card profiles [#14].

  More specifically - PulseCardProfileInfo objects and PulseCardInfo
  "profile_list" and "profile_active" attributes.

  ``pulse.card_profile_set(card, profile)`` can be used to set active profile
  (either by name or PulseCardProfileInfo object).

- 16.11.0: This changelog file was started, thanks to the idea from #12.
