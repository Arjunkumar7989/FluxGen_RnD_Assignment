from grid_model import initialize_grid
from source_propagation import apply_multiple_sources
from stress_analysis import cumulative_stress
from interest_zone import interest_zone_sensitivity

def main():
    # Initialize base groundwater head grid
    base_grid = initialize_grid(50)

    # Define groundwater consumption sources
    sources = [
        {"location": (10, 20), "strength": 5},   # Agriculture
        {"location": (30, 15), "strength": 8},   # Built-up
        {"location": (40, 35), "strength": 3},   # Forest
        {"location": (20, 40), "strength": 4},   # Water bodies
    ]

    # Apply sources using superposition
    grid = apply_multiple_sources(base_grid, sources)

    # Compute groundwater stress field
    stress = cumulative_stress(grid)

    # Evaluate critical / interest zone
    zone = (25, 25)
    report = interest_zone_sensitivity(grid, stress, zone)

    print("Critical Zone Report:", report)


if __name__ == "__main__":
    main()
