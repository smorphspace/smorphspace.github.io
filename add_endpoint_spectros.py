"""
Patch samples.json to add src_spectro / tgt_spectro fields for RQ2 and RQ3 pairs.
These are placeholder mappings reusing the trajectory endpoint spectrograms — marked WIP.

RQ2 (audio→prompt):  src_spectro = spectros[0],  no tgt_spectro (tgt is text)
RQ3 (audio→audio):   src_spectro = spectros[0],  tgt_spectro = spectros[-1]
"""

import json
from pathlib import Path

SAMPLES = Path("audio/samples.json")

with open(SAMPLES) as f:
    samples = json.load(f)

for rq, rq_data in samples["data"].items():
    for ds, ds_data in rq_data.items():
        first_method = ds_data["methods"][0]
        for pair in ds_data["pairs"]:
            spectros = pair["methods"][first_method]["spectros"]
            if rq == "rq2":
                pair["src_spectro"] = spectros[0]
                pair.pop("tgt_spectro", None)
            elif rq == "rq3":
                pair["src_spectro"] = spectros[0]
                pair["tgt_spectro"] = spectros[-1]

with open(SAMPLES, "w") as f:
    json.dump(samples, f, indent=2)

print("Done.")
