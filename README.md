# matplotlib-din461

Changes the appearance of a python matplotlib 2D plot in accordance with DIN461. <br />
DIN461 is a German standard: <br />
* https://www.beuth.de/de/norm/din-461/710844
* https://de.wikipedia.org/wiki/DIN_461

## Minimal example (tested in Python 3.x)

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib_din461 import apply_din461

t = np.arange(0.0, 1.0 + 0.01, 0.01)
s = np.cos(4 * np.pi * t) + 2

plt.plot(t, s)
plt.xlabel("Time $t$")
plt.ylabel("Voltage $U$")

ax = plt.gca()
apply_din461(ax, "s", "V")

plt.tight_layout()
plt.show()
```

### Result
![matplotlib-din461-example](https://user-images.githubusercontent.com/8809455/174426531-b887c7e7-7f26-4451-97dc-eb9e9e4505c4.png)


## Parameters of apply_din461

```python
def apply_din461(ax, x_unit_name, y_unit_name, x_left_to_right=True, y_bottom_to_top=True):
```
* ax (matplotlib ax): Axis to be motified
* x_unit_name (unicode): Name of the unit in x direction
* y_unit_name (unicode): Name of the unit in y direction
* x_left_to_right (bool): If True, arrow from left to right
* y_bottom_to_top (bool): If True, arrow bottom to top


## License
This project is licensed under the terms of the MIT license - see the [LICENSE](LICENSE) file for details.
