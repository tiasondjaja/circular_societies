# Circular Societies Visualization Tool
*Kristen Mazur, Mutiara Sondjaja, Matthew Wright, and Carolyn Yarnall*

This github repostory contains a set of python tools for visualizing and generating examples of "circular societies" in approval voting.

**Try online** [!(Open In Colab)[https://colab.research.google.com/assets/colab-badge.svg]](https://colab.research.google.com/github/tiasondjaja/circular_societies/blob/master/examples-Google_Colab.ipynb)

**Contents**
+ Background
+ The `circularsocieties` module
  + Documentation
  + Requirements

## Background
The development of this tool is motivated by the following papers, which study [approval voting](https://en.wikipedia.org/wiki/Approval_voting) in a mathematical context.
+ Deborah E. Berg, Serguei Norine, Francis Edward Su, Robin Thomas, and Paul Wollan. "Voting in agreeable societies." The American Mathematical Monthly 117, no. 1 (2010): 27-39. [[link](https://www.tandfonline.com/doi/abs/10.4169/000298910X474961?casa_token=PlhiXI4HRjMAAAAA:yXsJ4gkl8AKIHl0Fb_mu4nmAePrEuOxU9lkP41GqRb4u9GYi6dfGNh-wv9cFq5Raf8JylMkW1jl8)]
+ Christopher S. Hardin,  "Agreement in circular societies." The American Mathematical Monthly 117, no. 1 (2010): 40-49. [[link](https://www.tandfonline.com/doi/pdf/10.4169/000298910X474970?casa_token=cFh5CCpwXZ4AAAAA:LuHGpNK3hLKUrAD2d2VyvNCYh3F7SZZ0h75zhnMewyczDoqUFMId3McqZoPWIG0UF1R9zAftBHx9)]
+ Kristen Mazur, Mutiara Sondjaja, Matthew Wright, and Carolyn Yarnall. "Approval voting in product societies." The American Mathematical Monthly 125, no. 1 (2018): 29-43.[[link](https://www.tandfonline.com/doi/full/10.1080/00029890.2018.1390370?casa_token=CdP_YwyN-rMAAAAA%3AYFnm8_De0WofNkewBpptRe1ACk5-8z9apxbj-En2e2gNSH9ypDlJv7R-oK2TjC6Tqrt3I4jEElbc)]
+ Francis Edward Su and Shira Zerbib. "Piercing numbers in approval voting." Mathematical Social Sciences 101 (2019): 65-71. [[link](https://www.sciencedirect.com/science/article/pii/S016548961930054X?casa_token=iDSgXTu-P9kAAAAA:fznLMC8CgdoV4LhBqUFPBlTW6WocgkfSkeFAiVru87ez_G2hzO972-gzY5IQXISu3aKwPK0)]

## The `circularsocieties` module
+ circularsocieties.py
+ Examples (local Jupyter notebook): examples.ipynb
+ Examples (online): examples-Google_Colab.ipynb [Link to Google Colab notebook](https://drive.google.com/file/d/1K2BIE4yZJZWwpXcJERYEuEgioiuWvZ9e/view?usp=sharing)

### Documentation
+ [DOCUMENTATION.md](https://github.com/tiasondjaja/circular_societies/blob/master/DOCUMENTATION.md)
### Requirements
+ numpy (for linear algebra computations)
+ matplotlib (for plotting/visualization)
+ cvxpy (for computing piercing numbers via integer programming)
+ cvxopt (allows cvxpy to use the open source mixed-integer program solver 'GLPK_MI')
+ itertools (for generating combinations of k objects from a collection of m objects)
