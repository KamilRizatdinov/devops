# Docker best practices:

* Containers generated with image you build can be stopped and destroyed, then rebuilt and replaced with an absolute minimum set up and configuration
* Make use of .dockerignore to make sure you not included unnecessary files and folders
* Make sure to expose only those ports your running application needs
* Tests are often not needed in production, only on development
* Manipulate the order of layers for best caching experience. For example you can copy and install dependencies before copying the rest of the files. This will ensure you will not need to rerun the dependency instalation layers on every update of your codebase
* Use multi-stage builds. They allow you to reduce the size of your image
* Use only trusted images as your base image
* Avoid running containers as root
* Sign docker images
* Find, fix and monitor for open source vulnerabilities

## References:
* https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
* https://sysdig.com/blog/dockerfile-best-practices/
* https://snyk.io/blog/10-docker-image-security-best-practices/
