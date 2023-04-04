# Regex-finder
Implementation of regex-finder that computes plausible regex for given strings by finding common subsequences.

Instructions to use:

Regex finder
```
from regex import get_regex_patterns

codes = ['TMRQ40561', 'PIV30146', 'TICSV3941', 'QOM940315', 'GLDGH9481', 'MJY1481']
regexes = get_regex_patterns(codes)

# output:
        number of possible regrexes : 1
        0 -> [A-Z]{3,5}\d{4,6}
        Time taken : 6.198883056640625e-05 sec
```


Additional functionalities <br>
Data/Code generation

```
# To generate synthetic codes using prior codes.
from utils import generate_data

dataset, word_list = generate_data(prior_codes, num_instances=10,
	 			                   lower_b=1, upper_b=1)

# num_instances -> number of codes to generate
# lower_b -> minimum number of hex to be added to prior codes
# upper_b -> maximum number of hex to be added to prior codes
```
