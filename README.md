# Ballot

Designed for [Southampton University Hillwalking Club](https://walking.susu.org) away trips.



## Usage

Download the files by cloning this repository

Export a csv file containing the entires from the google sheets signup form

```bash
python ballot.py [csv filename] [number of spaces to allocate]
```

This will output two text files, `places.txt` and `not_places.txt`, which is in the correct format to be pasted into outlook for bulk emailing.

