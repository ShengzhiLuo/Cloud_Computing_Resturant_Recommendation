# Restaurant recommendation and reservation
## 1. Overview
- A serverless and dynamic website with AWS S3, Cognito, API Gateway, Lambda and DynamoDB.
- Crawled NYC restaurant information in Yelp with Requests and stored in Elasticsearch for further search.
- Created chatbot using Lex, adopted SQS queue to store reservation information temporarily and then sent message to customer by SNS.
- Devised the recommendation module by calculating best matching restaurants and dropping those far away from customers with Google Maps API.


