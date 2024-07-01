# 20-Mastering-Celery

Mastering_Celery is a comprehensive project designed to demonstrate the capabilities and configurations of Celery, a powerful distributed task queue. Built using Docker Compose for seamless deployment, the project encompasses various services:

- Django Backend: Provides the core application framework.
- Database:
    - PostgreSQL
- Celery Services:
    - Standalone Lightweight Worker: Efficiently handles lightweight tasks.
    - Regular Worker: Executes general tasks (based on django image).
- Message Brokers:
    - Redis: Primary message broker.
    - RabbitMQ: Alternative message broker.
- Monitoring and Management:
    - Flower: Web-based tool for monitoring and managing Celery workers.
- Proxy:
    - nginx configured as reverse proxy for Django, and to serve static files.


## Key Features:

### Task Configuration and Types:
Demonstrates task prioritization, chaining, grouping, and queue usage.
Illustrates scheduling, time intervals, exception handling, and task routing.
Implements rate limiting, passing arguments, and returning results from tasks.
Shows synchronous and asynchronous task execution.

### Worker Types:
Utilizes both standalone lightweight Celery workers for specific Django tasks and regular workers for broader functionalities.

### Monitoring and Management:
Uses Flower to monitor Celery tasks and manage their execution.

### Message Brokers:
Configures Redis and RabbitMQ as message brokers, showcasing their integration with Celery.

### Error Handling and Monitoring:
* Demonstrates error handling within tasks.
* Integrates Sentry for monitoring Celery tasks and handling errors effectively.

### Advanced Configurations:
* Covers Celery task autodiscovery and customization.
* Implements automatic retries, task timeouts, and task revoking.
* Handles task signals and ensures graceful shutdown and cleanup.

### Scheduled Tasks:
Shows task scheduling, including periodic tasks and persistence using Django's beat scheduler.

### Integration and Deployment:
Organizes everything within Docker containers and Docker Compose for easy setup and reproducibility.


## Project Structure:
* Docker Compose Setup: Includes services for Django, Celery workers, Redis, RabbitMQ, Flower, and PostgreSQL database.
* Task Definitions: Tasks are defined within Celery or task files, categorized and commented for clarity and specific functionality.
* Scenario-Based Configurations: Parts of the configuration may be commented or uncommented to illustrate specific scenarios while keeping all configurations and examples in one place.


## Enviromental variables:
To ensure proper configuration, please adjust the environmental variables and rename folders as follows:
- Rename the folder **.envs/.dev-example** to **.envs/.dev**
- Set all environmental variables specific to your project's requirements within .envs/.dev.

This step ensures that your project is configured correctly with the appropriate environmental settings.


## Conclusion:
Mastering_Celery serves as a comprehensive resource for learning and showcasing the capabilities of Celery. It provides extensive examples and configurations, making it a valuable tool for understanding task queue management, asynchronous processing, and distributed systems in real-world applications. By leveraging Docker and Docker Compose, the project ensures ease of setup and deployment across different environments, fostering practical learning and experimentation with Celery.

