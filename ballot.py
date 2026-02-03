import argparse
import random
import csv

def main(filename: str, num_places: int) -> None:
    with open(filename, "r") as f:
        reader = csv.reader(f)
        header = ""
        entries = []
        
        # get the header row and all other rows separately
        for line in reader:
            if reader.line_num== 1:
                header = line
            else:
                entries.append(line)
        
        # get the index of the first header column that contains the word email
        email_row_index = header.index([ i for i in header if "email" in i.lower() ][0])
                        
        # use `random.choice` to pick `num_places` random items from the entries.
        # add them to the places list and remove them from the unselected pool.
        places: list[list[str]] = []
        for i in range(num_places):
            places.append(random.choice(entries))
            entries.remove(places[-1])
        
        # get just the email address' for easy pasting into outlook
        places_  = [i[email_row_index].replace("\"", "").replace(" ", "") for i in places]
        entries_ = [i[email_row_index].replace("\"", "").replace(" ", "") for i in entries]
        
        # output email address to files
        with open("email_places.txt", "w") as p:
            p.write("; ".join(places_))
        
        with open("email_not_places.txt", "w") as p:
            p.write("; ".join(entries_))
        
        # output all details to files
        with open("places.csv", "w") as p:
            p.write("\n".join([",".join(i) for i in places]))
            

if __name__ == "__main__":
    # parse args to determine filename of csv file and number of places
    # if arguments aren't passed in then prompt user to input them.
    parser = argparse.ArgumentParser(description="Perform a ballot to decide who gets on the trip", add_help=False)
    parser.add_argument("filename", nargs="?", type=str, help="The filename of the csv file exported from google sheets")
    parser.add_argument("places", nargs="?", type=int, help="The nunber of places to allocate to people")
    
    args, _ = parser.parse_known_args()
        
    args = [args.filename, args.places]
    if args[0] is None:
        args[0] = input("Please enter the filename of the csv file downloaded from google sheets > ")
    if args[1] is None:
        args[1] = int(input("Please enter the number of spaces available > "))
        
    main(args[0], args[1])