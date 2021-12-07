# Live Coding - Mensageria na AWS com Amazon SNS e Amazon SQS

Repositório para o Live Coding do dia 08/12/2021

## Serviços utilizados

- Amazon SNS
- Amazon SQS
- AWS Lambda

## Instruções para desenvolvimento

### Criando uma Queue no Amazon SQS

- Acessar o Console da AWS -> Amazon SQS -> Create New Queue -> Queue Name [nome_da_queue] -> Standard Queue -> Create

### Criando uma função no AWS Lambda

- Acessar o Console da AWS -> Amazon SNS -> Create topic -> Name [nome_do_topic]
- Subscriptions -> Create subscription -> Protocol [Email] -> Endpoint [seu_email_para_subscrever] -> Create
- Acessar sua caixa de email e confirmar a subscrição ao tópico

### Criando um tópico no Amazon SNS
