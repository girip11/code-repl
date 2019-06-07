# Json Web Token

## What is Json Web Token (JWT)?
* Json web tokens contain digital signatures of claims that can be used for authenticating web requests. JWT can be used for authenticating requests from clients post the single signon, or it can be used between web servers for exchanging information.

## Structure
* JWT consists of three sections
    ```bash
        '<Base64 encoded header json>.' +
        '<Base64 encoded payload json>.' +
        '<Base64 encoded digital signature>'
    ```

### Header

* Header is a json that primarily contains two fields **alg** and **typ**. **alg** field contains information about the algorithm used to compute the hash/digital signature. It could be SHA256 or RSA
    ```JSON
        {
            "alg": "HS256",
            "typ": "jwt"
        }
    ```

### Payload
* Payload consists of claims that can be used by the web servers for web request authorization. Claims are of two types. Standard claims and custom claims. Standard claims are listed as below. 
    - iss - issuer 
    - sub - subject (whom the token refers to)
    - aud - audience (who the token is intended for)
    - exp - expiration time (time in epoch seconds)
    - nbf - not valid before (time in epoch seconds)
    - iat - issued at (time in epoch seconds)
    - jti - jwt id

* Its not mandatory for payload to contain all the standard claims. JWT libraries can offer validation against these standard claims.

* Custom claims are application based. For instance, we can define a claim called **role** and assign some value that can be interpreted by the target web server and use the claim for authorizing the requests.

### Digital signature(hash)
* Hash or the digital signature is computed as in the below snippet. Hashing algorithm specified in the header will be used for generating the digital signature.
  ```bash
        # Assume base64_enc method returns base64 encoded string
        secret = $1 # secret used by the hashing algorithm
        base64_encoded_header=base64_enc(header_json)
        base64_encoded_payload=base64_enc(payload_json)
        data_to_sign="${base64_encoded_header}.${base64_encoded_payload}"

        # Hasing algorithm as mentioned in the header
        digital_signature=hash_algorithm($data_to_sign, $secret)
        base64_encoded_signature=base64_enc($digital_signature)

        jwt="${base64_encoded_header}.${base64_encoded_payload.${base64_encoded_signature}"
  ```

* Hashing algorithm accepts a **secret** for signing the data. Web servers who are processing the jwt will have secret available to them to verify the token integrity.

## JWT application
* Single sign on - Once the user signs in for the first time, server can generate a jwt if the sign in successful and it can be sent to the client in the response to the sign in request. From there on, clients can pass the jwt on every subsequent request to the server.

* Secure communication across trusted services - In cases where services are aware of existance of each other and share the hashing algorithm secret, jwt can be used to communicate with all those services. For instance, a client(browser) can get the jwt from service1 after proving its authenticity. Then the client can use this jwt to communicate with service2, given that the service1 and service2 both know the secret used for the hashing algorithm.

## Reference:
* [Generate JWT](http://jwtbuilder.jamiekurtz.com/)
* [JWT token verification](https://jwt.io/)