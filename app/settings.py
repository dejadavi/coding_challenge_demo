from requests.packages.urllib3.util.retry import Retry

retry_behaviour = Retry(
    total=3,
    read=3,
    connect=3,
    backoff_factor=.5,
    status_forcelist=(500, 502, 504),
)
