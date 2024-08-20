# preparing data Pipeline: Exploratory Data Analysis

*Last update: 14/08/2024*

The present notebook introduces the current model operationalized in the machine learning pipeline. In addition, it illustrates some of the functions to load the data, then has a rapid exploratory data analysis, a review about the features generation, and how the model was fit.

The machine learning task in the project, as described in the [README](https://github.com/shreyashankar/toy-ml-pipeline#ML-task-description-and-evaluation-procedure), is: 

 > *We train* ***a model to predict whether a passenger in a NYC taxicab ride will give the driver a large tip***. *This is a binary classification task. A large tip is arbitrarily defined as greater than 20% of the total fare (before tip).* ***To evaluate the model or measure the efficacy of the model, we measure the F1 score.***
 
 ## Loading the data from the source

Loading data from the sources to ingest it into local S3 bucket (minio) after cleaning it and preparing it for the model.


## Different data exporters
if you need to send cleaned data into different sources other than minio you can adjust `io_config.yaml` file with appropriate s3 `AWS_REGION`, `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` key in case if the bucket if private.

