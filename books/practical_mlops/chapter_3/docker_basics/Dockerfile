FROM centos:8

RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-* &&\
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-* &&\
    yum update -y &&\
    dnf install -y python38 && dnf clean all

RUN pip3 install --no-cache-dir pytest

ENTRYPOINT [ "/bin/bash" ]
