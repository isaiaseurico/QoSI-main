# QoSI
Qualidade de Serviço em Redes IP / Internet

Avaliação intermedia: 28 de Abril
Avaliação final: 19 de Maio

Results to be exported per measurement:
  - latency (ms)
  - jitter (ms)
  - packet loss (%)
  - download (Mbps)
  - upload (Mbps)
  - target (azure/aws/ibm/google/alibaba)
  - isp (ASN)
  - device operating system (linux,windows,macos,android,iphone) iperf3 python library not works on Windows!
  - date
  - hour

Cloud Virtual Machines (UK/London region):
  - Amazon AWS: 13.40.241.112
  - Alibaba Cloud: 8.208.103.146
  - Azure: 51.142.248.75 
  - Google: 35.214.121.83
  - IBM:

## Specs to create virtual machines in clouds
  - 1GB of memory
  - 1 CPU
  - Region/Location: London/UK
  - OS: CentOS8
  - Name: qosi-vm
  - Add firewall rule: reply ICMP and TCP port 5201

## Instructions to configure virtual machine

Install iperf3:
```sudo yum install iperf3```

If you cannot install software with yum, replace old CentOS 8 repositories:

```sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*```

```sed -i 's|#baseurl=http://vault.centos.org|baseurl=http://mirror.centos.org|g' /etc/yum.repos.d/CentOS-*```

Download this repository as zip file and extract it
```https://github.com/pg45517/QoSI/archive/refs/heads/main.zip```

Copy the file:
```sudo cp QoSI-main/iperf.service /etc/systemd/system/```

Reload and start service:

```sudo systemctl daemon-reload```

```sudo systemctl enable iperf```

```sudo systemctl start iperf```

## Download real time measurements results:

Linux command:

```curl -X POST http://18.169.204.30:8888/download -H 'Content-Type: application/json' -d '{"token_key":"Aeco9H382YPq"}' --output results.csv```

## How To Run the tool

Download the code, enter th folder with code and then

1. Install requirements:

```sudo ./install.sh```

2. Run python script:

```sudo python3 qosi.py```
