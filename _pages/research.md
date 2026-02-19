---
title: "Research"
layout: textlay
excerpt: "Adam Rozman Research PhD Candidate"
sitemap: false
permalink: /research/
---

# Research Overview

My research focuses on computationally modeling unsteady aerodynamics and aeroacoustics, specifically aimed at reducing the noise of next-generation rotorcraft vehicles. I apply and develop models spanning a range of fidelities depending on application scale- from developing databases to capture acoustic and performance trends using analytical models, to understanding the complex three-dimensional dynamics causing propeller noise in edgewise flight and multirotor configurations using high-fidelity Computational Fluid Dynamics (CFD). As drones and electric Vertical Take-Off and Landing (eVTOL) aircraft become more prevalent in urban environments, understanding and predicting their complex noise signatures is critical for public and regulatory acceptance.

---

## Wing-Propeller Aeroacoustic Interaction
This work investigated the interaction noise caused by a pusher-propeller ingesting the wake of a wing. This is a common configuration in future aircraft design and relevant to multirotor and eVTOL designs that include propellers mounted close to lifting surfaces.

<div class="clearfix" markdown="0" style="text-align: center; margin: 20px 0;">
    <img src="{{ site.url }}{{ site.baseurl }}/images/aart-animation.gif" alt="AART Q Criterion" style="max-width: 80%; border-radius: 8px;">
    <p><em>Figure 1: Q-criterion isosurface of wing-propeller interaction.</em></p>
</div>

* **Acoustic Analogy Evaluation**: Developed a pipeline to extract data from a government CFD suite into permeable surface Ffowcs Williams-Hawkings (FW-H) inputs. I investigated the acoustic prediction of these permeable surfaces, exploring downstream extent and endcap averaging, and compared to the more traditional impermeable FW-H approach. Results agreed closely and showed that the permeable approach does not capture any extra contributions to tonal noise.
* **Turbulence Modeling**: Investigated the impact of laminar-to-turbulent transition models in hybrid RANS/LES (DES). Found that the transition models predicted a significantly smaller wing wake defecit, predicting lower interaction noise and agreeing worse with the experiment.

<div class="clearfix" markdown="0" style="text-align: center; margin: 20px 0;">
    <img src="{{ site.url }}{{ site.baseurl }}/images/aart_mic10.png" alt="Permeable FW-H Results" style="max-width: 80%; border-radius: 8px;">
    <p><em>Figure 2: Far-field acoustic results comparison between permeable and impermeable FW-H methods and experiment.</em></p>
</div>

---

## eVTOL Propeller Modeling & Urban Gust Response
This work centers around experimental measurements taken on a scaled-down version of a realistic eVTOL propeller, designed by Joby Aviation, tested in the Virginia Tech Stability Wind Tunnel. I implemented reduced-order and high-fidelity CFD models of the propeller in the various inflow conditions tested in the experiment.

* **Urban Gust Impacts**: I investigated the effect of large transient disturbances on the noise of an eVTOL propeller in a vertiport approach trajectory. I implemented a canonical disturbance and one extracted from an urban flow CFD simulation. My findings show an average increase of ~2.3 dB in overall sound pressure levels due to increased Blade Vortex Interaction (BVI) during gust encounters.
* **Computational Efficiency**: Demonstrated that actuator line models can provide acoustic predictions at an order of magnitude lower cost, enabling long-duration transient noise analysis that would be prohibitive with blade-resolved CFD.

<div class="clearfix" markdown="0" div style="text-align: center; margin: 20px 0;">
    <img src="{{ site.url }}{{ site.baseurl }}/images/joby_qcrit.png" alt="Propeller Wake Visualizations" style="max-width: 80%; border-radius: 8px;">
    <p><em>Figure 3: Q-criterion isosurface of high-fidelity simulation of eVTOL propeller in edgewise flight</em></p>
</div>

<div class="clearfix" markdown="0" div style="text-align: center; margin: 20px 0;">
    <img src="{{ site.url }}{{ site.baseurl }}/images/palm_disturbance_spectrogram.png" alt="Spectrogram with disturbance" style="max-width: 80%; border-radius: 8px;">
    <p><em>Figure 4: Spectrogram examining the noise of a propeller impacted by a disturbance extracted from an urban flow model of Boston.</em></p>
</div>
