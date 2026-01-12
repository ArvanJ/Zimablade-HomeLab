FROM projectdiscovery/nuclei:latest

RUN apk add --no-cache curl bash tzdata

COPY scan.sh /scan.sh
COPY nuclei-cron /etc/crontabs/root

RUN chmod +x /scan.sh
CMD crond -f
