# Ariel Zeto's Data Engineering Test

# Note: There are two versions of the data pipeline (and tests). One is written in Pandas, the other using Python's built-in CSV library. Feel free to look at either, or both!

There are two versions (CSV library, pandas library) I completed for this test to showcase my ability to work with Python libraries.

**Version 1:** There is `data_pipeline.py` & `test_data_pipeline.py` - these utilized the .CSV library of Python. The output when running the pipeline here creates the `applied_changes_data.py`.

**Version 2:** There is `data_pipeline_pandas.py` & `test_data_pipeline_pandas.py` - these utilize the Pandas library of Python. The output when runing the pipeline here creates the `applied_changes_data_panda.csv` file, consisting of transformations and validation.

The CSV library data_pipeline (and its unit tests) was built first, then I created a Pandas library version (and its unit tests) second. I did not have much at all exposure to Pandas, so this was a great experience to utilize my skillset and apply myself to understand the powerful and much utilized library within the industry.

I plan to complete an online Pandas course prior to the next interview round so that I may become more knowledgeable in it.

## Introduction:

This repository contains Ariel Zeto's Data Engineering test for ChowaCo.
The test itself necessitates that a data pipeline is applied. Such data pipeline must be written utilizing Python. Additionally, the data pipeline must process and read a .CSV file, apply transformations, check for validations, contain unit tests, and load all data transformations into a new dataset, such as a SQLite database or .CSV file - in this case, a .CSV file.

## Objective:

To design a data pipeline that processes a dataset, applies transformations, and loads it into a mock data warehouse, in this case, a new .csv file with all the validation and transformations applied.

## Dataset:

The dataset provided is labeled as `data.csv`, included within the repo. See below for where the dataset was located, and reasons for selecting the dataset.

The dataset provided for this Data Engineering test a large .CSV file, via **Kaggle**.
For all intents and purposes of this exam, I looked for a dataset that contains highly valuable data, attributes, and factors regarding the housing market in Ames, Iowa (US).
The data set is massive in scope, and contains some key points that need validation, as well as transformations, such as empty/missing values in cells, leading zeroes (when len(digit) > 1, as there do exist original 0 worthy cell values), combining of some columns and handling it as one (Date sold).

Link to the where you may find the .CSV file. [Ames Housing Dataset, via Kaggle](https://www.kaggle.com/datasets/shashanknecrothapa/ames-housing-dataset/data)

## Requirements:

- Data pipeline to be written in Python
- Implement data validation (such as checking for missing values)
- Transform data (such as removing trailing zeroes, filling empty cells, combination of columns, removal of whitespace, etc)
- Unit Tests (also written in Python)
- Consistent naming conventions, such as snake_case
- Data pipeline to be called `data_pipeline.py` (However, I also wrote a `data_pipeline_pandas.py` version too).
- Unit testing to be called `test_data_pipeline.py` (however, I also wrote a `test_data_pipeline_pandas.py` version too)
- Every transformation to be written to a new mock data warehouse, such as a SQL database or new .CSV file (.CSV file chosen for this test)

## Design Decisions:

For this test, I wanted to locate a dataset that had applicable usecases - one that impacts everybody...the housing market - in this case, within Ames, Iowa (USA).
The following dataset is utilized for regression tasks, such as predicting housing prices.
Additionally, there are alphanumeric values for a large variety of factors, making this data set very applicable for prediciton models (and those generally just interested in data)!
This dataset was selected for various reasons.

- The dataset is massive, showcasing the ability that I have to work with files big (or small).
- I wanted to work with a .CSV file that contained missing data, such that I could verify that I can write python scripts working with large data and optimize them.
- The file contained some errors, such as leading zeroes for large numeric values, such example, the `PID` category. Such leading zeroes add to clutter, and I wanted to remove them (except in the instance of cells where `0` is the actual value).
- To test my ability looping through every row of data, to determine if there exist duplicate rows, and how to handle and optimize said data (however, the pandas version utilizes `Dataframes`, removing the necessity of looping as it is taken care of).
- Ability to remove whitespace within individual cells (which would be inconsistent otherwise)

The `data_pipeline.py` simply relies on the `csv` library, built within Python's library.
The `test_data_pipeline.py` file simply relies on the `unittest` and `random` modules, both of which are also built within the standard Python library.
Its testing file, `test_data_pipeline_pandas.py`, relies on unit testing, in addition to pandas testing framework.

As mentioned, I wanted to gain exposure with Pandas, and therefore wrote a pipeline `data_pipeline_pandas.py` and its tests utilizing the Pandas library, these being `data_pipeline_pandas.py`.

The `random` library is utilized within the `test_csv_read` (first unit test). Rather than reading every single data point of the massive .CSV file, it utilizes a random seed of fifty, each time. These randomly selected rows are then compared with columns in the row(s) selected.

## Evaluation of data_pipeline.py & test_data_pipeline.py:

### Regarding `data_pipeline.py`

Within `data_pipeliine.py`, there is a `main` function that makes the required callings to the written functions. Simply run this file, and `main()` will be called, which will output a new .CSV file, `applied_changes_data.csv`.

### Regarding `test_data_pipeline.py`

This file contains several unit tests. The unit test corresponds to the functions written in `data_pipeline.py`.
The unit tests call the functions, and utilize `assert` operators in order to validate that the functions work as desired.

Unit Tests were selected due to their standard implementation of Python.

At the bottom of this README, **I have provided instructions on how to run the unit tests.**

### The Outcome (CSV Library version):

By running `data_pipeline.py`, the transformed and validated data will write a new .CSV fle, labeled `applied_changes_data.csv`.
By running the unit tests, you'll notice that `test_write_data.csv` is written. This is normal. You may disregard this file, it is simply created (and based off of the changes) to simply ensure that the function that writes the final .CSV works as intended. Note: This does not occur with the Pandas version of the tests, to avoid redundancy.

## There's a `test_write_data.csv` that is made when executing the unit tests based off of the CSV library version, why?:

This is to ensure that the function actually writes a new CSV file, granted, it will be based off of the original data set, given that it does not utilize the transformations.

## Evaluation of data_pipeline_pandas.py & test_data_pipeline_pandas.py:

### Regarding `data_pipeline_pandas.py`

Within `data_pipeliine_pandas.py`, there is a main function that makes the required callings to the written functions. Simply run this file, and `main()` will be called, which will output a new .CSV file, `applied_changes_data_pandas.csv`.

### Regarding `test_data_pipeline_pandas.py`

This file contains several unit tests. The unit test corresponds to the functions written in `data_pipeline_pandas.py`. The unit tests call the functions, and utilize assert operators in order to validate that the functions work as desired.

### The Outcome (Pandas Library version):

By runing `data_pipeline_pandas.py`, the transformed and validated data will write a new .CSV file, labeled `applied_changes_data_panda.csv`. There are several tests for `test_data_pipeline_pandas.py`, however, unlike the pipeline written using Python's .CSV library, it does **not** write a file (to avoid redundacy). Additionally, the unit tests have been slightly altered.

## Questions?:

Feel free to contact me! I am more than happy to help with running and executing the pipeline if there are any concerns.

## How to run the tests corresponding to `test_data_pipeline.py`:

The tests are written utilizing Python's included Unit Testing framework.
Within the directory of where `test_data_pipeline.py` (and `data_pipeline.py`), simply open a new terminal instance in your favorite IDE of choice, and paste the following command.

`python3 -m unittest test_data_pipeline.py`

## How to run the tests corresponding to `test_data_pipeline_pandas.py`:

Similar to running the unit tests for the data pipeline written using the .CSV library, the tests written for the pandas version of the pipeline can be called within the terminal by running:

`python3 -m unittest test_data_pipeline_pandas.py`
