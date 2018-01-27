# matplotlib-din461

Changes the appearance of a python matplotlib 2D plot in accordance with DIN461. <br />
DIN461 is a German standard: <br />
* https://www.beuth.de/de/norm/din-461/710844
* https://de.wikipedia.org/wiki/DIN_461

## Minimal example

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib-din461 import apply_din461

t = np.arange(0.0, 1.0 + 0.01, 0.01)
s = np.cos(4 * np.pi * t) + 2

plt.plot(t, s)
plt.xlabel("Time $t$", fontsize=25)
plt.ylabel("Voltage $U$", fontsize=20)

ax = plt.gca()
apply_din461(ax, "s", "V")

plt.tight_layout()
plt.show()
```

### Result

![DIN461 plotting example](https://dl.dropboxusercontent.com/s/2ss8dc36eho96od/matplotlib-din461-example.png?dl=0)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

