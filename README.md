<div align="center"><img src="assets/django.png" style="width: 200px"></div>
<br>
<h1 align="center">Django + Docker Saas Template</h1>

<div align="center">

![license](https://img.shields.io/github/license/leoraclet/django-saas-template)
![language](https://img.shields.io/github/languages/top/leoraclet/django-saas-template)
![lastcommit](https://img.shields.io/github/last-commit/leoraclet/django-saas-template) <br>
![Language](https://img.shields.io/badge/Language-Python-1d50de)
![Libraries](https://img.shields.io/badge/Framework-Django-fa8925)
![Size](https://img.shields.io/badge/Size-376Mo-f12222)
![OpenSource](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)

</div>

> [!IMPORTANT]
>
> This project is currently under active development. I'm regularly making updates and additions to improve its completeness and functionality.


## Table of Contents
- [Table of Contents](#table-of-contents)
- [🌟 Showcase](#-showcase)
- [📖 About](#-about)
- [✨ Features](#-features)
- [📦 Structure](#-structure)
- [📚 Libraries](#-libraries)
- [🚀 Install \& Run](#-install--run)
  - [🏠 System](#-system)
  - [🐳 Using Docker](#-using-docker)
- [❤️ Thanks](#️-thanks)
- [📜 License](#-license)


## 🌟 Showcase

> [!NOTE]
>
> Some images coming some day ...

## 📖 About

This is a fully featured template for building a **Django**-based **SaaS** application, containerized with
**Docker**. It includes everything from user authentication and background task processing to a **REST API**
with complete documentation.

The frontend is developed using **Vite** and **Svelte**, compiled into static assets and served via Django’s
template system.

For development, testing, and production, the stack incorporates tools such as **PostgreSQL**,
**Redis**, **Caddy**, **MailHog**, **Sentry**, **Grafana**, and **Prometheus**.

## ✨ Features

**Project**

- 🔄 **Reproducibility**: The project is built using [**uv**](https://docs.astral.sh/uv/), enabling seamless setup replication across different machines for consistent environments.

- 📖 **Well-Documented**: Source files include thorough comments and, where applicable, links and explanations to clarify key settings.

**Program**

  - 🧱 **Django-based backend** Powerful and extensible backend using Django, ideal for SaaS
  applications.

  - 🔐 **Built-in authentication system** User registration, login, password reset, and more out
  of the box.

  - ⚙️ **Background task support** Integrated support for background processing (e.g., with Celery
  or Django Q).

  - 🔌 **REST API with documentation** Fully functional REST API with auto-generated documentation
  (e.g., Swagger or ReDoc).

  - 🎨 **Modern frontend with Vite and Svelte** Responsive and fast frontend built with Svelte and
  bundled via Vite, served through Django templates.

  - 🐳 **Docker-based development and deployment** Consistent environments using Docker for local
  development, testing, and production.

  - 📊 **Monitoring and observability tools** Integrated support for Prometheus and Grafana for
  metrics and monitoring.

  - 📬 **Email testing with MailHog** Catch and inspect outgoing emails during development.

  - 📈 **Error tracking with Sentry** Real-time error logging and alerting for faster debugging
  and maintenance.

  - 🌐 **Caddy as a web server and reverse proxy** Automatically manages HTTPS and routing for
  production-ready deployments.

  - 🐘 **PostgreSQL database** Reliable and robust relational database for handling application
    data.

  - 🚀 **Redis integration** In-memory data store for caching, session management, and background
  tasks.

## 📦 Structure

> [!NOTE]
>
> The project's structure should speak for itself, but here are the most important parts just in case
> you're wondering

**Directories**

- [**`.github`**](./.github/) - Contains GitHub Actions CI/CD workflows.
- [**`.vscode`**](./.vscode/) - VS Code-specific settings and helper documentation.
- [**`ansible`**](./ansible/) - Ansible configuration files (*currently empty*).
- [**`assets`**](./assets/) - Static image resources used in the project.
- [**`docker`**](./docker/) - Scripts to run services via Docker (e.g. Django, Celery, Gunicorn).
- [**`etc`**](./etc/) - Configuration files for infrastructure components (e.g. Grafana, Traefik, Caddy, Prometheus).
- [**`frontend`**](./frontend/) - Frontend app using **Svelte**, **Vite**, and **TypeScript**.
- [**`server`**](./server/) - Main Django application, including apps, configuration, static files, templates, and localization.
- [**`terraform`**](./terraform/) - Infrastructure-as-code configuration with Terraform (*currently empty*).

**Files**

- `.dockerignore`, `.gitignore`, `.gitattributes` - Ignore rules and Git configurations.
- `.editorconfig`, `.flake8`, `.pre-commit-config.yaml` - Formatting and linting configurations.
- `.env.prod`, `db.prod.env` - Environment variable files for production setup.
- `.python-version` - Python version specification (for pyenv and tooling).
- `Dockerfile.test`, `docker-compose*.yml` - Docker configuration files for different environments.
- `Jenkinsfile` - CI/CD pipeline configuration for Jenkins.
- `Justfile`, `Makefile` - Task runners for development and automation.
- `Procfile` - Process declaration file for deployment (e.g. Heroku).
- `LICENSE`, `README.md` - License and documentation files.
- `pyproject.toml`, `requirements.txt`, `uv.lock` - Python environment and dependency configuration.


## 📚 Libraries

> [!NOTE]
>
> Below are some of the key libraries and dependencies used in this project. For the full list, refer to the [`pyproject.toml`](./pyproject.toml) file.


- 🌐 Web Framework & Core
  - **[`django`](https://www.djangoproject.com/):** Full-featured web framework for building modern
    web apps.
  - **[`django-environ`](https://github.com/joke2k/django-environ):** Environment variable
    management for 12-factor app configs.
  - **[`whitenoise[brotli]`](https://whitenoise.evans.io/en/stable/):** Efficient static file
    serving in production.

- ⚙️ API & Serialization
  - **[`djangorestframework`](https://www.django-rest-framework.org/):** Build robust REST APIs with
    Django.
  - **[`drf-spectacular`](https://drf-spectacular.readthedocs.io/):** Automatically generate
    OpenAPI/Swagger schema.

- 🔐 Authentication & Payments
  - **[`django-allauth`](https://django-allauth.readthedocs.io/):** Integrated auth with support for
    social login, MFA, and OIDC.
  - **[`dj-stripe`](https://dj-stripe.dev/):** Connects Django to Stripe for payments and
    subscriptions.

- ⚡ Async & Real-time
  - **[`channels`](https://channels.readthedocs.io/):** WebSocket and async support for Django.
  - **[`uvicorn`](https://www.uvicorn.org/):** ASGI server for running async Django apps.

- ⏱️ Task Queue & Scheduling
  - **[`django-celery-beat`](https://github.com/celery/django-celery-beat):** Schedule periodic
    tasks with Celery and Django.
  - **[`redis`](https://redis.io/):** In-memory data store used as Celery broker and cache.

- 📊 Monitoring & Observability
  - **[`sentry-sdk`](https://docs.sentry.io/platforms/python/guides/django/):** Real-time error
  monitoring and performance tracing.

- 🪵 Logging & Notifications
  - **[`loguru`](https://github.com/Delgan/loguru):** Feature-rich logging library with beautiful
    formatting.
  - **[`apprise`](https://github.com/caronc/apprise):** Multi-platform push notification system.


## 🚀 Install & Run

If you'd like to run this Django app on your machine, here are two versions of how to do so by either doing on your [**system**](#-system) or [**using docker**](#-using-docker).

### 🏠 System

First, make sure the [**`uv`**](https://docs.astral.sh/uv/getting-started/installation/) Python package manager is installed on your system.

Once that's done, clone the repository

```bash
git clone https://github.com/leoraclet/django-saas-template
cd django-saas-template
```

Then, install the project dependencies:

```bash
uv sync
```

> [!TIP]
>
> You may need to create a virtual environment beforehand:
> ```bash
> uv venv
> ```

Finally, if you have either [**Make**](https://www.gnu.org/software/make/manual/make.html) or
[**Just**](https://github.com/casey/just) installed, you can launch the development server accordingly.

```bash
make migrate  # To migrate the Database (MANDATORY)
make run  # To run the developement server
```

or you can just run simple commands using

```bash
uv run {YOUR_COMMAND}
```

### 🐳 Using Docker

Ensure that [**Docker**](https://docs.docker.com/get-started/introduction/get-docker-desktop/) is installed on your system and that the `docker` command is available in your terminal.

To start the Docker setup, run:

```bash
docker compose up -d
```

> [!TIP]
>
> To rebuild the image from scratch (without using the cache), use the following command:
>```bash
> docker compose build --no-cache
>```

As with local development, you can use the [**`Makefile`**](./Makefile) (or [**`Justfile`**](./Justfile)) to manage Docker-related tasks easily with the following commands:

```bash
make up      # Build (if needed) and start the containers
make down    # Stop and remove containers and associated networks
make build   # Build or rebuild the Docker services
make logs    # View the output logs from running containers
```

## ❤️ Thanks

Projects and blog posts that inspired this template :

- [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django)
- [Testdriven Blog](https://testdriven.io/blog/)
- [SaaS Pegasus Guides](https://www.saaspegasus.com/guides/)
- [Digital
  Ocean](https://www.digitalocean.com/community/tutorials/how-to-scale-and-secure-a-django-application-with-docker-nginx-and-let-s-encrypt)
- [Django Astro
  Demo](https://github.com/marqetintl/django-astro-jsx-demo/blob/main/django/config/urls.py)
- [Medium Article](https://medium.com/@Am_Issath/list/django-web-development-tricks-e2bac4bc0742)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
