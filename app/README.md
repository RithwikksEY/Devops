# Cloud-Native DevOps Backend Service

## Overview
This project demonstrates a cloud-native backend service deployed using DevOps best practices.

## Tech Stack
- Python (FastAPI)
- Docker
- Terraform
- Azure Kubernetes Service (AKS)
- GitHub Actions

## Repository Structure
- `app/` – Application source code and Dockerfile
- `infra/terraform/` – Infrastructure provisioning using Terraform
- `k8s/` – Kubernetes deployment manifests
- `.github/workflows/` – CI/CD pipelines

## Application Endpoints
- `/health` – Service health check
- `/info` – Runtime and environment information
- `/time` – Current server time
- `/config` – Runtime configuration values

## Deployment
Infrastructure and application deployment are automated using GitHub Actions.
