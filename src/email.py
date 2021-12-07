#!/usr/bin/python3
import json
import boto3
import os
 
def lambda_handler(event, context):
    batch_processes=[]
    for record in event['Records']:
        print(record)
        send_request(record["body"])
         
 
def send_request(body):
    # Criar um novo cliente SNS
    sns = boto3.client('sns')
 
    # Publicar uma mensagem em um tópico SNS
    response = sns.publish(
        TopicArn=os.environ['email_topic'],    
        Message=body,    
    )
 
    # Imprimir a resposta
    print(response)
