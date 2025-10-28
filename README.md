# MLPractice
This is a example using Selenium webdriver with python
If you want to run this example, you must have Python and pytest properly installed, and add to the "conftest" Python file the route of your driver. Here are some instructions to run this project porperly.

If you plan to run this using the command console, please make sure to create a folder to store all the files and access that folder using the command console. Once there, just write the command <<pytest -v -s>> to see all the prints and the Test case properly.

This project was designed to run on Chrome by default, but you can run it in Mozilla Firefox using the following command on the console: <<tests/test_MercadoLibre.py --browserName firefox>>, but you need to update the localization of the driver file.
