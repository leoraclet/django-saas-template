<div align="center" style="scale: 60%"><img src="assets/django.png"></div>
<h1 align="center">Django Docker Saas Template</h1>

<div align="center">

![license](https://img.shields.io/github/license/leoraclet/django-saas-template)
![language](https://img.shields.io/github/languages/top/leoraclet/django-saas-template)
![lastcommit](https://img.shields.io/github/last-commit/leoraclet/django-saas-template)

</div>

## Table of Contents
- [Table of Contents](#table-of-contents)
- [📖 About](#-about)
- [✨ Features](#-features)
- [📦 Structure](#-structure)
- [📚 Libraries](#-libraries)
- [🚀 Install \& Run](#-install--run)
- [❤️ Thanks](#️-thanks)
- [📜 License](#-license)


## 📖 About

This is a fully featured template for building a Django-based SaaS application, containerized with
Docker. It includes everything from user authentication and background task processing to a REST API
with complete documentation.

The frontend is developed using Vite and Svelte, compiled into static assets and served via Django’s
template system.

For development, testing, and production, the stack incorporates tools such as Docker, PostgreSQL,
Redis, Caddy, MailHog, Sentry, Grafana, and Prometheus.

## ✨ Features

- **Project**

    - 🔄 **Reproducible**: Built with Nix, this configuration can be effortlessly reproduced on
    other machines, ensuring a consistent setup.

    - 📖 **Documented**: Most of the parts of my configuration files are commented and documented
    with links and explanations if necessary

- **Program**

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

- **Directories**

  - [**`terraform`**](./terraform/) - Terraform configuration files
  - [**`ansible`**](./ansible/) - Ansible configuration files
  - [**`server`**](./server/) - Main **Django** application
  - [**`assets`**](./assets/) - Images, Shaders and other Resources.
  - [**`docker`**](./docker/) - Docker start scripts
  - [**`etc`**](./etc/) - Services configuration
  - [**`frontend`**](./frontend/) - Frontend app (**Vite** + **Svelte** + **Tailwind CSS**)

- **Files**

  - `pyproject.toml` - Python environment configuration
  - `uv.lock` - Used by **uv** to version dependencies

## 📚 Libraries

> [!NOTE]
>
> Here are the principal libraries / dependencies of this project, but you can find all of theme in
> the [`pyproject.toml`](./pyproject.toml) file.

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

First, ensure you have the [**`uv`**](https://docs.astral.sh/uv/) python package manager installed.

If so, then clone the repo

```bash
git clone https://github.com/leoraclet/django-saas-template
cd django-saas-template
```

and install dependencies

```bash
uv sync
```

> [!TIP]
>
> You might need to create a virtual environment first.
> ```bash
> uv venv
> ```

Finally, depending if you have [**Make**](https://www.gnu.org/software/make/manual/make.html) or
[**Just**](https://github.com/casey/just) installed, you can run the developement server like this

```bash
make run
```

```bash
just run
```

## ❤️ Thanks

Many projects and blog posts have been great inspirations for this one.

Here are they :

- [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django)
- [Testdriven Blog](https://testdriven.io/blog/)
- [SaaS Pegasus Guides](https://www.saaspegasus.com/guides/)
-

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
