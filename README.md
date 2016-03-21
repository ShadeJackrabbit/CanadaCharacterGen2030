# Canadian Pacific Northwest Character Generator circa 2030

A character generator for making random humans in the year 2030 in British Columbia, Canada

Most of the data used has been compiled from various Statistics Canada site, including directly taken from their site. I have extrapolated a lot of data to future values, using programs such as Wolfram Mathematica, and libraries like SciPy.

## Requirements
- Python 3.5
- NumPy 1.10.4

## Updates

### v0.6 - Synonym
- Transitioned away from a pure myers-briggs personality generation
- Generates four aspect descriptions based on synonym lists
- Lists sourced from 'a website'

The purpose of this update is to instead of simply generate a myers-briggs profile for each character, generate a single descriptor for each of the four elements of said profile, using a table of synonyms.

This is because in language, synonyms are never perfect matches. They have connotations and meanings implied via the cultural subtext the terms arrive from. Therefor there is almost more description in four simple words (each describing one of the four personality aspects) than there is in the profile returned from the myers-briggs matrix.

#### Current Issues
The old data is... perhaps over two years old? And I have no clue what half of it means. I have a lot of lists of numbers and stuff and I'm not really sure how accurate all of it is any more. I feel like it could be a good idea to reparse numbers and restate their sources

### v0.5.1
- Update to the layout of the generated character sheet
- Removed name generation until better system can be sorted out

### v0.5 - Precursor
- Did a ton of research
- Gathered data from online sources
- Parsed the data

Can generate characters with backgrounds, physical traits, personality traits, and names, all using projections of real-world data
