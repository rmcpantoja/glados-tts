import torch

from utils.cleaners import Cleaner
from utils.tokenizer import Tokenizer

def prepare_text(text: str)->str:
    if not ((text[-1] == '.') or (text[-1] == '?') or (text[-1] == '!')):
        text = text + '.'
    cleaner = Cleaner('no_cleaners', True, 'es')
    tokenizer = Tokenizer()
    return torch.as_tensor(tokenizer(cleaner(text)), dtype=torch.int, device='cpu').unsqueeze(0)