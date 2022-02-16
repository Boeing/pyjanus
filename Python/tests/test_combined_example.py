import pyJanus

# def combined_example():
    # janus = pyJanus.Janus("Examples/CombinedExample.xml")

janus = pyJanus.Janus("../../../Examples/CombinedExample.xml")
angle_of_attack = janus.get_variabledef("angleOfAttack")
reynolds_number = janus.get_variabledef("reynoldsNumber")
ambient_density = janus.get_variabledef("ambientDensity")
true_airspeed = janus.get_variabledef("trueAirspeed")
reference_area = janus.get_variabledef("referenceArea")
drag = janus.get_variabledef("drag")

angle_of_attack.set_value(10)
reynolds_number.set_value(0.36e6)
ambient_density.set_value(1.225)
true_airspeed.set_value(100.0)
reference_area.set_value(25.0)

drag.get_value()
print(drag)
