from classes import RCScalculations
from output import Output
from inputing import Inputing

file = Inputing()
file.Init_Parametrs()

D=float(file.Get_D())
f_min=float(file.Get_min())
f_max=float(file.Get_max())

print(D,' ', f_min,' ', f_max)

RCS= RCScalculations(D, f_min, f_max)
RCS.RCScalculate()

print(RCS.GetRCS())

window= Output(RCS.GetFrequency(), RCS.GetRCS())
window.makeplot()

window.xml_saving()
