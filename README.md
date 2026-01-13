PROBLEM 1 – The Incomplete Geometry (FINAL R&D-GRADE WRITEUP)
My understanding of the problem

The core challenge is to estimate the total storage capacity of an irregular underground reservoir when only 65% of its spatial depth data is available. The remaining 35% must be inferred in a physically realistic way without introducing bias from simplistic averaging.

Key physical principles involved

Spatial continuity, natural boundary irregularity, and correlation between neighboring depth measurements govern the reservoir geometry. Since the walls are naturally formed, the surface is expected to be smooth but non-uniform, without engineered symmetry.

My approach

Simple averaging is inadequate because it ignores spatial correlation and boundary curvature. Instead, spatial interpolation techniques that respect physical continuity are required.
Kriging is preferred over spline or triangulation methods because it explicitly models spatial covariance between measurement points. This aligns with naturally formed reservoir walls, where depth variations are correlated over distance rather than changing arbitrarily. The inferred surface for the unmeasured region is generated based on nearby measured depths while preserving realistic gradients.

Assumptions & limitations

This approach assumes spatial smoothness and correlation continuity across the inaccessible region. It may fail in zones with sharp geological discontinuities such as faults or sudden lithological changes that violate smooth spatial behavior.

Uncertainty quantification

The dominant source of uncertainty arises from spatial sparsity rather than sensor noise. Multiple spatial realizations can be generated using Monte Carlo sampling of interpolation parameters, producing a distribution of possible volumes rather than a single estimate.

Validation strategy

The model is considered valid if the estimated total volume falls within ±10% of independent survey data, historical capacity records, or alternative interpolation methods applied to known regions. Sensitivity analysis is used to ensure no single region disproportionately influences the final estimate.

# PROBLEM 2 – The Spectral Discrepancy (FINAL R&D-GRADE WRITEUP)
My understanding of the problem

The challenge is to reconcile a satellite-detected increase in greenness across 50 water bodies with conflicting ground truth from 5 verified clear sites, while deciding whether a regional algae bloom alert should remain active.

Key physical principles involved

Atmospheric scattering, surface reflectance, and sensor band sensitivity can distort satellite-based greenness indices. Optical interference does not necessarily correspond to biological activity.

My approach

Non-biological factors such as atmospheric haze, sun-glint, and suspended sediments can falsely elevate visible-band greenness. Near-Infrared (NIR) bands are used to cross-check biological activity, as true algal biomass strongly reflects in NIR while optical artifacts do not.
To decide alert continuation, spatial weighting is applied. The 5 verified sites reduce uncertainty locally, but the remaining 45 sites still carry risk. A Bayesian update framework is used where field-verified clarity lowers probability only in nearby spatial clusters, not across the entire region.

Assumptions & limitations

This approach assumes spatial dependency between nearby water bodies. It may overestimate risk if the unverified sites experience fundamentally different environmental conditions.

Validation framework

Before issuing a high-risk alert, the system checks secondary data including recent rainfall, wind speed, surface temperature, and historical bloom seasonality. Alerts are triggered only if multispectral confirmation and environmental conditions jointly support biological plausibility.

Success criteria

An alert is allowed only if both spectral indicators and secondary environmental variables exceed predefined thresholds, reducing false positives caused by optical artifacts.

# PROBLEM 3 – The Balancing Act (FINAL R&D-GRADE WRITEUP)
My understanding of the problem

The objective is to reconcile a mass-balance mismatch in a closed watershed system where observed inflows, storage change, and outflows do not sum correctly.

Key physical principles involved

Mass conservation, delayed hydrological response, subsurface storage, evaporation, and sensor uncertainty govern the system behavior.

My approach

The missing 400 units can be attributed to subsurface infiltration, soil moisture storage, groundwater recharge, evaporation losses, and potential sensor lag or calibration error. These components are explicitly categorized into environmental storage, natural loss, and measurement uncertainty.

Delay modeling

The 12-hour delay between rainfall and outlet response is modeled using a time-lag or convolution-based response function representing travel time through the watershed. This delay is critical for early warning systems because immediate outlet readings cannot be used to infer real-time system saturation.

Temperature impact on volume vs mass

A 10°C temperature increase causes thermal expansion of water, affecting volume without changing mass. The digital twin accounts for this by correcting volume measurements using temperature-adjusted density relationships, preventing misinterpretation of expansion as added water input.

Validation strategy

The digital twin is validated if cumulative inflow equals corrected outflow plus adjusted storage change within acceptable tolerance limits over multiple rainfall events.
