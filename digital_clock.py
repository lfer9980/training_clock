from parapy.core import *
from parapy.geom import *

from digits import Digits
from colons import Colons


class DigitalClock(GeomBase):
    # input
    hours: Input = Input(0)
    minutes: Input = Input(0)

    # main
    digital_clock: Part = Part()
    translated_digit_a: Part = Part()
    translated_digit_b: Part = Part()
    translated_digit_c: Part = Part()
    translated_digit_d: Part = Part()
    colons: Part = Part()

    # Parts

    # methods
    @staticmethod
    def return_digit(class_name, rel_pos, number):
        attributes = dir(class_name)
        number = number

        str_num: str = f'0{number}' if 0 <= number <= 9 else f'{number}'
        int_number: int = int(str_num[rel_pos])

        methods = [attr for attr in attributes if callable(getattr(class_name, attr)) and 'digit_' in attr]
        invoke_method: str = methods[int_number]

        return getattr(class_name(), invoke_method)

    # parts
    @translated_digit_a.getter
    def getter(self):
        return TranslatedShape(shape_in=self.return_digit(class_name=Digits,
                                                          rel_pos=0,
                                                          number=self.hours,
                                                          ),
                               displacement=Vector(-1.5, 0, 0),
                               )

    @translated_digit_b.getter
    def getter(self):
        return TranslatedShape(shape_in=self.return_digit(class_name=Digits,
                                                          rel_pos=1,
                                                          number=self.hours,
                                                          ),
                               displacement=Vector(-0.6, 0, 0),
                               )

    @colons.getter
    def getter(self):
        return TranslatedShape(shape_in=Colons().compound_colons,
                               displacement=Vector(0, 0, 0),
                               )

    @translated_digit_c.getter
    def getter(self):
        return TranslatedShape(shape_in=self.return_digit(class_name=Digits,
                                                          rel_pos=0,
                                                          number=self.minutes,
                                                          ),
                               displacement=Vector(0.6, 0, 0),
                               )

    @translated_digit_d.getter
    def getter(self):
        return TranslatedShape(shape_in=self.return_digit(class_name=Digits,
                                                          rel_pos=1,
                                                          number=self.minutes,
                                                          ),
                               displacement=Vector(1.5, 0, 0),
                               )

    @digital_clock.getter
    def getter(self):
        return TranslatedShape(shape_in=Compound(built_from=[self.translated_digit_a,
                                                             self.translated_digit_b,
                                                             self.colons,
                                                             self.translated_digit_c,
                                                             self.translated_digit_d,
                                                             ],
                                                 ),
                               displacement=Vector(0, -2, 0),
                               color='red',
                               )
