# CI best practices:

* Automate the build
* Make the build self-testing
* Every commit should be built
* Keep the build fast
* Make it easy to get the latest deliverables
* Automate deployment
* Build image only if test reports OK
* Cache your dependencies
* Cache your docker image
* Use repository for your secrets, do not expose them to the public. (Take a ‘security first approach’)
* Make each step as small as you can, do not overload them
* Implement tracking and version control tools

## References:
* https://www.cloudbees.com/continuous-delivery/continuous-integration-best-practices
