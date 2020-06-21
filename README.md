## nbautoconvert
  Without any plugin support, convert your jupyter notebook directly to markdown (README.md)!  

## Setup
  To fireup, copy the nbautoconvert file from here to the root of your repository. Next, you need to place this pre-commit inside repo/.git/hooks/. That's it!  

Freely make changes in your notebook, as from now everytime you commit any change in your notebook, your README will be automatically rendered with your notebook. This rendering also includes the outputs of notebook and will be captured inside README_files. Linking between output and README.md is also be auto-configured.  

## Pre-commit hook

  This pre-commit hook gets triggered even before you've set the commit message. Further more, this invokes the nbautoconvert residing at the root of the project.  

## Core script

  This is the main script which will perform the core work. On being invoked, this checks for all the files which have been added/modified, any file ending with ".ipynb" will be taken into consideration and will converted to README.md using jupyter nbconvert. Again, since it's a readme file, I have added it at the root of the repo.  

*Name and directory of the output markdown file can be easily configured in the nbautoconvert script.*

<h4>Key notes<h4>
    1. Name of notebook shouldn't have any spaces<br>
	<br>2. Pre-commit hook file shouldn't already exist<br>
	<br>3. Notebook should be at the root of the project<br>


```python

```
