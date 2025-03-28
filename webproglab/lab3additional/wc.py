# Dictionary of Cricket World Cup winners (Year: Country)
world_cup_winners = {
    1975: "West Indies",
    1979: "West Indies",
    1983: "India",
    1987: "Australia",
    1992: "Pakistan",
    1996: "Sri Lanka",
    1999: "Australia",
    2003: "Australia",
    2007: "Australia",
    2011: "India",
    2015: "Australia",
    2019: "England",
    2023: "Australia"
}

# Count wins for each country
from collections import Counter
win_counts = Counter(world_cup_winners.values())

# Find the best performing country (most wins)
best_country = max(win_counts, key=win_counts.get)
best_wins = win_counts[best_country]

# Unique list of winning countries
unique_winners = set(world_cup_winners.values())

# Output results
print(f"🏆 Best Performing Country: {best_country} ({best_wins} wins)")
print("\n🌍 Unique World Cup Winners:")
for country in sorted(unique_winners):
    print("-", country)
