# REST API for retrieving the most frequent queries during a specific time range.

## Description
This API provides endpoints to retrieve the most frequent queries within a specified time range. Two different implementations, one using pandas and the other using sets, are provided in this repository.

## My Thought Process
Since this is the first time I am working on a Python project, I needed to understand how to tackle the two biggest challenges of this problem statement which are:
- to parse a large dataset
- to use an efficient data structure 

#### Using Sets
While learning about the different data structures in Python, the ones that seemed to be appropriate to be considered were:
- nested lists (outer list acts as rows and the inner list as columns)
- nested tuples
- list of tuples
- dictionaries
- sets

Sets seemed to fit perfectly to solve this problem statement because of the following reasons:
- Lists allow duplicate elements to be present. Hence, an additional logic would be required to filter out all the duplicates.
- Tuples are immutable. Hence, elements could not be added or removed.
- Dictionaries can handle the problem of duplicate elements using a key. However, every key needs to have a value, which in this case is redundant and consumes extra space.

Hence, a set is the perfect choice for this challenge which can handle duplicates on its own, is mutable, and also doesn't use redundant memory. It also has an O(1) time complexity for any operation like insertion or deletion, since it uses a hashtable as its underlying data structure.

#### Using the Pandas library
Since the dataset is basically in the form of a 2D array, the Pandas dataframe is another excellent choice of data structure to solve this challenge. 

## Run the program
To run this program, follow the instructions below.

1. Install Flask is not already present using this command.

        pip3 install Flask   

2. Install the pandas library if not already present using this command.
  
         pip3 install pandas

3. Clone the contents of this repository into a new folder. Make sure to have the file ```hn_logs.tsv``` in the same root folder as that of the contents of this repository.

4. To run the server
    Open a new terminal and run the following command.
    #### Using sets
        python3 main_sets.py
    #### Using dataframes
        python3 main_pandas.py

    The server must be up and running on port 5000 by default.

5. To run the test file, edit the value of the variable ```TIMESTAMP``` in the file ```test.py``` with a choice of your own. To test the algorithm using dataframes or sets, uncomment the corresponding line in the file ```test.py```.


## Challenges I ran into
- I started delving deep into using the concept of pagination in REST APIs only to realize that it is unnecessary for this problem statement.
- I strongly considered using dictionaries since I had not researched about sets back then, and then ran into the problem of giving redundant values to every unique key.

## Future Scope
I want to add another feature where an additional parameter containing another timestamp can be given optionally, to retrieve the most frequent queries in the duration from one timestamp to the other. However, this feature, as of now, works only when both the timestamps passed are in the format ```yyyy-mm-dd hh:mm: ss```.
I want to develop this application further to accept both timestamps in any format.

## References
- https://saturncloud.io/blog/how-to-efficiently-read-large-csv-files-in-python-pandas/
- https://www.youtube.com/watch?v=MbslvX0AMVE
- https://codedamn.com/news/backend/rest-api-pagination-handling-large-data-sets
- https://saturncloud.io/blog/converting-object-column-in-pandas-dataframe-to-datetime-a-data-scientists-guide/#:~:text=To%20convert%20an%20object%20column,object%20column%20containing%20date%20strings.&text=As%20you%20can%20see%2C%20the,is%20now%20in%20datetime%20format
- https://www.youtube.com/watch?v=Lw2rlcxScZY
- https://stackoverflow.com/questions/14032066/can-flask-have-optional-url-parameters
