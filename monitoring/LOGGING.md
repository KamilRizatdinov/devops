# Logging

## Familiarize with code base

* As you can see from my file structure, I used Vagrant + Ansible in order to deploy full stack inside Ubuntu 20.04 VM. In order to start you should run this command from current directory:
```sh
vagrant up
```

* If you want to check my `docker-compose.yaml`, `prometheus.yaml` and `promtail.yaml` you can find them here:
![click\!](https://github.com/KamilRizatdinov/devops/tree/main/monitoring/roles/monitoring/templates)

## Logging best practices

* Log at the Proper Level
* Write Meaningful Log Messages
* Log in Machine Parseable Format
* Make the Logs Human-Readable
* Don’t Log Too Much or Too Little
* Don’t Log Sensitive Information

### References:
* ![Logging Best Practices](https://www.scalyr.com/blog/the-10-commandments-of-logging/)

## Logging screenshots

![](https://github.com/KamilRizatdinov/devops/blob/main/monitoring/screenshots/logging/promtail.png)
![](https://github.com/KamilRizatdinov/devops/blob/main/monitoring/screenshots/logging/graphana.png)

## Monitoring screenshots

![](https://github.com/KamilRizatdinov/devops/blob/main/monitoring/screenshots/monitoring/graphana-loki.png)
![](https://github.com/KamilRizatdinov/devops/blob/main/monitoring/screenshots/monitoring/graphana-prometheus.png)
![](https://github.com/KamilRizatdinov/devops/blob/main/monitoring/screenshots/monitoring/prometheus-loki.png)
![](https://github.com/KamilRizatdinov/devops/blob/main/monitoring/screenshots/monitoring/prometheus-prometheus.png)
![](https://github.com/KamilRizatdinov/devops/blob/main/monitoring/screenshots/monitoring/prometheus-targets.png)

