# SPDX-FileCopyrightText: 2020 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`displayio.epaperdisplay`
================================================================================

displayio for Blinka

**Software and Dependencies:**

* Adafruit Blinka:
  https://github.com/adafruit/Adafruit_Blinka/releases

* Author(s): Melissa LeBlanc-Williams

"""


__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_Blinka_displayio.git"


class EPaperDisplay:
    """Manage updating an epaper display over a display bus

    This initializes an epaper display and connects it into CircuitPython. Unlike other
    objects in CircuitPython, EPaperDisplay objects live until
    displayio.release_displays() is called. This is done so that CircuitPython can use
    the display itself.

    Most people should not use this class directly. Use a specific display driver instead
    that will contain the startup and shutdown sequences at minimum.
    """

    def __init__(
        self,
        display_bus,
        start_sequence,
        stop_sequence,
        *,
        width,
        height,
        ram_width,
        ram_height,
        colstart=0,
        rowstart=0,
        rotation=0,
        set_column_window_command=None,
        set_row_window_command=None,
        set_current_column_command=None,
        set_current_row_command=None,
        write_black_ram_command,
        black_bits_inverted=False,
        write_color_ram_command=None,
        color_bits_inverted=False,
        highlight_color=0x000000,
        refresh_display_command,
        refresh_time=40,
        busy_pin=None,
        busy_state=True,
        seconds_per_frame=180,
        always_toggle_chip_select=False,
        grayscale=False,
    ):
        # pylint: disable=too-many-locals,unnecessary-pass
        """
        Create a EPaperDisplay object on the given display bus (displayio.FourWire or
        displayio.ParallelBus).

        The start_sequence and stop_sequence are bitpacked to minimize the ram impact. Every
        command begins with a command byte followed by a byte to determine the parameter
        count and if a delay is need after. When the top bit of the second byte is 1, the
        next byte will be the delay time in milliseconds. The remaining 7 bits are the
        parameter count excluding any delay byte. The third through final bytes are the
        remaining command parameters. The next byte will begin a new command definition.


        :param display_bus: The bus that the display is connected to
        :type _DisplayBus: displayio.FourWire or displayio.ParallelBus
        :param ~_typing.ReadableBuffer start_sequence: Byte-packed initialization sequence.
        :param ~_typing.ReadableBuffer stop_sequence: Byte-packed initialization sequence.
        :param int width: Width in pixels
        :param int height: Height in pixels
        :param int ram_width: RAM width in pixels
        :param int ram_height: RAM height in pixels
        :param int colstart: The index if the first visible column
        :param int rowstart: The index if the first visible row
        :param int rotation: The rotation of the display in degrees clockwise. Must be in
            90 degree increments (0, 90, 180, 270)
        :param int set_column_window_command: Command used to set the start and end columns
            to update
        :param int set_row_window_command: Command used so set the start and end rows to update
        :param int set_current_column_command: Command used to set the current column location
        :param int set_current_row_command: Command used to set the current row location
        :param int write_black_ram_command: Command used to write pixels values into the update
            region
        :param bool black_bits_inverted: True if 0 bits are used to show black pixels. Otherwise,
            1 means to show black.
        :param int write_color_ram_command: Command used to write pixels values into the update
            region
        :param bool color_bits_inverted: True if 0 bits are used to show the color. Otherwise, 1
            means to show color.
        :param int highlight_color: RGB888 of source color to highlight with third ePaper color.
        :param int refresh_display_command: Command used to start a display refresh
        :param float refresh_time: Time it takes to refresh the display before the stop_sequence
            should be sent. Ignored when busy_pin is provided.
        :param microcontroller.Pin busy_pin: Pin used to signify the display is busy
        :param bool busy_state: State of the busy pin when the display is busy
        :param float seconds_per_frame: Minimum number of seconds between screen refreshes
        :param bool always_toggle_chip_select: When True, chip select is toggled every byte
        :param bool grayscale: When true, the color ram is the low bit of 2-bit grayscale
        """
        pass

    def show(self, group):
        # pylint: disable=unnecessary-pass
        """Switches to displaying the given group of layers. When group is None, the default
        CircuitPython terminal will be shown (eventually).
        """
        pass

    def refresh(self):
        # pylint: disable=unnecessary-pass
        """Refreshes the display immediately or raises an exception if too soon. Use
        ``time.sleep(display.time_to_refresh)`` to sleep until a refresh can occur.
        """
        pass

    @property
    def time_to_refresh(self):
        """Time, in fractional seconds, until the ePaper display can be refreshed."""
        return 0

    @property
    def width(self):
        # pylint: disable=unnecessary-pass
        """Display Width"""
        pass

    @property
    def height(self):
        # pylint: disable=unnecessary-pass
        """Display Height"""
        pass

    @property
    def bus(self):
        # pylint: disable=unnecessary-pass
        """Current Display Bus"""
        pass
