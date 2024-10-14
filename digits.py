from parapy.core import *
from parapy.geom import *


class Digits(GeomBase):
    # Parts
    digit_0: Part = Part(derived)
    digit_1: Part = Part(derived)
    digit_2: Part = Part(derived)
    digit_3: Part = Part(derived)
    digit_4: Part = Part(derived)
    digit_5: Part = Part(derived)
    digit_6: Part = Part(derived)
    digit_7: Part = Part(derived)
    digit_8: Part = Part(derived)
    digit_9: Part = Part(derived)

    digits_segment_a: ChamferedSolid = ChamferedSolid(built_from=Box(width=0.5,
                                                                     length=0.1,
                                                                     height=0.11,
                                                                     centered=True,
                                                                     position=translate(XOY, 'y', 0.5)
                                                                     ),
                                                      distance=0.025,
                                                      )

    digits_segment_b: ChamferedSolid = ChamferedSolid(built_from=Box(width=0.1,
                                                                     length=0.4,
                                                                     height=0.11,
                                                                     centered=True,
                                                                     position=translate(XOY, 'x', 0.3, 'y',
                                                                                        0.25)
                                                                     ),
                                                      distance=0.025,
                                                      )

    digits_segment_c: ChamferedSolid = ChamferedSolid(built_from=Box(width=0.1,
                                                                     length=0.4,
                                                                     height=0.11,
                                                                     centered=True,
                                                                     position=translate(XOY, 'x', 0.3, 'y',
                                                                                        -0.25)
                                                                     ),
                                                      distance=0.025,

                                                      )

    digits_segment_d: ChamferedSolid = ChamferedSolid(built_from=Box(width=0.5,
                                                                     length=0.1,
                                                                     height=0.11,
                                                                     centered=True,
                                                                     position=translate(XOY, 'y', -0.5)
                                                                     ),
                                                      distance=0.025,
                                                      )

    digits_segment_e: ChamferedSolid = ChamferedSolid(built_from=Box(width=0.1,
                                                                     length=0.4,
                                                                     height=0.11,
                                                                     centered=True,
                                                                     position=translate(XOY, 'x', - 0.3, 'y',
                                                                                        - 0.25)
                                                                     ),
                                                      distance=0.025,
                                                      )

    digits_segment_f: ChamferedSolid = ChamferedSolid(built_from=Box(width=0.1,
                                                                     length=0.4,
                                                                     height=0.11,
                                                                     centered=True,
                                                                     position=translate(XOY, 'x', -0.3, 'y',
                                                                                        0.25)
                                                                     ),
                                                      distance=0.025,
                                                      )

    digits_segment_g: ChamferedSolid = ChamferedSolid(built_from=Box(width=0.5,
                                                                     length=0.1,
                                                                     height=0.11,
                                                                     centered=True,
                                                                     ),
                                                      distance=0.025,
                                                      )

    @digit_0.getter
    def getter(self):
        return Compound(built_from=[self.digits_segment_a,
                                    self.digits_segment_b,
                                    self.digits_segment_c,
                                    self.digits_segment_d,
                                    self.digits_segment_e,
                                    self.digits_segment_f,
                                    ],
                        )

    @digit_1.getter
    def getter(self):
        return Compound(built_from=[self.digits_segment_b,
                                    self.digits_segment_c,
                                    ],
                        )

    @digit_2.getter
    def getter(self):
        return Compound(built_from=[self.digits_segment_a,
                                    self.digits_segment_b,
                                    self.digits_segment_g,
                                    self.digits_segment_e,
                                    self.digits_segment_d,
                                    ],
                        )

    @digit_3.getter
    def getter(self):
        return Compound(built_from=[self.digits_segment_a,
                                    self.digits_segment_b,
                                    self.digits_segment_g,
                                    self.digits_segment_c,
                                    self.digits_segment_d,
                                    ],
                        )

    @digit_4.getter
    def getter(self):
        return Compound(built_from=[self.digits_segment_f,
                                    self.digits_segment_g,
                                    self.digits_segment_b,
                                    self.digits_segment_c,
                                    ],
                        )

    @digit_5.getter
    def getter(self):
        return Compound(built_from=[self.digits_segment_a,
                                    self.digits_segment_f,
                                    self.digits_segment_g,
                                    self.digits_segment_c,
                                    self.digits_segment_d,
                                    ],
                        )

    @digit_6.getter
    def getter(self):
        return Compound(built_from=[self.digits_segment_a,
                                    self.digits_segment_f,
                                    self.digits_segment_g,
                                    self.digits_segment_e,
                                    self.digits_segment_c,
                                    self.digits_segment_d,
                                    ],
                        )

    @digit_7.getter
    def getter(self):
        return Compound(built_from=[self.digits_segment_a,
                                    self.digits_segment_b,
                                    self.digits_segment_c,
                                    ],
                        )

    @digit_8.getter
    def getter(self):
        return Compound(built_from=[self.digits_segment_a,
                                    self.digits_segment_b,
                                    self.digits_segment_c,
                                    self.digits_segment_d,
                                    self.digits_segment_e,
                                    self.digits_segment_f,
                                    self.digits_segment_g,
                                    ],
                        )

    @digit_9.getter
    def getter(self):
        return Compound(built_from=[self.digits_segment_a,
                                    self.digits_segment_b,
                                    self.digits_segment_f,
                                    self.digits_segment_g,
                                    self.digits_segment_c,
                                    ],
                        )
