from asml_product_p10_if_shim import shim_if
print(shim_if({"coherence": 0.8, "bandwidth": 0.01, "power_frac": 0.75,
               "pol_degree": 0.6, "pulse_structure": 0.7, "pointing_jitter": 0.02}).to_dict())
