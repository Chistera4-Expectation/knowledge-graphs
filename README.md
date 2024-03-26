## Knowledge Graphs
This repo contains the results of the experiments presented in the "Large language models as oracles for instantiating ontologies with domain-specific knowledge" paper.
The source code for running the KGFiller experiments is available [here](https://github.com/Chistera4-Expectation/kg-filler/tree/main).

### Repo Organization
The output of each experiment run is available on a different branch. The branch name identifies the LLM which was queried to build the ontology. For example, the results of the experiments run using GPT 3.5 are stored in the "experiments/food-openai-gpt-3.5-turbo-2024-03-04-11-49-51e65ec39eb5" branch.

Each branch corresponding to a single experiment contains:
- A single `ontology.owl` file which contains the owlready2 version of the ontology constructed using our proposed KGFiller tool. This file can be used to inspect the result of the ontology population process using an ontology editor and visualization tool such as [Protégé](https://protege.stanford.edu) or [PoolParty](https://www.poolparty.biz).
- A set of YAML files containing the results of each LLM query used to build the final ontology. The cache files can be used during the execution of the KGFiller tool to avoid querying multiple times the LLM with the same question.

Here we provide a list of the LLMs used for running each experiment and the corresponding branch name:
| LLM | Branch |
| ----------- | ----------- |
| GPT 3.5     | experiments/food-openai-gpt-3.5-turbo-2024-03-04-11-49-51e65ec39eb5       |
| GPT 4       | experiments/food-openai-gpt-4-turbo-preview-2024-03-07-08-18-c10105f7dc70 |
| Openchat    | experiments/food-hugging-openchat-2024-03-05-15-39-e818ad43d2ca           |
| Llama 2     | experiments/food-hugging-llama-2-2024-03-06-07-57-aaf72dd5a1b9            |
| Mistral     | experiments/food-hugging-mistral-2024-03-05-13-01-f05e54dd38b6            |
| Gemma       | experiments/food-hugging-gemma-2024-03-07-08-14-766c0f00ea6f              |
| Mixtral     | experiments/food-hugging-mixtral-2024-03-06-17-35-6b92d06e536b            |
| Nous Hermes | experiments/food-hugging-nous-hermes-2024-03-07-18-13-03cc5b03ae76        |

For more details about the experiments' setup, we would like to refer the reader to the paper.
