# Open Nofity APIs


APIs for [api.open-notify.org](http://api.open-notify.org)


## Install for the first time:

Make sure you have some packages:

    # apt-get install python python-dev python-pip virtualenvwrapper redis-server

Note: if you're installing `virtualenvwrapper` for the first time, be sure to log out and back in before continuing.

Create a virtual environment

    $ mkvirtualenv opennotify
    (opennotify)$ pip install -r requirements.txt

Get data

    (opennotify)$ python update.py


## Run locally:

Start virtual environment

    $ workon opennotify

Run with [foreman](https://github.com/ddollar/foreman) using dev procfile:

    (opennotify)$ foreman start -f Procfile.dev

Open a browser to [localhost:5000](http://localhost:5000).


## Run Testsuite

    (opennotify)$ cd testsuite
    (opennotify)$ pip install -r requirements.txt
    (opennotify)$ cd ..
    (opennotify)$ make test


## API Documentation

Docs are in the gh-pages branch, or on the web here:

 - [Open Notify API Documentation](http://open-notify.org/Open-Notify-API/)


## Modifications from original source code:

* Updated from Python v2.7 to v3.6
* Changed data source from NASA to Celestrak to simplify parsing
* Deployed using https to allow integration with other https sites. Modern browsers will block a mixed content request (i.e. request to http from https).

## Heroku Deployment

To deploy to heroku:

* Create a Heroku app and push the code
* Provision redis add-on
* Modify the name of the Redis URL environmental variable from REDIS_URL to REDISTOGO_URL
* Provision scheduler add-on
* Create a daily recurring task: `$python update.py`


## License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
