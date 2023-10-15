# myapp.py

import physics

height = 100  # Výška v metrech

# Použití funkcí z modulu physics
fall_time = physics.free_fall_time(height)
lunar_fall_time = physics.lunar_free_fall_time(height)
light_year_distance = 9.461e15  # 1 světelný rok v metrech
light_year_time = physics.time_to_travel_light_years(light_year_distance)

print(f"Čas volného pádu na Zemi ze výšky {height} metrů: {fall_time} sekund")
print(f"Čas volného pádu na Měsíci ze výšky {height} metrů: {lunar_fall_time} sekund")
print(f"Čas cestování 1 světelným rokem: {light_year_time} sekund")
