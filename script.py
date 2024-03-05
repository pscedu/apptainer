#sort repositories
file = open("README.md", "w")

# STEM
repositories = ['octave','asciigenome']
repositories.sort()
file.write('# List of Apptainer definition files and more\n')
file.write('[![Build it!](https://github.com/pscedu/apptainer/actions/workflows/build.yml/badge.svg)](https://github.com/pscedu/apptainer/actions/workflows/build.yml)\n')
file.write('[![](https://imgs.xkcd.com/comics/cloud_2x.png)](https://xkcd.com/1444/)\n\n')
file.write('This repository lists the Apptainer definition files and other files needed to deploy software on Bridges2.\n')
file.write('## STEM\n')
file.write( '| Name | Information |\n' )
file.write( '| --- | --- |\n' )

for repository in repositories:
  str = '| [' + repository + '](http://github.com/pscedu/apptainer-' + repository + ') | ![Issue](https://img.shields.io/github/issues/pscedu/apptainer-' + repository + ')![forks](https://img.shields.io/github/forks/pscedu/apptainer-' + repository + ')![Stars](https://img.shields.io/github/stars/pscedu/apptainer-' + repository + ')![License](https://img.shields.io/github/license/pscedu/apptainer-' + repository + ') |\n'
  file.write( str )

# Utilities
repositories = ['chalk-cli','lowcharts','bat']
repositories.sort()
file.write('\n## Utilities\n')
file.write( '| Name | Information |\n' )
file.write( '| --- | --- |\n' )

for repository in repositories:
  str = '| [' + repository + '](http://github.com/pscedu/apptainer-' + repository + ') | ![Issue](https://img.shields.io/github/issues/pscedu/apptainer-' + repository + ')![forks](https://img.shields.io/github/forks/pscedu/apptainer-' + repository + ')![Stars](https://img.shields.io/github/stars/pscedu/apptainer-' + repository + ')![License](https://img.shields.io/github/license/pscedu/apptainer-' + repository + ') |\n'
  file.write( str )

file.write('---\nCopyright © 2020-2024 Pittsburgh Supercomputing Center. All Rights Reserved.\n\nThe [Biomedical Applications Group](https://www.psc.edu/biomedical-applications/) at the [Pittsburgh Supercomputing Center](http://www.psc.edu) in the [Mellon College of Science](https://www.cmu.edu/mcs/) at [Carnegie Mellon University](http://www.cmu.edu).')
file.close()
