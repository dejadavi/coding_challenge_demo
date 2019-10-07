
# Coding Challenge



## Indices

* [Default](#default)

  * [App GitHub BitBucket Profile](#1-app-github-bitbucket-profile)
  * [App GitHub Profile](#2-app-github-profile)
  * [App Health Check](#3-app-health-check)


--------


## Default



### 1. App GitHub BitBucket Profile


Get a summary profile of an organization's bitbucket repos


***Endpoint:***

```bash
Method: GET
Type: RAW
URL: http://127.0.0.1:8080/github/mailchimp
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Content-Type | application/json |  |



***Responses:***


Status: App GitHub BitBucket Profile - Mailchimp | Code: 200



```js
{
    "orgname": "mailchimp",
    "repo_count": 10,
    "repos": [
        {
            "has_issues": false,
            "is_private": false,
            "language": "php",
            "name": "mandrill-api-php",
            "scm": "git",
            "website": "http://mandrillapp.com/api/docs/"
        },
        {
            "has_issues": false,
            "is_private": false,
            "language": "python",
            "name": "mandrill-api-python",
            "scm": "git",
            "website": "http://mandrillapp.com/api/docs/"
        },
        {
            "has_issues": false,
            "is_private": false,
            "language": "javascript",
            "name": "mandrill-api-js",
            "scm": "git",
            "website": "http://mandrillapp.com/api/docs/"
        },
        {
            "has_issues": false,
            "is_private": false,
            "language": "ruby",
            "name": "mandrill-api-ruby",
            "scm": "git",
            "website": "https://mandrillapp.com/api/docs/"
        },
        {
            "has_issues": false,
            "is_private": false,
            "language": "javascript",
            "name": "mailchimp-api-node",
            "scm": "git",
            "website": "http://apidocs.mailchimp.com/api/2.0/"
        },
        {
            "has_issues": false,
            "is_private": false,
            "language": "php",
            "name": "mailchimp-api-php",
            "scm": "git",
            "website": "http://apidocs.mailchimp.com/api/2.0/"
        },
        {
            "has_issues": false,
            "is_private": false,
            "language": "python",
            "name": "mailchimp-api-python",
            "scm": "git",
            "website": "http://apidocs.mailchimp.com/api/2.0/"
        },
        {
            "has_issues": false,
            "is_private": false,
            "language": "ruby",
            "name": "mailchimp-api-ruby",
            "scm": "git",
            "website": "http://apidocs.mailchimp.com/api/2.0/"
        },
        {
            "has_issues": false,
            "is_private": false,
            "language": "dart",
            "name": "mandrill-api-dart",
            "scm": "git",
            "website": "https://mandrillapp.com/api/docs/index.dart.html"
        },
        {
            "has_issues": false,
            "is_private": false,
            "language": "javascript",
            "name": "mandrill-api-node",
            "scm": "git",
            "website": "https://mandrillapp.com/api/docs/index.nodejs.html"
        }
    ]
}
```



### 2. App GitHub Profile


Get a summary profile of an organization's github repos


***Endpoint:***

```bash
Method: GET
Type: RAW
URL: http://127.0.0.1:8080/github/mailchimp
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Content-Type | application/json |  |



***Responses:***


Status: App GitHub Profile - Mailchimp | Code: 200



```js
{
    "orgname": "mailchimp",
    "repo_count": 19,
    "repos": [
        {
            "full_name": "mailchimp/APIv3-examples",
            "private": false,
            "watchers_count": 83
        },
        {
            "full_name": "mailchimp/auto-value-gson",
            "private": false,
            "watchers_count": 0
        },
        {
            "full_name": "mailchimp/ChimpKit2",
            "private": false,
            "watchers_count": 29
        },
        {
            "full_name": "mailchimp/ChimpKit3",
            "private": false,
            "watchers_count": 52
        },
        {
            "full_name": "mailchimp/content-style-guide",
            "private": false,
            "watchers_count": 425
        },
        {
            "full_name": "mailchimp/country-region-selector",
            "private": false,
            "watchers_count": 2
        },
        {
            "full_name": "mailchimp/email-blueprints",
            "private": false,
            "watchers_count": 6604
        },
        {
            "full_name": "mailchimp/IronBox-PHP",
            "private": false,
            "watchers_count": 4
        },
        {
            "full_name": "mailchimp/MailChimp.tmbundle",
            "private": false,
            "watchers_count": 24
        },
        {
            "full_name": "mailchimp/mandrill-api-ruby",
            "private": false,
            "watchers_count": 0
        },
        {
            "full_name": "mailchimp/mc-magento",
            "private": false,
            "watchers_count": 111
        },
        {
            "full_name": "mailchimp/mc-magento2",
            "private": false,
            "watchers_count": 73
        },
        {
            "full_name": "mailchimp/mc-woocommerce",
            "private": false,
            "watchers_count": 49
        },
        {
            "full_name": "mailchimp/mc_markdown",
            "private": false,
            "watchers_count": 7
        },
        {
            "full_name": "mailchimp/middleman-with-md-submodule-example",
            "private": false,
            "watchers_count": 13
        },
        {
            "full_name": "mailchimp/OAuth2-sample-apps",
            "private": false,
            "watchers_count": 40
        },
        {
            "full_name": "mailchimp/play",
            "private": false,
            "watchers_count": 10
        },
        {
            "full_name": "mailchimp/Specs",
            "private": false,
            "watchers_count": 0
        },
        {
            "full_name": "mailchimp/statistrano",
            "private": false,
            "watchers_count": 42
        }
    ]
}
```



### 3. App Health Check



***Endpoint:***

```bash
Method: GET
Type: 
URL: http://127.0.0.1:5000/health-check
```



***Responses:***


Status: App Health Check | Code: 200



```js
I'm gucci.
```



---
[Back to top](#coding-challenge)
