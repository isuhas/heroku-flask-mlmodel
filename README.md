# heroku-flask-mlmodel
https://iris-test1.herokuapp.com/predict?sepal_length=7.3&amp;sepal_width=2.9&amp;petal_length=6.3&amp;petal_width=2.0
https://iris-test1.herokuapp.com/

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
https://dashboard.heroku.com/apps/iris-test1/deploy/heroku-git

Install the Heroku CLI
Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

$ heroku login
Clone the repository
Use Git to clone iris-test1's source code to your local machine.

$ heroku git:clone -a iris-test1
$ cd iris-test1
Deploy your changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.

$ git add .
$ git commit -am "make it better"
$ git push heroku master

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

References:
http://blog.socratesk.com/blog/2018/01/29/expose-ML-model-as-REST-API

https://xcitech.github.io/tutorials/heroku_tutorial/

https://iamalivingcontradiction.wordpress.com/2015/11/17/how-to-build-a-prediction-api-in-10-minutes-with-flask-swagger-and-scipy/

https://www.patricksoftwareblog.com/steps-for-starting-a-new-flask-project-using-python3/


-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

Notes:

Copy-paste and create new requirements.txt file from auto generated requirements.txt
