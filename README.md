## nbautoconvert
  Without any plugin support, automatically convert jupyter notebook to markdown (README.md) as soon as you commit changes in notebook!!  

## Setup
  To fireup, copy the nbautoconvert sciprt from here to the root of your repository. Next, you need to place pre-commit hook inside repo/.git/hooks/ and you're good to go! 

## Usage
The usage is as simple as git commit because that's all you've to do and rest will be done by the script. Freely make changes in your notebook, as from now on, everytime you commit any change in your notebook, your README will be automatically rendered with your updated notebook. This visualization will also include the output images from notebook and will be captured inside README_files directory. Linking between these images and README.md is also auto-configured. 

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
