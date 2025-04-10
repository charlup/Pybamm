# Pybamm

# NCA Graphite model
This Repository holds a place for some practice electrochemical models for liion modelling.
The different models include:
- Graphite - NCA 


The charging protocol can be described by the following:
1. Charge to 4.2V using a 1C charge CC
2. Charge till 0.1C at 4.2V CV
3. Rest for 1 hr
4. Discharge at 0.1C to 2.5V
5. Step profile charge to 4.2V (Steps at 1C to 0.3, 0.7 to 0.8 and 0.3 to 1 SOC)
6. Rest for 30 mins
7. Discharge at 0.5C CC to 2.5V
8. Rest 30 mins 
Repeat steps 5-8 10 times

