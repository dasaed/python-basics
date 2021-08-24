# flask
Flask is a useful library for building Python websites. 
It's a light-weight package, and may not be as powerful as django, but for "on-the-go" sort of projects, it can be very useful.
Some important notes about flask:
  * flask uses jinja to parse python code into html templates


## Folder Structure
```commandline
.
├── Pipfile                 # Resources
├── Pipfile.lock            # Packages for working project
├── README.md               # This file
└── web_app_1               # Web application contents (the sample project)
    ├── main.py             # What runs the application server
    └── website             # For website contents
        ├── __init__.py     # Allows us to conver this folder into a python package
        ├── auth.py         # For authentication
        ├── models.py       # 
        ├── static          # For static content, such as images, videos, even some JavaScript, etc.
        ├── templates       # For the HTML content that will be dynamically loaded on our pages. 
        |                   # Useful for headers, footers, and other website-like elements
        └── views.py        # Main views, or URLs endpoints, for the front-end of the website
```

## Setup
```commandline
pipenv install
```

## Run the webserver
```commandline
pipenv shell
python main.py
```

## Credits
Based on this **[tutorial](https://www.youtube.com/watch?v=dam0GPOAvVI)**