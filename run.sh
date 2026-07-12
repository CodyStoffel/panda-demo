#!/bin/bash
unset LD_LIBRARY_PATH
LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MESA_LOADER_DRIVER_OVERRIDE=d3d12 python main.py
