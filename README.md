# Jinka Scraper

## Getting started

- Install dependencies
- > pip3 install --r requirements/global.txt

## How to use the app

```
./main.py --alert_id=<alert_id> --authentication_token=<authentication_token>

# Example
## alert_id=2306da5e990d75bb2e00a0ea2381f63c
## authentication_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OTMzMzgxLCJlbWFpbCI6ImFudG9ueS52ZW9wYXNldXRoQGVwZmVkdS5mciIsImNyZWF0ZWRfYXQiOiIyMDIzLTAxLTIyVDA5OjMzOjUzLjAwMFoiLCJpYXQiOjE2NzQzODQ1NjIsImV4cCI6MTY3Njk3NjU2Mn0.iAcn9knYNqxVPsM-lxUVqThS5rLzIjDwnohNVrn5OeI
```

## Where to get the alert_id

> Go to https://www.jinka.fr/
> Login with your credentials
> Get redirected to: https://www.jinka.fr/asrenter/alert/dashboard/<alert_id>?filter=all&page=3&sorting=
> See the alert_id in the URL

## Where to get the authentication_token

> Go to https://www.jinka.fr/
> Login with your credentials
> Get redirected to: https://www.jinka.fr/asrenter/alert/dashboard/<alert_id>?filter=all&page=3&sorting=
> Open chrome's dev tools with Cmd+Otion+I
> Go to Application tab
> Open the cookie
> Get the value from LA_API_TOKEN

