import os; assert os.system("pip install -qqq PyYAML") == 0
from pathlib import Path
import yaml
from dataclasses import dataclass


@dataclass
class Price:
    model: str
    input: float
    output: float

    def per_tokens(self, input: int, output: int) -> float:
        return self.input * input + self.output * output


DIR_CURRENT = Path(__file__).parent

# https://openai.com/api/pricing/ (look for "Other models")
PRICES = {
    'gpt-3.5-turbo-0125': Price('gpt-3.5-turbo-0125', 0.5/(10**6), 1.5/(10**6)),
    'gpt-4-0125-preview': Price('gpt-4-0125-preview', 10.0/(10**6), 30.0/(10**6)),
}

total_tokens = 0
total_input_tokens = 0
total_output_tokens = 0
total_expense = 0.0

for path in DIR_CURRENT.glob('*.yml'):
    with open(path) as f:
        data = yaml.safe_load(f)
        try:
            tokens = data['usage']['total_tokens']
            total_tokens += tokens
            input_tokens = data['usage']['prompt_tokens']
            total_input_tokens += input_tokens
            output_tokens = data['usage']['completion_tokens']
            total_output_tokens += output_tokens
            price = PRICES[data['model']]
            expense = price.per_tokens(input_tokens, output_tokens)
            total_expense += expense
            print(f"+ {tokens} tokens = {input_tokens}in + {output_tokens}out = {expense}$")
        except KeyError as e:
            print(f"Error in {path}: {e}")

print(f"= {total_tokens} tokens = {total_input_tokens}in + {total_output_tokens}out = {total_expense}$")
