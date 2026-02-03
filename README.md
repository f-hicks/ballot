# Ballot

Designed for [Southampton University Hillwalking Club](https://walking.susu.org) away trips.

It will work on any csv file where headers exist, and where there is at least one header that case insensitively contains the string "email". It uses python's built in `random.choice` to pseudorandomly pick an item from an iterable. This is repeated until enough participants have been chosen.

## Usage

Download the files by cloning this repository

Export a csv file containing the entires from the google sheets signup form

```bash
python ballot.py [csv filename] [number of spaces to allocate]
```

This will output two text files, `email_places.txt` and `email_not_places.txt`, which is in the correct format to be pasted into outlook / another email client for bulk emailing.
It will also output a csv file, `places.csv`, which is a subset of the input csv file only containing the personal details of those who have gotten a place on the trip.


