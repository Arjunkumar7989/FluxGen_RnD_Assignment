def interest_zone_sensitivity(grid, stress, zone):
    x, y = zone
    return {
        "Head": grid[x, y],
        "Stress": stress[x, y]
    }
