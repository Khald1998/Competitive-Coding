def moon_phase_emoji(date):
    day = int(date[:2])
    phases = [
        (5, "🌑"),
        (9, "🌒"),
        (13, "🌓"),
        (16, "🌔"),
        (20, "🌕"),
        (24, "🌖"),
        (28, "🌗"),
        (32, "🌘")
    ]
    for (phase_end_day, emoji) in phases:
        if day < phase_end_day:
            return emoji
    return phases[0][1]

print(moon_phase_emoji("01-09-1420"))
print(moon_phase_emoji("15-05-1436"))
print(moon_phase_emoji("29-11-1444"))
