import pybamm

# Create a basic battery model
model = pybamm.lithium_ion.DFN()  # Doyle-Fuller-Newman model

# Set up simulation
sim = pybamm.Simulation(model)

# Solve the model
sim.solve([0, 3600])  # Simulate for 1 hour (3600 seconds)

# Plot the results
sim.plot()