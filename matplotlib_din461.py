# -*- coding: utf-8 -*-
#
"""
MIT License

Copyright (c) 2018 Christof Küstner

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Switch to Python3 unicode literals and print() function
from __future__ import unicode_literals, print_function

import matplotlib.pyplot as plt
import matplotlib.ticker as mpl_ticker
import numpy as np


def apply_din461(ax, x_unit_name, y_unit_name,
                 x_left_to_right=True, y_bottom_to_top=True):
    """
    Applies the DIN 461 for units and labels

    @param ax: Axis to be motified
    @type  ax: matplotlib.axes
    @param x_unit_name: Name of the unit in x direction
    @type  x_unit_name: unicode
    @param y_unit_name: Name of the unit in y direction
    @type  y_unit_name: unicode
    @param x_left_to_right: If Ture, arrow from left to right
    @type  x_left_to_right: bool
    @param y_bottom_to_top: If Ture, arrow bottom to top
    @type  y_bottom_to_top: bool
    """
    # updates can only be applied if plot has been plotted/updated
    ax.figure.canvas.draw()

    # add arrow to x axis label
    label_text = ax.xaxis.get_label().get_text()
    if x_left_to_right:
        label_text += " $\longrightarrow$"
    else:
        label_text = "$\longleftarrow$ " + label_text
    ax.set_xlabel(label_text)

    # add arrow to y axis label
    label_text = ax.yaxis.get_label().get_text()
    if y_bottom_to_top:
        label_text += " $\longrightarrow$"
    else:
        label_text = "$\longleftarrow$ " + label_text
    ax.set_ylabel(label_text)

    # change the x unit name
    def x_tick_formatter(x, pos):
        visible_labels = [t for t in ax.get_xticklabels() if t.get_visible()]
        x_number_of_ticks = len(visible_labels)
        if pos == x_number_of_ticks - 2:
            return x_unit_name
        else:
            return unicode(x)
    ax.xaxis.set_major_locator(mpl_ticker.MaxNLocator(prune="upper"))
    ax.xaxis.set_major_formatter(mpl_ticker.FuncFormatter(x_tick_formatter))

    # change the y unit name
    def y_tick_formatter(x, pos):
        visible_labels = [t for t in ax.get_yticklabels() if t.get_visible()]
        y_number_of_ticks = len(visible_labels)
        if pos == y_number_of_ticks - 2:
            return y_unit_name
        else:
            return unicode(x)
    ax.yaxis.set_major_locator(mpl_ticker.MaxNLocator(prune="upper"))
    ax.yaxis.set_major_formatter(mpl_ticker.FuncFormatter(y_tick_formatter))


if __name__ == "__main__":
    # Minimal example (tested in Python 2.x)
    t = np.arange(0.0, 1.0 + 0.01, 0.01)
    s = np.cos(4 * np.pi * t) + 2

    plt.plot(t, s)
    plt.xlabel("Time $t$", fontsize=25)
    plt.ylabel("Voltage $U$", fontsize=20)

    ax = plt.gca()
    apply_din461(ax, "s", "V")

    plt.tight_layout()
    plt.show()
