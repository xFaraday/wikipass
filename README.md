# Getting Wordlists from wikipedia
## Wikipedia API

Python3 has wikipedia package for the wikipedia API.  This allows for recursive querying of wikipedia.  Specifically the processing and storage of infinite tailored wordlists.

## Construction of a wordlist

When the program is run, it will prompt for a wikipedia search.  You can search for any term here and it will return a listing of possible matches.  On the selection of one of the matches it will serve as the "root node".  The root node defines the point in wikipedia in which the script will recursively index.

It might take longer than expected to generate a wordlist because at the time of writing this README.md, it attempts to remove most duplicate words before writing them to the file.  This is to reduce time when actually performing the password cracking.

## Use Case

The use case of this script is to generate custom wordlists for a specific target.

For example:
If the target in question has a pension for Dinosaurs or Western Movies, this script can be used to generate a wordlist from the wikipedia pages ofthat interest.  When combined with Hashcat rulesets it provides an effective strategy to crack passwords with a dictionary attack.

## Possible Errors

When selecting a root node, the program might exit unexpectedly.  This is because when grabbing links of the page, it depends on how well the page is maintained on the wikipedia side of things.  If the page is old or not maintained properly, the program will be unable to query recursively so it exits.
