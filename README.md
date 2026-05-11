# 🤖 AWS AI Chatbot — Serverless AI Assistant powered by Claude AI

A fully working AI-powered chatbot built on AWS using serverless architecture, Claude AI (Anthropic), and automated CI/CD deployment via GitHub Actions. Built as a personal DevOps learning project.

## 🚀 Live API Endpoint

POST https://siqyzofbt0.execute-api.us-east-1.amazonaws.com/chat

Test it:
curl -X POST https://siqyzofbt0.execute-api.us-east-1.amazonaws.com/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is AWS Lambda?", "session_id": "test-1"}'

## 🏗️ Architecture

User HTTP Request → API Gateway → Lambda → Claude AI → DynamoDB → Response

## ☁️ AWS Services Used

| Service | Purpose |
|---|---|
| AWS Lambda | Serverless compute |
| API Gateway | Public HTTPS REST endpoint |
| DynamoDB | Stores chat history |
| IAM | Permissions management |
| CloudWatch | Logs and monitoring |

## 🤖 AI Integration

| Tool | Purpose |
|---|---|
| Claude AI (Anthropic) | Generates AI responses |
| Model | claude-haiku-4-5 |

## 🔁 CI/CD Pipeline

Every push to main → Lambda auto-deploys in 12 seconds via GitHub Actions.

## 📁 Project Structure

aws-ai-chatbot/
├── lambda_function.py
├── .github/workflows/deploy.yml
└── README.md

## 🗄️ DynamoDB Schema

| Field | Type | Description |
|---|---|---|
| session_id | String PK | Conversation ID |
| timestamp | Number SK | Unix timestamp |
| role | String | user or assistant |
| message | String | Message content |

## 🛠️ Local Setup

git clone https://github.com/neelk8s/aws-ai-chatbot.git
cd aws-ai-chatbot
python3 -m venv venv
source venv/bin/activate
pip install boto3

## 🔐 IAM Permissions Required

- AmazonDynamoDBFullAccess
- AWSLambdaBasicExecutionRole

## 🧰 Tech Stack

| Category | Technology |
|---|---|
| Runtime | Python 3.14 |
| AI Model | Claude Haiku 4.5 |
| Cloud | AWS us-east-1 |
| CI/CD | GitHub Actions |

## 🗺️ Roadmap

- Serverless Lambda function DONE
- REST API via API Gateway DONE
- DynamoDB chat history DONE
- Claude AI integration DONE
- GitHub Actions CI/CD DONE
- Terraform IaC - coming soon
- Docker containerization - coming soon
- Web UI frontend - coming soon

## 👤 Author

Neelam — Salesforce Consultant transitioning to DevOps
AWS | Python | CI/CD | Serverless | Claude AI
GitHub: @neelk8s
