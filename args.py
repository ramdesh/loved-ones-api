from dataclasses import dataclass


@dataclass
class args:
    dataset_path: str = ""
    dataset_cache: str = "./dataset_cache"
    model: str = "openai-gpt"
    model_checkpoint: str = ""
    max_history: int = 100
    device: str = "cpu"
    no_sample: bool = False
    max_length: int = 100
    min_length: int = 1
    seed: int = 0
    temperature: float = 0.7
    top_k: int = 0
    top_p: float = 0.9
