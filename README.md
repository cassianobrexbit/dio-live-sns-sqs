# Live Coding - Mensageria na AWS com Amazon SNS e Amazon SQS

Repositório para o Live Coding do dia 08/12/2021

## Serviços utilizados

- Amazon SNS
- Amazon SQS
- AWS Lambda

## Instruções para desenvolvimento

### Criando uma Queue no Amazon SQS

- Acessar o Console da AWS -> Amazon SQS -> Create New Queue -> Queue Name [nome_da_queue] -> Standard Queue -> Create

### Criando um tópico no Amazon SNS 

- Acessar o Console da AWS -> Amazon SNS -> Create topic -> Name [nome_do_topic]
- Subscriptions -> Create subscription -> Protocol [Email] -> Endpoint [seu_email_para_subscrever] -> Create
- Acessar sua caixa de email e confirmar a subscrição ao tópico

### Criando uma função no AWS Lambda

- Acessar o Console da AWS -> AWS Lambda -> Create function -> Author from scratch -> Function name [nome_da_função] -> Runtime Python 3.9 -> Create function
- Inserir o código contido [aqui](src/email.py)
- Add trigger -> SQS -> Selecionar a queue SQS criada

#### Configurar permissões da função lambda para o SNS e o SQS

- Acessar a função criada -> Configuration -> Permissions -> Selecionar a role criada
- No console do AWS IAM -> Attach policies [AmazonSQSFullAccess, AmasonSNSFullAccess]

#### Configurar variáveis de ambiente

- Acessar a função criada -> Configuration -> Environment variables -> Add environment variable -> Key [email_topic] -> Value [arn_do_topico_criado] -> Save

### Testar a aplicação

- Acessar o SQS -> Selecionar a queue criada -> Send a message -> Inserir o corpo da mensagem -> Send
- Verificar na caixa de email o resultado

