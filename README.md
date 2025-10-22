# FastAPI with Pydantic Examples

<img width="85" alt="map-user" src="https://img.shields.io/badge/views-254-green"> <img width="125" alt="map-user" src="https://img.shields.io/badge/unique visits-014-green">

[FastAPI](https://fastapi.tiangolo.com/) is a Python library and web framework designed for building APIs. It has the performance of comparable NodeJS and Go with the ease and familiarity of Python.

[Pydantic](https://docs.pydantic.dev/latest/) is a Python library used for data validation management.

FastAPI combined with Pydantic can be a great compromise between a light weight easy to build web framework that is still production ready.

This repository has a collection of examples that build on each other and add complexity. I put these examples together in a repository so I can have them as a reference and so other may benefit as well.

Below are the details of what is in each example
* [Example_1](https://github.com/ev2900/FastAPI_Pydantic_Examples/tree/main/Example_1) - Basic API routes
* [Example_2](https://github.com/ev2900/FastAPI_Pydantic_Examples/tree/main/Example_2) - Path Parameters / Data Validation with Type-Hints & Enums
* [Example_3](https://github.com/ev2900/FastAPI_Pydantic_Examples/tree/main/Example_3) - Model Classes and Nested Models
* [Example_4](https://github.com/ev2900/FastAPI_Pydantic_Examples/tree/main/Example_4) - URL Query Parameters for Filtering
* [Example_5](https://github.com/ev2900/FastAPI_Pydantic_Examples/tree/main/Example_5) - Request Body and POST requests + Pydantic pre-validators
* [Example_6](https://github.com/ev2900/FastAPI_Pydantic_Examples/tree/main/Example_6) - Annotated Type for Data Validation + Metadata

## Set Up
To run the examples you will need to install FastAPI, Pydantic and Uvicorn. I built these examples using Pydantic version ```2.11.7```, FastAPI version ```0.116.1``` and uvicorn version ```0.35.0```. You can install these via. the included [requirements.txt](https://github.com/ev2900/FastAPI_Pydantic_Examples/blob/main/requirements.txt).

Run ```pip install -r requirements.txt```

## Local FastAPI Web Server

The first few lines of each example python script have this information in comments. To run a local web server ```python -m uvicorn <name_of_file_with_out_file_extentions:app --reload```

You can then use [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to test your APIs. [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) can be a good place to check that the server is up and running and view the auto documentation that FastAPI creates.

## Unit Tests

For each example I created unit tests using [pytest](https://docs.pytest.org/en/stable/). You will see a file in each example named ```Test_<Name_of_Example>.py```. This file contains the unit tests for the example.

If you want to run the unit test you can issues the command ```python -m pytest```

If you are running on windows and you want to run all of the test scripts for every example you can optionally use the [run_all_unit_tests.ps1](https://github.com/ev2900/FastAPI_Pydantic_Examples/tree/main) powershell script.

In the future I will probably add a GitHub action to run these tests with each commit.
