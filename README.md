# my-server

## GitLab CI/CD

This repository includes a GitLab pipeline in `.gitlab-ci.yml` with:

- `backend_tests`: runs `pytest` from `backend/` on every merge request and on `main`.
- `deploy_production`: deploys automatically on push to `main` (after tests pass).

Configure these CI/CD variables in GitLab (`Settings -> CI/CD -> Variables`):

- `SSH_PRIVATE_KEY` (masked, protected): private key used by the runner to SSH.
- `DEPLOY_USER`: remote SSH user.
- `DEPLOY_HOST`: deployment host (domain name or IP).
- `DEPLOY_PATH`: absolute path to this project on the remote machine.
- `DEPLOY_PORT` (optional): SSH port, default `22`.
- `DEPLOY_ENV_URL` (optional): production environment URL shown in GitLab.

To fully block merges when tests fail, enable the project setting that requires successful pipelines before merge.
