from parapy.core import *
from parapy.geom import *

from analog_clock import AnalogClock
from digital_clock import DigitalClock


class Assembly(GeomBase):
    # Inputs
    minutes: int = Input(59)
    hours: int = Input(11)

    # final parts
    analog: Part = Part(derived)
    digital: Part = Part(derived)

    @analog.getter
    def getter(self):
        return AnalogClock(hours=self.hours,
                           minutes=self.minutes)

    @digital.getter
    def getter(self):
        return DigitalClock(hours=self.hours,
                            minutes=self.minutes)


if __name__ == "__main__":
    from parapy.gui import display

    assembly: Assembly = Assembly()

    display(obj=[assembly],
            viewport_grid=True,
            view='top',
            )
