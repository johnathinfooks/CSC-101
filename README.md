# Dangerous Activity Analysis and Flagging Tool

## Information

Johnathin Fooks <br>
Vincent Le <br>

Final project for CSC-101 at California Polytechnic State University under Professor Anita Rathi.

## Functionality and Use

### Dataset Generation
To create a dataset, run the `data/dataGen/dataGen.py` file. <br>
It will prompt multiple parameters regarding the dataset. Fill out accordingly. This will make a dataset in json formatting with random values within the parameters set.

### Dataset Analysis
To analyze a dataset, run the `main.py` file. <br>
Use `main.py help` for help to use the tool. <br>

### Overview of Valid Operations
```
Valid input:

help - access help information
info - access general information
list - list datasets
analysis <dataset name> <output file name> <max dangerous> - show all users that are flagged as dangerous according to prompted value
```

### Analysis
This will create a file in `results/` that contains the output of the analysis. <br>
- `<dataset name>` is the name of the dataset to be analyzed. Use `list` to get valid dataset options. <br>
- `<output file name>` is the name of the output file (.txt file) that contains the analysis results. This file will be in `results/`. <br>
- `<max dangerous>` is an integer value that is how many dangerous words are allowed for the user to be flagged. For example: if it is 3 then 3 dangerous words are allowed; a user with 4 dangerous words would be flagged.

### Program Design Details
- Consistent and mindful error handling and function layout; organized and intuitive.
- Custom `p_err` functon for intuitive and consistent error printing. Helpful during development process.
- Attempt at intuitive classes to make foundamental analysis logic easy and expandable.
- Expandable operation handling; easy to add functionality in the future.

## Closing comments
We are proud of this project due to the fact that this class is our first exposure to Python and our around week and a half timeline to complete it. While AI and external tools were used to develop this project, every line of the repository was first understood and then written by us. Anyone interested in continuing this project would be intereseted in flagging users who send too many messages that are within a timestamp too close to eachother (spam checking). Thank you professor Anita Rathi for a pleasant and informative quarter in CSC-101.
