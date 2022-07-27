
# Grocery  application with JWT

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/aitamahi/Grocery-Application-JWT.git
$ cd Grocery-Application-JWT
```
Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd grocery
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/app/register`.

```
curl --location --request POST 'localhost:8000/app/item/' \
--header 'Authorization: token eaf5297d58e26945d93babd6a16579ff8022b5b9' \
--header 'Content-Type: application/json' \
--data-raw '{
    "Item_name" : "Oranges",
    "Weights":"2",
    "Volumes":"0",
    "Units":"0",
    "Item_category":17    
}'
```
Output:
```{"id":3,"Item_name":"Oranges","Weights":"2","Volumes":"0","Units":"0","Item_category":17}```

```
curl --location --request POST 'localhost:8000/app/category/' \
--header 'Authorization: token eaf5297d58e26945d93babd6a16579ff8022b5b9' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=Ymk84OAyT2sjnoCND3YHsWK775jKcpaeTouhbv7ZoyNx6U3vYPbAKSXRiBMmTK5x; sessionid=zbsfmtvjzt4v2zyfedrzyros8v660gw1' \
--data-raw '{
    "category_item":"Fruits & Veg"
}'
```

Output:
```{"id":16,"category_item":"Fruits & Veg"}```
```
curl --location --request GET 'localhost:8000/app/order/' \
--header 'Authorization: token eaf5297d58e26945d93babd6a16579ff8022b5b9' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=Ymk84OAyT2sjnoCND3YHsWK775jKcpaeTouhbv7ZoyNx6U3vYPbAKSXRiBMmTK5x; sessionid=zbsfmtvjzt4v2zyfedrzyros8v660gw1' \
--data-raw '{
    "user": "33",
    "order_id":1,
    "created_at":"2022-07-26 21:17:22",
    "date":"2022-07-26",
    "items": [3]
}'
```
output:
```{"3":{"date":"2022-07-26T00:00:00Z","order_id":1,"created_at":"2022-07-26T21:17:22Z","user":33,"items":[3]}}```

```
curl --location --request GET 'localhost:8000/app/order_list/' \
--header 'Authorization: token eaf5297d58e26945d93babd6a16579ff8022b5b9' \
--data-raw ''
```
Output:
```
[{"id":1,"date":"2022-07-26T00:00:00Z","order_id":1,"created_at":"2022-07-26T21:17:22Z","user":33,"items":[]},{"id":2,"date":"2022-07-26T00:00:00Z","order_id":1,"created_at":"2022-07-26T21:17:22Z","user":33,"items":[3]},{"id":3,"date":"2022-07-26T00:00:00Z","order_id":1,"created_at":"2022-07-26T21:17:22Z","user":33,"items":[3]}]
```

```
curl --location --request GET 'localhost:8000/app/item/1' \
--header 'Authorization: token eaf5297d58e26945d93babd6a16579ff8022b5b9' \
--header 'Cookie: csrftoken=Ymk84OAyT2sjnoCND3YHsWK775jKcpaeTouhbv7ZoyNx6U3vYPbAKSXRiBMmTK5x; sessionid=zbsfmtvjzt4v2zyfedrzyros8v660gw1' \
--data-raw ''
```
Output:
```
{
    "id": 1,
    "Item_name": "flour",
    "Weights": "1",
    "Volumes": null,
    "Units": null,
    "Item_category": 17
}
```
```
curl --location --request POST 'localhost:8000/app/cart/' \
--header 'Authorization: token eaf5297d58e26945d93babd6a16579ff8022b5b9' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user": 33,
    "item": 3
}'
```
```
curl --location --request POST 'localhost:8000/app/review/' \
--header 'Authorization: token eaf5297d58e26945d93babd6a16579ff8022b5b9' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user":33,
    "product":3,
    "reviews_item":"2",
    "rating_item":"2"
}'
```
Output:
```
{
    "id": 6,
    "reviews_item": "2",
    "rating_item": "2",
    "user": 33,
    "product": 3
}
```
```
curl --location --request GET 'localhost:8000/app/itemfetch/?name=flour&categorys=Fruits&Veg&price=100' \
--header 'Authorization: token eaf5297d58e26945d93babd6a16579ff8022b5b9' \
--data-raw ''
```
Output:
```
[
    {
        "Item_name": "flour",
        "Item_category": 17,
        "Item_max_price": "200"
    },
    {
        "Item_name": "Oranges",
        "Item_category": 17,
        "Item_max_price": "100"
    }
]
```
```
curl --location --request POST 'localhost:8000/app/payment/' \
--header 'Authorization: token eaf5297d58e26945d93babd6a16579ff8022b5b9' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "order_id":1,
    "user":32,
    "payment":5000,
    "timestamp":"2022-07-27 11:06:20"
}'
```
ouput:
```
{"id":1,"payment":5000.0,"timestamp":"2022-07-27T05:36:37.365491Z","order_id":1,"user":32}
{"id":1,"payment":5000.0,"timestamp":"2022-07-27T05:36:37.365491Z","order_id":1,"user":32}
```
