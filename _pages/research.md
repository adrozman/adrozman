---
title: "Research"
layout: textlay
excerpt: "Adam Rozman Research PhD Candidate"
sitemap: false
permalink: /research/
---

# Research

# Research Overview

My research focuses on the intersection of computational fluid dynamics (CFD) and aeroacoustics, specifically aimed at reducing the noise footprint of next-generation aerial vehicles. As drones and electric Vertical Take-Off and Landing (eVTOL) aircraft become more prevalent in urban environments, understanding and predicting their complex noise signatures is critical for public acceptance and regulatory compliance.

---

## Wing-Propeller Aeroacoustic Interaction
This research evaluates the interaction between a pusher-propeller and a wing, focusing on how wing-wake inflow distortions increase noise levels. This is a common configuration in many multirotor and eVTOL designs.

<div class="clearfix" markdown="0" style="text-align: center; margin: 20px 0;">
    <img src="{{ site.url }}{{ site.baseurl }}/images/aart-animation.gif" alt="AART Q Criterion" style="max-width: 80%; border-radius: 8px;">
    <p><em>Figure 1: Computational geometry of the AART wing-propeller setup used for interaction noise studies.</em></p>
</div>

* **Acoustic Analogy Evaluation**: I compared permeable vs. impermeable Ffowcs Williams-Hawkings (FW-H) methods. Results indicated that while the permeable approach is viable, it provides negligible benefits over the simpler impermeable method for these specific interaction frequencies.
* **Turbulence Modeling**: Investigated the impact of laminar-to-turbulent transition models, finding that fully turbulent models better captured the wing wake deficit essential for accurate noise prediction.

<div class="clearfix" markdown="0" style="text-align: center; margin: 20px 0;">
    <img src="{{ site.url }}{{ site.baseurl }}/images/aart_mic10.png" alt="Permeable FW-H Results" style="max-width: 80%; border-radius: 8px;">
    <p><em>Figure 2: Far-field acoustic results comparison between FW-H methods and experiment.</em></p>
</div>

---

## eVTOL Propeller Dynamics & Urban Gust Response
Using a subscale Joby Aviation propeller as a benchmark, this work evaluates the trade-offs between high-fidelity CFD (OVERFLOW) and mid-fidelity actuator line models (ROAM) under complex flight conditions.

* **Urban Gust Impacts**: I modeled the effects of urban-informed gusts on a vertiport approach trajectory. My findings show an average increase of ~2.3 dB in overall sound pressure levels during gust encounters.
* **Computational Efficiency**: Demonstrated that actuator line models can provide acoustic predictions at an order of magnitude lower cost, enabling long-duration transient noise analysis that would be prohibitive with blade-resolved CFD.

<div class="clearfix" markdown="0" div style="text-align: center; margin: 20px 0;">
    <img src="{{ site.url }}{{ site.baseurl }}/images/joby_qcrit.png" alt="Propeller Wake Visualizations" style="max-width: 80%; border-radius: 8px;">
    <p><em>Figure 3: Simulated approach trajectory into a vertiport, incorporating urban-flow-informed gusts.</em></p>
</div>

<div class="clearfix" markdown="0" div style="text-align: center; margin: 20px 0;">
    <img src="{{ site.url }}{{ site.baseurl }}/images/palm_disturbance_spectrogram.png" alt="Spectrogram with disturbance" style="max-width: 80%; border-radius: 8px;">
    <p><em>Figure 4: Comparison of steady-state wake vs. wake structure under PALM-generated atmospheric disturbances.</em></p>
</div>

---

## Tools and Solvers
In my research, I utilize several high-performance computing (HPC) tools:
* **CREATE™-AV Helios & OVERFLOW**: High-fidelity CFD solvers.
* **PSU-WOPWOP**: Acoustic propagation using the FW-H analogy.
* **ROAM/CHARM**: Mid-fidelity aerodynamic modeling.
* **Python**: Data processing and signal analysis.
