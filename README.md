# pull-request-status
Simple API to return current status of the pull request


run the python file, `python pull_req_status.py` this will create a http server on localhost

`test`: running`127.0.0.1:9999` should return `Service is running`

please test the api using Postman.


##input type is json: 
input json should contain a url argument 
eg: {
"url":"github.com/user/repository-name"
}

output will be a json responce containing pull requests id's and statuses.


![github_sakthi](https://user-images.githubusercontent.com/16059874/42134167-d694749c-7d53-11e8-8417-b7928a8beb3f.PNG)
