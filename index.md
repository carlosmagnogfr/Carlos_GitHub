![Finance_Image](finance_2.jpg)

## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/carlosmagnogfr/Finance_Stuff/edit/master/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/carlosmagnogfr/Finance_Stuff/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.




```python
from math import exp, sqrt
import numpy as np

def binomial_tree(s, k, t, v, rf, cp, jr, am:False, n=100):
  """Price option with binomial trees and Cox, Ross and Rubinstein (1979) formula"""
  #Cálculos iniciais
  h=t/n
  if jr==1:
    u=exp((rf-0.5*v**2)*h+v*sqrt(h))
    d=exp((rf-0.5*v**2)*h-v*sqrt(h))
  else:
    u=exp(v*sqrt(h))
    d=exp(-v*sqrt(h))
  
  drift=exp(rf*h)
  q=(drift-d)/(u-d)
  
  #Process the terminal stock price
  stkval = np.zeros((n+1,n+1))
  optval = np.zeros((n+1,n+1))
  stkval[0,0] = s

  for i in range(1, n+1):
    stkval[i,0] = stkval[i-1,0]*u
    for j in range (1, n+1):
      stkval[i,j] = stkval[i-1,j-1]*d
  
  #Backward recursion for option price
  # REVER ESSA PARTE
  for j in range(n + 1):
    optval[n,j] = max(0,cp*(stkval[n,j]-k))
    for i in range(n-1,-1,-1):
      for j in range(i+1):
        optval[i,j] = (q*optval[i+1,j]+(1-q)*optval[i+1,j+1])/drift
        if am:
          optval[i,j] = max(optval[i,j],cp*(stkval[i,j]-k))
  return optval[0,0]
```
