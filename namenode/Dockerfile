FROM bde2020/hadoop-base:2.0.0-hadoop3.2.1-java8

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install -y cron nano python3 python3-pip \
    # Remove package lists for smaller image sizes
    && rm -rf /var/lib/apt/lists/* \
    && which cron \
    && rm -rf /etc/cron.*/*

HEALTHCHECK CMD curl -f http://localhost:9870/ || exit 1

ENV HDFS_CONF_dfs_namenode_name_dir=file:///hadoop/dfs/name
RUN mkdir -p /hadoop/dfs/name
VOLUME /hadoop/dfs/name

ADD run.sh /run.sh
RUN chmod a+x /run.sh


# register cron jobs to start the scripts by adding lines to /etc/crontab
RUN echo '@reboot root /bin/bash /work/script/startup.sh' >> /etc/crontab
RUN echo '* * * * * root /bin/bash /work/script/test.sh' >> /etc/crontab

EXPOSE 9870

# start cron in foreground (don't fork)
# ENTRYPOINT [ "cron", "-f" ]

CMD ["/run.sh"]




