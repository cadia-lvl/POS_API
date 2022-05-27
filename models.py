import pos
import torch

device = torch.device("cpu")  # CPU
tagger_model: pos.Tagger = torch.hub.load(
    repo_or_dir="cadia-lvl/POS:master",
    skip_validation=True,
    model="tag",
    device=device,
    force_reload=False,
    force_download=False,
)

