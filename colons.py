from parapy.core import *
from parapy.geom import *

class Colons(GeomBase):
    # parts
    colonA: Part = Part(derived)
    colonB: Part = Part(derived)
    compound_colons: Part = Part(derived)

    @colonA.getter
    def getter(self):
        return ChamferedSolid(built_from=Box(width=0.1,
                                             length=0.1,
                                             height=0.11,
                                             centered=True,
                                             position=translate(self.position, 'y', 0.35)
                                             ),
                              distance=0.025,
                              )

    @colonB.getter
    def getter(self):
        return ChamferedSolid(built_from=Box(width=0.1,
                                             length=0.1,
                                             height=0.11,
                                             centered=True,
                                             position=translate(self.position, 'y', -0.35)
                                             ),
                              distance=0.025,
                              )

    @compound_colons.getter
    def getter(self):
        return Compound(built_from=[self.colonA, self.colonB])

