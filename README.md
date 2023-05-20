AirBnB Clone - The Console

The console is the first segment of the AirBnB project at Holberton School, which covers fundamental concepts of higher-level programming. The goal of the AirBnB project is to deploy a server that serves as a simple copy of the AirBnB website (HBnB). In this segment, a command interpreter is created to manage objects for the AirBnB (HBnB) website.

Functionalities of this command interpreter:
- Create a new object (e.g., a new User or a new Place)
- Retrieve an object from a file, a database, etc.
- Perform operations on objects (count, compute stats, etc.)
- Update attributes of an object
- Destroy an object

Table of Contents:
1. Environment
2. Installation
3. File Descriptions
4. Usage
5. Examples of Use
6. Bugs
7. Authors
8. License

Environment:
This project is interpreted and tested on Ubuntu 14.04 LTS using Python 3 (version 3.4.3).

Installation:
1. Clone this repository: git clone "https://github.com/Andrews98-lab/AirBnB_clone.git"`
2. Access the AirBnb directory: `cd AirBnB_clone`
3. Run the console interactively: `./console` and enter commands
4. Run the console non-interactively: `echo "" | ./console.py`

File Descriptions:
- `console.py`: The console contains the entry point of the command interpreter. It supports the following commands:
  - `EOF`: Exits the console
  - `quit`: Exits the console
  - `create`: Creates a new instance of `BaseModel`, saves it to the JSON file, and prints the ID
  - `destroy`: Deletes an instance based on the class name and ID (saves the change into the JSON file)
  - `show`: Prints the string representation of an instance based on the class name and ID
  - `all`: Prints the string representation of all instances based on the class name or all instances
  - `update`: Updates an instance based on the class name and ID by adding or updating attributes (saves the change into the JSON file)

- `models/` directory contains classes used for this project:
  - `base_model.py`: The BaseModel class from which future classes will be derived. It has the following methods:
    - `__init__(self, *args, **kwargs)`: Initialization of the BaseModel
    - `__str__(self)`: String representation of the BaseModel class
    - `save(self)`: Updates the attribute `updated_at` with the current datetime
    - `to_dict(self)`: Returns a dictionary containing all keys/values of the instance

- Classes inherited from `BaseModel`:
  - `amenity.py`
  - `city.py`
  - `place.py`
  - `review.py`
  - `state.py`
  - `user.py`

- `models/engine` directory contains the `FileStorage` class that handles JSON serialization and deserialization:
  - `file_storage.py`: Serializes instances to a JSON file and deserializes back to instances. It has the following methods:
    - `all(self)`: Returns the dictionary `__objects`
    - `new(self, obj)`: Sets `obj` with key `.id` in `__objects`
    - `save(self)`: Serializes `__objects` to the JSON file (path: `__file_path`)
    - `reload(self)`: Deserializes the JSON file to `__objects`

- `tests/` directory contains all unit test cases

 for this project:
  - `test_models/test_base_model.py`: Contains the `TestBaseModel` and `TestBaseModelDocs` classes.
    - `TestBaseModelDocs` class includes the following test methods:
      - `setUpClass(cls)`: Set up for the doc tests
      - `test_pep8_conformance_base_model(self)`: Test that `models/base_model.py` conforms to PEP8
      - `test_pep8_conformance_test_base_model(self)`: Test that `tests/test_models/test_base_model.py` conforms to PEP8
      - `test_bm_module_docstring(self)`: Test for the `base_model.py` module docstring
      - `test_bm_class_docstring(self)`: Test for the `BaseModel` class docstring
      - `test_bm_func_docstrings(self)`: Test for the presence of docstrings in `BaseModel` methods

    - `TestBaseModel` class includes the following test methods:
      - `test_is_base_model(self)`: Test that the instantiation of a BaseModel works
      - `test_created_at_instantiation(self)`: Test that `created_at` is a public instance attribute of type `datetime`
      - `test_updated_at_instantiation(self)`: Test that `updated_at` is a public instance attribute of type `datetime`
      - `test_diff_datetime_objs(self)`: Test that two BaseModel instances have different datetime objects

  - `test_models/test_amenity.py`: Contains the `TestAmenityDocs` class.
    - `TestAmenityDocs` class includes the following test methods:
      - `setUpClass(cls)`: Set up for the doc tests
      - `test_pep8_conformance_amenity(self)`: Test that `models/amenity.py` conforms to PEP8
      - `test_pep8_conformance_test_amenity(self)`: Test that `tests/test_models/test_amenity.py` conforms to PEP8
      - `test_amenity_module_docstring(self)`: Test for the `amenity.py` module docstring
      - `test_amenity_class_docstring(self)`: Test for the `Amenity` class docstring

  - `test_models/test_city.py`: Contains the `TestCityDocs` class.
    - `TestCityDocs` class includes the following test methods:
      - `setUpClass(cls)`: Set up for the doc tests
      - `test_pep8_conformance_city(self)`: Test that `models/city.py` conforms to PEP8
      - `test_pep8_conformance_test_city(self)`: Test that `tests/test_models/test_city.py` conforms to PEP8
      - `test_city_module_docstring(self)`: Test for the `city.py` module docstring
      - `test_city_class_docstring(self)`: Test for the `City` class docstring

  - `test_models/test_file_storage.py`: Contains the `TestFileStorageDocs` class.
    - `TestFileStorageDocs` class includes the following test methods:
      - `setUpClass(cls)`: Set up for the doc tests
      - `test_pep8_conformance_file_storage(self)`: Test that `models/file_storage.py` conforms to PEP8
      - `test_pep8_conformance_test_file_storage(self)`: Test that `tests/test_models/test_file_storage.py` conforms to PEP8
      - `test_file_storage_module_docstring(self)`: Test for the `file_storage.py` module docstring
      - `test_file_storage_class_docstring(self)`: Test for the `FileStorage` class docstring

  - `test

_models/test_place.py`: Contains the `TestPlaceDocs` class.
    - `TestPlaceDocs` class includes the following test methods:
      - `setUpClass(cls)`: Set up for the doc tests
      - `test_pep8_conformance_place(self)`: Test that `models/place.py` conforms to PEP8
      - `test_pep8_conformance_test_place(self)`: Test that `tests/test_models/test_place.py` conforms to PEP8
      - `test_place_module_docstring(self)`: Test for the `place.py` module docstring
      - `test_place_class_docstring(self)`: Test for the `Place` class docstring

  - `test_models/test_review.py`: Contains the `TestReviewDocs` class.
    - `TestReviewDocs` class includes the following test methods:
      - `setUpClass(cls)`: Set up for the doc tests
      - `test_pep8_conformance_review(self)`: Test that `models/review.py` conforms to PEP8
      - `test_pep8_conformance_test_review(self)`: Test that `tests/test_models/test_review.py` conforms to PEP8
      - `test_review_module_docstring(self)`: Test for the `review.py` module docstring
      - `test_review_class_docstring(self)`: Test for the `Review` class docstring

  - `test_models/test_state.py`: Contains the `TestStateDocs` class.
    - `TestStateDocs` class includes the following test methods:
      - `setUpClass(cls)`: Set up for the doc tests
      - `test_pep8_conformance_state(self)`: Test that `models/state.py` conforms to PEP8
      - `test_pep8_conformance_test_state(self)`: Test that `tests/test_models/test_state.py` conforms to PEP8
      - `test_state_module_docstring(self)`: Test for the `state.py` module docstring
      - `test_state_class_docstring(self)`: Test for the `State` class docstring

  - `test_models/test_user.py`: Contains the `TestUserDocs` class.
    - `TestUserDocs` class includes the following test methods:
      - `setUpClass(cls)`: Set up for the doc tests
      - `test_pep8_conformance_user(self)`: Test that `models/user.py` conforms to PEP8
      - `test_pep8_conformance_test_user(self)`: Test that `tests/test_models/test_user.py` conforms to PEP8
      - `test_user_module_docstring(self)`: Test for the `user.py` module docstring
      - `test_user_class_docstring(self)`: Test for the `User` class docstring

Examples of use:
```
vagrantAirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help ):
EOF  all  create  destroy  help  quit  show  update

(hbnb) all
MyModel ** class doesn't exist **
(hbnb) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) all
BaseModel [[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 
