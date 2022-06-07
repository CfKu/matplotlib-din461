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
![Figure_1](https://user-images.githubusercontent.com/106767099/172333364-c999b77e-2ddd-4a3f-975b-438c4810a8d2.png)


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

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

