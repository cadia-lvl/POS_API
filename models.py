
import pos
import torch

# Initialize the tagger
device = torch.device("cpu")  # CPU
tagger_model: pos.Tagger = torch.hub.load(
    repo_or_dir="cadia-lvl/POS",
    model="tag",
    device=device,
    force_reload=False,
    force_download=False,
)

