import pybamm
import numpy as np
'''
models = [
    pybamm.lithium_ion.SPM(),
    pybamm.lithium_ion.SPMe(),
    pybamm.lithium_ion.DFN(),
]
sims = []
for model in models:
    sim = pybamm.Simulation(model)
    sim.solve([0, 3600])
    sims.append(sim)

#pybamm.dynamic_plot(sims)
#interactive(children=(FloatSlider(value=0.0, description='t', max=3600.0, step=36.0), Output()), _dom_classes=…
#<pybamm.plotting.quick_plot.QuickPlot at 0x7faf48ed9490>)
output_variables = ["Electrolyte concentration [mol.m-3]", "Voltage [V]"]
sim.plot(output_variables=output_variables)

sim.plot(
    [
        ["Electrode current density [A.m-2]", "Electrolyte current density [A.m-2]"],
        "Voltage [V]","Current [A]",
    ]
)
sim.plot_voltage_components()
sim.plot_voltage_components(split_by_electrode=True)

parameter_values = pybamm.ParameterValues("Chen2020")
parameter_values["Ambient temperature [K]"] = 278
sims = []
for model in models:
    sim = pybamm.Simulation(model)
    sim.solve([0, 3600])
    sims.append(sim)
pybamm.dynamic_plot(sims)
sim.plot(
    [
        ["Electrode current density [A.m-2]", "Electrolyte current density [A.m-2]"],
        "Voltage [V]","Current [A]",
    ]
)
'''

experiment = pybamm.Experiment(
    [
        "Discharge at C/10 for 10 hours or until 3.3 V",
        "Rest for 1 hour",
        "Charge at 1 A until 4.1 V",
        "Hold at 4.1 V until 50 mA",
        "Rest for 1 hour",
    ]*10
)
model = pybamm.lithium_ion.DFN()
sim = pybamm.Simulation(model, experiment=experiment)
sim.solve()
sim.plot()
# this will plot the cycle number
sim.solution.cycles[5].plot()

t = np.linspace(0, 1, 60)
sin_t = 0.5 * np.sin(2 * np.pi * t)
drive_cycle_power = np.column_stack([t, sin_t])
experiment = pybamm.Experiment([pybamm.step.power(drive_cycle_power)])
sim = pybamm.Simulation(model, experiment=experiment)
sim.solve()
sim.plot()