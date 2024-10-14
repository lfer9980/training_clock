from math import pi

from parapy.geom import *
from parapy.core import *


class AnalogClock(GeomBase):
    # constants
    HOURS_SEGMENTS: int = 12
    MINUTES_SEGMENTS: int = 60
    CLOCK_RADIUS: int = 1
    WIDTH_SEGMENT_HOURS: int = 0.2
    WIDTH_SEGMENT_MINUTES: int = 0.1

    # inputs
    hours: int = Input(0)
    minutes: int = Input(0)

    # parts
    clock_shell: Part = Part(derived)
    clock_center: Part = Part(derived)
    division_primary: Part = Part(derived)
    division_secondary: Part = Part(derived)
    indicator_hours: Part = Part(derived)
    indicator_minutes: Part = Part(derived)

    # Attributes
    @staticmethod
    def angle_step(steps):
        return 2 * pi / steps

    @clock_shell.getter
    def getter(self):
        return Cylinder(radius=self.CLOCK_RADIUS,
                        height=0.1,
                        color="white",
                        centered=True,
                        )

    @clock_center.getter
    def getter(self):
        return Cylinder(radius=0.05,
                        height=0.11,
                        color='black',
                        centered=True
                        )

    @division_primary.getter
    def getter(self):
        return Box(quantify=self.HOURS_SEGMENTS,
                   width=self.WIDTH_SEGMENT_HOURS,
                   length=0.05,
                   height=0.11,
                   color="black",
                   centered=True,
                   position=translate(rotate(self.position,
                                             rotation_axis='z',
                                             angle=self.angle_step(steps=self.HOURS_SEGMENTS) * child.index,
                                             deg=False,
                                             ),
                                      'x', self.CLOCK_RADIUS - 0.05 - 0.1,
                                      ),
                   )

    @division_secondary.getter
    def getter(self):
        return Box(quantify=self.MINUTES_SEGMENTS,
                   width=self.WIDTH_SEGMENT_MINUTES,
                   length=0.03,
                   height=0.11,
                   color="black",
                   centered=True,
                   position=translate(rotate(self.position,
                                             rotation_axis='z',
                                             angle=self.angle_step(steps=self.MINUTES_SEGMENTS) * child.index,
                                             deg=False,
                                             ),
                                      'x', self.CLOCK_RADIUS - 0.03 - 0.1,
                                      ),
                   )

    @indicator_hours.getter
    def getter(self):
        return Box(width=0.05,
                   length=self.CLOCK_RADIUS / 2,
                   height=0.11,
                   color="black",
                   centered=True,
                   position=translate(rotate(self.position,
                                             rotation_axis='z',
                                             angle=-self.angle_step(self.HOURS_SEGMENTS) * self.hours,
                                             deg=False),
                                      'y', self.CLOCK_RADIUS - 0.85,
                                      )
                   )

    @indicator_minutes.getter
    def getter(self):
        return Box(width=0.03,
                   length=self.CLOCK_RADIUS - 0.2,
                   height=0.11,
                   color="black",
                   centered=True,
                   position=translate(rotate(self.position,
                                             rotation_axis='z',
                                             angle=-self.angle_step(self.MINUTES_SEGMENTS) * self.minutes,
                                             deg=False),
                                      'y', self.CLOCK_RADIUS - 0.7,
                                      )
                   )
