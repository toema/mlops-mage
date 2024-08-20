

## About

This is a project example of a standalone ML pipeline written **entirely** in Python with orchestration in mage. 


## Getting started

This mage project is broken down into several pipelines, described in a high level by the directories in this repository.

All Python dependencies and virtual environment creation is handled by the mage docker image ..

1. Launch Mage and the database service (PostgreSQL):

   ```
   ./start.sh
   ```

2. Open [`http://localhost:6789`](http://localhost:6789) in your browser.

## ML task description and evaluation procedure

We train a model to predict whether a passenger in a NYC taxicab ride will give the driver a large tip. This is a **binary classification task.** A large tip is arbitrarily defined as greater than 20% of the total fare (before tip). To evaluate the model or measure the efficacy of the model, we measure the [**F1 score**](https://en.wikipedia.org/wiki/F-score).

The current best model is an instance of `sklearn.ensemble.RandomForestClassifier` with `max_depth` of 10 and other default parameters. The test set F1 score is 0.716. I explored this toy task earlier in my [debugging ML talk](https://github.com/shreyashankar/debugging-ml-talk).

## Dataset description

We use the yellow taxicab trip records from the NYC Taxi & Limousine Comission [public dataset](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page), which is stored in a public aws S3 bucket. The data dictionary can be found [here](https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf) and is also shown below:

| Field Name      | Description |
| ----------- | ----------- |
| VendorID      | A code indicating the LPEP provider that provided the record. 1= Creative Mobile Technologies, LLC; 2= VeriFone Inc.       |
| lpep_pickup_datetime   | The date and time when the meter was engaged.        |
| lpep_dropoff_datetime   | The date and time when the meter was disengaged.        |
| Passenger_count   | The number of passengers in the vehicle. This is a driver-entered value.      |
| Trip_distance   | The elapsed trip distance in miles reported by the taximeter.      |
| PULocationID   | TLC Taxi Zone in which the taximeter was engaged.      |
| DOLocationID   | TLC Taxi Zone in which the taximeter was disengaged      |
| RateCodeID   | The final rate code in effect at the end of the trip. 1= Standard rate, 2=JFK, 3=Newark, 4=Nassau or Westchester, 5=Negotiated fare, 6=Group ride     |
| Store_and_fwd_flag | This flag indicates whether the trip record was held in vehicle memory before sending to the vendor, aka “store and forward,” because the vehicle did not have a connection to the server. Y= store and forward trip, N= not a store and forward trip |
| Payment_type | A numeric code signifying how the passenger paid for the trip. 1= Credit card, 2= Cash, 3= No charge, 4= Dispute, 5= Unknown, 6= Voided trip |
| Fare_amount | The time-and-distance fare calculated by the meter. | 
| Extra | Miscellaneous extras and surcharges. Currently, this only includes the $0.50 and $1 rush hour and overnight charges. |
| MTA_tax | $0.50 MTA tax that is automatically triggered based on the metered rate in use. | 
| Improvement_surcharge | $0.30 improvement surcharge assessed trips at the flag drop. The improvement surcharge began being levied in 2015. | 
| Tip_amount | Tip amount – This field is automatically populated for credit card tips. Cash tips are not included. | 
| Tolls_amount | Total amount of all tolls paid in trip. | 
| Total_amount | The total amount charged to passengers. Does not include cash tips. |

## Loading the data from the source

Loading data from the sources to ingest it into local S3 bucket (minio) after cleaning it and preparing it for the model.

## Different data exporters
if you need to send cleaned data into different sources other than minio you can adjust `io_config.yaml` file with appropriate s3 `AWS_REGION`, `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` key in case if the bucket if private.

## Repository structure

The `last_project` contains multiple pipelines, each organized into the following high-level subdirectories:

* `preparing_data`
* `automatic_retraining`
* `predict`
* `sklearn_training`
* `xgboost_training`
* `deploying_to_production`

### Pipeline components

Any applied ML pipeline is essentially a series of functions applied one after the other, such as data transformations, models, and output transformations. This pipeline was initially built in a lightweight fashion to run on a regular laptop with around 8 GB of RAM. *The logic in these components is a first pass; there is a lot of room to improve.*

The following table describes the components of this pipeline, in order:

_Running the Docker image: `./start.sh`._


### Data storage

The inputs and outputs for the pipeline components, as well as other artifacts, are stored in a public S3 bucket named `taxi` located in `minio`. Read access is universal and doesn't require special permissions. Write access is limited to those with credentials. If you are interested in contributing and want write access, please contact me directly describing how you would like to be involved, and I can send you keys. 


If you have write permissions, store your keys/ids in an `io_config.yaml` file and export them as environment variables. If you do not have write permissions, you will run into an error if you try to write to the S3 bucket.

## Utils documentation

The `utils` directory contains helper functions and abstractions for expanding upon the current pipeline. Tests are in `utils/tests.py`. Note that only the `io` functions are tested as of now.


## Contributing

Having a toy example of an ML pipeline isn't just nice to have for people experimenting with MLOps tools. ML beginners or data science enthusiasts looking to understand how to build pipelines around ML models can also benefit from this repository.

Anyone is welcome to contribute, and your contribution is greatly appreciated! Feel free to either create issues or pull requests to address issues.

1. Fork the repo
2. Create your branch (`git checkout -b YOUR_GITHUB_USERNAME/somefeature`)
3. Make changes and add files to the commit (`git add .`)
3. Commit your changes (`git commit -m 'Add something'`)
4. Push to your branch (`git push origin YOUR_GITHUB_USERNAME/somefeature`)
5. Make a pull request

## Contact

Original author: [Toema](https://www.linkedin.com/in/mohamed-toema/)

Email: m.toema20@gmail.com

