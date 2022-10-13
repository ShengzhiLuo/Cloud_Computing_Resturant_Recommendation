import boto3
# Define the client to interact with Lex
client = boto3.client('lexv2-runtime')
import json
def lambda_handler(event, context):
    msg_from_user = event['messages'][0]['unstructured']['text']
    # change this to the message that user submits on 
    # your website using the 'event' variable
    # msg_from_user = "Hello"
    print(f"Message from frontend: {msg_from_user}")
    # Initiate conversation with Lex
    response = client.recognize_text(
            botId='MGM8JJ3B1X', # MODIFY HERE
            botAliasId='BPIJKWWAM4', # MODIFY HERE
            localeId='en_US',
            sessionId='testuser',
            text=msg_from_user)
    
    msg_from_lex = response.get('messages', [])
    if msg_from_lex:
        
        print(f"Message from Chatbot: {msg_from_lex[0]['content']}")
        print(response)
        resp = {
            'statusCode': 200,
            'messages': [
                 {'type': 'unstructured',
                 'unstructured': {
                 'text': json.dumps(msg_from_lex[0]['content'])
                     }}]
        }
        # modify resp to send back the next question Lex would ask from the user
        
        # format resp in a way that is understood by the frontend
        # HINT: refer to function insertMessage() in chat.js that you uploaded
        # to the S3 bucket
        return resp