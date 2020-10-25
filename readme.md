# Text Analyser

A text analysis and plotting tool

## Credits

Project under IIT Mandi Course - CS308, The project was realised with due regards to the following contributors:

1. Dipanshu Verma (B18054)
2. Ayushman (B18164)
3. Ujjwal Soni (B18031)
4. Bhumanyu Goyal (B18012)
5. Harish Jaglan (B18115)

The team was further subdivided to work under following branches:

1. API - Dipanshu
2. Frontend - Harish and Ujjwal
3. Backend - Bhumanyu and Ayushman

## Documentation

For detailed documentation of API refer **`documentationAPI.md`** under **`docs/`** subfolder
In a nutshell the role of each file is as follows:

1. **API**
    - Creating a link between frontend and backend designs
    - Creation of easy to use pre defined functionalities readily available for carrying out complex pieces of codes or their combinations
    - Helping to make code easier to understand. The API itself being a pool of functions helps to reduce the clutter in backend and frontend which can readily import these functionalities

2. **Frontend**
    - For detailed documentation of frontend refer **`documentation_frontend.md`** under **`docs/`** subfolder
    - Enabling the user to easily surf through the rich array of functionalities provided by the backend and API
    - Tinker based easy to understand and implement bug free Graphical User Interface.
    - Two different tabs for:
        - To view quick analysis of data along with graphs
        - To view the lines containing required words list passed by the user

3. **Backend**
    - To implement the structure and handling of events under the action of user interacting with the Frontend.
    - To enable features such as BROWSE, FETCH and so on built upon the functionalities provided in the API.

## Usage

To run the application the user has to execute the gui.py. This can be done using the following command

```bash
python3 ./gui.py
```
-----------
**(Optional)**

The application comes with a pre-installed python3 environment which can be made use of to avoid library conflicts. To run the appliaction under the environment run the following piece of code

```
source ./env/bin/activate
python3 gui.py
```

After running the application. The environment can be deactivated using ```deactivate ```

---------

Once the Application is active further refer to ```design.md``` under wiki section or under ```docs/``` subfolder for understanding the GUI interaction.

## TechStack and Requirements

In order to make use of the application, you must have the latest tinker for python3 installed on your machines.
In order to meet all other python3 dependency requirements run the following segment of code

```
pip install requirements.txt
```
-------------------------------------------------------

**(Optional)**

The application comes with a pre-installed python3 environment which can be made use of to avoid library conflicts. To run the appliaction under the environment run the following piece of code

```
source ./env/bin/activate
python3 gui.py
```

After running the application. The environment can be deactivated using ```deactivate ```

--------------------------------------------------------
