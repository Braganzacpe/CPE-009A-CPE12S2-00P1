from projectilemotion import projectilemotion_solver

v = 11.0
angle = 20.0

R, h = projectilemotion_solver(v, angle)

print("Horizontal Distance:", round(R, 2), "m")
print("Maximum Height:", round(h, 2), "m")