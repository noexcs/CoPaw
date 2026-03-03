# -*- coding: utf-8 -*-
"""Timezone utilities for dynamic timezone detection."""

from tzlocal import get_localzone

def get_local_timezone() -> str:
    tz = get_localzone()
    return tz.key