
How Temperature Estimation Works

1. Color Mapping to Temperature
Thermal images use a color gradient to represent temperature:
- White/Yellow/Orange → Warmer areas (typically core)
- Blue/Purple → Cooler areas (typically limbs or surroundings)

Each image includes a temperature scale (e.g., -5°C to 15°C), which helps map pixel colors to actual temperature values.



2. Region-Based Estimation
I visually analyze:
- Core regions: Head, chest, and torso
- Limb regions: Arms and legs

Using the color intensity in these regions and the image’s temperature scale, I estimate:
- Core temperature (usually higher)
- Limb temperature (usually lower)


3. Labeling Logic
Based on the average body temperature:
- Hyperthermic: > 37.5°C
- Normal: 36.0°C – 37.5°C
- Hypothermic: < 36.0°C

I am also normalizing borderline cases, so:
- Borderline hypothermic (e.g., 34–35.5°C) → can be labeled Normal
- Borderline hyperthermic (e.g., 37.5–38.0°C) → can be labeled Normal

