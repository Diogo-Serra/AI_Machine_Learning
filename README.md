![AI & Machine Learning banner](src/header-banner.png)

# AI & Machine Learning

A growing collection of hands-on projects that explore how AI and machine
learning systems work, from model fundamentals to practical applications.

The focus is on learning by building: implementing core ideas, studying their
trade-offs, and documenting the reasoning behind each solution.

## Areas of exploration

- Large language models and autoregressive generation
- Tokenization, embeddings, and attention
- Constrained decoding and structured outputs
- Classical machine learning algorithms
- Model evaluation, reliability, and performance
- Applied AI systems

## Projects

| Project | Description | Topics |
| --- | --- | --- |
| [Call Me Maybe](projects/function_call/) | Converts natural-language requests into typed function calls using a small local LLM and constrained decoding. | LLMs, tokenization, function calling, structured output |

Each project contains its own documentation, setup instructions, design
decisions, and technical analysis.

## Repository structure

```text
AI_Machine_Learning/
├── projects/
│   └── function_call/  # Constrained LLM function calling
└── README.md
```

## Approach

Projects in this repository aim to:

- build important mechanisms instead of treating models as black boxes;
- explain algorithms and design decisions clearly;
- use reproducible environments and documented workflows;
- validate results with testing, static analysis, and measurable outcomes
- connect theory to working implementations.

## Tech stack

The tools vary by project. Current work primarily uses Python, PyTorch,
Transformers, NumPy, MatPlotLib, Pydantic, and `uv`.

## Getting started

Open the [project index](#projects), choose a project, and follow the setup and
usage instructions in its README. Projects are self-contained and may have
different dependencies or system requirements.

## Resources

### Official documentation

- [PyTorch documentation](https://docs.pytorch.org/docs/2.13/)
- [Python documentation](https://docs.python.org/3/)
- [NumPy documentation](https://numpy.org/doc/stable/)
- [Matplotlib documentation](https://matplotlib.org/stable/)
- [Jupyter documentation](https://docs.jupyter.org/en/latest/)
- [Hugging Face Transformers documentation](https://huggingface.co/docs/transformers/)

### Courses and lectures

- [Andrej Karpathy - The spelled-out intro to language modeling: building makemore](https://www.youtube.com/watch?v=PaCmpygFfXo&t=4124s)
- [Andrej Karpathy - Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)
