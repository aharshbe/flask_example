# Flask_Example
## Currently under construction!
`(feel free to browse anyway)`
### Usage:
* `python flasktest.py`
* go to `http://127.0.0.1:5000/`
  * Route options:
    * `/hello/<user>` displays a variable that's passed: example `http://127.0.0.1:5000/hello/austin`
    * `/score/<int:score>` evaluates an int that is passed and displays a result, pass if >= 10 (refer to `templates/score.html`) or fail if it's not: example `http://127.0.0.1:5000/score/5`
    * `/table` which outputs a dictionary as a table: example `http://127.0.0.1:5000/table`
      * Fill the table on line 15 in `flasktest.py`
#### Author:
* Austin Harshberger
