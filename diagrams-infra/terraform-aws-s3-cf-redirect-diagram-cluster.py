#!/usr/bin/env python

from diagrams import Cluster, Diagram
from diagrams.aws.network import CloudFront, Route53
from diagrams.aws.storage import SimpleStorageServiceS3
from diagrams.aws.security import CertificateManager, KeyManagementService
from diagrams.onprem.network import Internet

graph_attr = {
    "margin":"-2"
}

cluster_graph_attr = {
    "margin":"10"
}

with Diagram("terraform-aws-s3-cf-redirect", graph_attr=graph_attr, filename="diagrams-output/terraform-aws-s3-cf-redirect-diagram", direction="TB", show=True):

    with Cluster("", graph_attr=cluster_graph_attr):

        with Cluster("Web Facing"):
            internet = Internet("redirect target")
            cf = CloudFront("cloudFront distro")

        with Cluster("S3"):

            with Cluster("Encryption"):
                kms = KeyManagementService("kms")  

            with Cluster("Buckets"):
                logging_bucket = SimpleStorageServiceS3("logbucket") 
                domain_buckets = [SimpleStorageServiceS3("www-fqdn"), SimpleStorageServiceS3("fqdn")]
              
        with Cluster("Route 53"): 

            with Cluster("Alias Records"):
                alias = [Route53("www-fqdn"), Route53("fqdn")]
            
            with Cluster("ACM Certs"):   
                acm = CertificateManager("acm")
                dvo = Route53("acm validation")