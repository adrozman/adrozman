---
title: ML Model for Rotor Efficiency Prediction
permalink: /pub_altpages/ml-rotor-efficiency/
layout: textlay
sitemap: false
---

# ML Model for Rotor Efficiency Prediction

This project objective was to create a machine learning model to predict the efficiency of a rotor blade based on its shape and operating condition.
The first challenge was to parameterize the shape of the blade. 
This was done by defining the chord, twist, and quarter chord location in Y and Z directions as a function of span.


<div class="clearfix" markdown="0" style="text-align: center; margin: 20px 0;">
    <img src="{{ site.url }}{{ site.baseurl }}/images/stacked_parameters.png" style="max-width: 40%; border-radius: 8px;">
    <p><em>Blade geometry parameterized representation as a 1D array.</em></p>
</div>

Dimensional reduction was applied to reduce the number of inputs and thus the complexity of the model. 
Principal Component Analysis (PCA) was found to parameterize these geometries the best, being able to reconstruct the original shape with negligible error using only the first 14 principal components. 
This reduced representation was also used to increase the number of blade geometries in the sample set by randomly perturbing the amplitudes along the principal directions.
A sample of blades produced using this technique are shown below.

<div class="clearfix" markdown="0" style="text-align: center; margin: 20px 0;">
    <img src="{{ site.url }}{{ site.baseurl }}/images/perturbed_blades.gif" style="max-width: 40%; border-radius: 8px;">
    <p><em>Perturbed Blade Geometries that Expand the Training Set</em></p>
</div>

Finally, the model was constructed using a Multi-Layer Perceptron Neural Network architecture. The model was able to predict the rotor figure of merit very accurately, even for holdout cases where a particular "family" of geometries was excluded from the training set.

<div class="clearfix" markdown="0" style="text-align: center; margin: 20px 0;">
    <img src="{{ site.url }}{{ site.baseurl }}/images/FM_removed_pair_n=14.png" style="max-width: 40%; border-radius: 8px;">
    <p><em>Figure of Merit Prediction for Holdout Case</em></p>
</div>

