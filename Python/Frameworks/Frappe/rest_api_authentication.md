# Authentication mechanisms supported in frappe

Frappe framework exposes REST API for all the doctypes and the REST API requests can be authenticated using either of the below to mechanisms

* password based authentication
* token based authentication

## Password based authentication

Using this method, `api/method/login` is called with **username and password**. Once that is successful, the response contains the **cookie**, which can be sent to authenticate future requests.

```Bash
username="Administrator"
passwd="passw0rd"
# login using the user credentials and store the cookies for authenticating with future requests
# Below command produces a JSON response like
# {"message":"Logged In",
#  "home_page":"/desk",
#  "full_name":"Administrator"}
curl -X POST 'http://localhost:8002/api/method/login' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-d '{"usr":"$username", "pwd":"$passwd"}' \
-c login-cookies.txt \
-w "%{http_code}"


# sample request for authenticating with the cookies
# produces output json like
# {"message":"Administrator"}
curl -X GET 'http://localhost:8002/api/method/frappe.auth.get_logged_user' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-b login-cookies.txt \
-w "%{http_code}"

# logout of the session
# produces output json {}
curl -X GET 'http://localhost:8002/api/method/logout' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json' \
-b login-cookies.txt \
-w "%{http_code}"

# delete the cookies
rm login-cookies.txt
```

```Javascript
fetch('http://<base-url>/api/method/login', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        usr: 'username or email',
        pwd: 'password'
    })
})
.then(r => r.json())
.then(r => {
    console.log(r);
})
```

## Token based authentication

Two types of token can be used. These tokens will be sent along with the **Authorization** header of the request.

### Basic token

This token is generated using the base64 encoded value of the string `"api_key:api_secret"`

```Bash
api_key="$1"
api_secret="$2"
# value part is case sensitive including the Basic keyword
token=$(echo "$api_key:$api_secret" | base64)
auth_header="Authorization: Basic $token"
```

```Python
import requests
import base64

url = "http://localhost:8002/api/method/frappe.auth.get_logged_user"

api_key = "<api_key>"
api_secret = "<api_secret>"

basic_token = base64.b64encode("{0}:{1}".format(api_key, api_secret).encode("utf-8"))

headers = {
  "Authorization": "Basic {}".format(basic_token)
}

requests.request('GET', url, headers = headers)
```

**NOTE**: In the documentation, the api key and secret are referred to as username and password. We can't use username and password with this type of authentication.

### Api key and secret as token

This token consists of **<api_key>:<api_secret>**. **api_key** for a user is generated only once. **secret** can be generated multiple times. But only the last generated **secret** is valid.

```Bash
# value part is case sensitive
token="<api_key>:<api_secret>"
auth_header="Authorization: token $token"
```

```Python
import requests

url = "http://localhost:8002/api/method/frappe.auth.get_logged_user"
token = "<api_key>:<api_secret>"

headers = {
  "Authorization": "token {}".format(token)
}

resp = requests.request('GET', url, headers = headers)
print("Status:{}, message:{}".format(resp.status_code, resp.json()))
```

## Generating token

Token can be used to perform CRUD operations

* api key once generated cannot be regenerated.
* Only system manager role can generate keys

Token can be generated using one of the 3 methods

* `/api/method/frappe.core.doctype.user.user.generate_keys?user="user_name"`
* `bench execute frappe.core.doctype.user.user.generate_keys --args ['user_name']`
* **Web: User -> Api Access -> Generate Keys**

---

## References

* [Password based authentication](https://frappe.io/docs/user/en/guides/integration/rest_api/simple_authentication)
* [Frappe REST API](https://frappe.io/docs/user/en/api/rest)
* [Http Cookies](https://ec.haxx.se/http-cookies.html)
* [Token based authentication](https://frappe.io/docs/user/en/guides/integration/rest_api/token_based_authentication)
* [Generate token in frappe](https://frappe.io/docs/user/en/guides/integration/how_to_set_up_token_based_auth)
