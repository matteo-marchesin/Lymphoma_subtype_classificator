#!/usr/bin/env python3
# -*- coding: utf-8 -*-

EXTERNAL_SOURCES: list[str] = [
    "src/modulo_x.py",      # file singolo -> modulo "modulo_x"
    "src/mio_pkg",          # directory pacchetto -> package "mio_pkg" + submoduli
    # "qualcosaltro/sotto/pkg_y",
]





if __name__ == "__main__":
    asyncio.run(main())
