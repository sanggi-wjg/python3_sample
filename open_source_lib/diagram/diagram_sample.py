from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS, Database
from diagrams.aws.network import ELB
from diagrams.oci.monitoring import Queue
from diagrams.onprem.database import MySQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.network import Nginx, Apache, Internet
from diagrams.onprem.queue import Celery

"""
https://diagrams.mingrammer.com
"""
with Diagram("Sample", show = False):
    user_web = EC2("Web")

    with Cluster('WEB SERVER'):
        web_server = [
            Apache('Web Server'), Nginx('Web Server')
        ]

    with Cluster('QUEUE'):
        sever_queue = Redis('Queue Broker')
        sever_queue - [Celery('Queue Worker')]

    with Cluster('DATABASE'):
        db_master = MySQL('Database')
        # db_master - Database('Database')

    with Cluster('DATABASE2'):
        db_slave = MySQL('Database2')
        # db_slave - Database('Database2')

    user_web >> web_server >> sever_queue
    sever_queue >> db_master
    sever_queue >> db_slave
    web_server >> db_master
    web_server >> db_slave
