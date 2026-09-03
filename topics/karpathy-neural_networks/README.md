# Neural Networks: Zero to Hero (Karpathy)

Working through Andrej Karpathy's [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)
series, building neural networks and language models from scratch — from
backpropagation basics to a GPT-style Transformer.

- [Playlist](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)
- [Reference notebooks & code](https://github.com/karpathy/nn-zero-to-hero)

## Progress

| # | Folder | Topic |
| --- | --- | --- |
| 1 | [01-micrograd](01-micrograd/) | Backpropagation & autograd engine from scratch |
| 2 | [02-makemore-bigram](02-makemore-bigram/) | Bigram character-level language model |
| 3 | [03-makemore-mlp](03-makemore-mlp/) | MLP language model |
| 4 | [04-makemore-batchnorm](04-makemore-batchnorm/) | Activations, gradients, BatchNorm |
| 5 | [05-makemore-backprop-ninja](05-makemore-backprop-ninja/) | Manual backprop through the MLP |
| 6 | [06-makemore-wavenet](06-makemore-wavenet/) | WaveNet-style hierarchical model |
| 7 | [07-gpt](07-gpt/) | Building GPT from scratch |
| 8 | [08-tokenizer](08-tokenizer/) | Building the GPT tokenizer |

## Setup

```bash
cd topics/karpathy-neural_networks
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
