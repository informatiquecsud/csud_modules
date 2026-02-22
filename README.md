# csud_modules

Modules Python used at Collège du Sud for teaching CS

## Loading a module from Pyodide (WebTigerPython)

```python
import micropip
await micropip.install("https://raw.githubusercontent.com/informatiquecsud/csud_modules/refs/heads/main/dist/csud-0.1.0-py3-none-any.whl")

from csud.crypto import *
```
