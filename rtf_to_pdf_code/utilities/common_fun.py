import uuid
from typing import List, Dict
import boto3
from striprtf.striprtf import rtf_to_text

__all__ = ['CommonFun']


class CommonFun(object):

    def __init__(self, prop):
        self.prop = prop
        self.list_files = []
        self.s3_resource_obj = boto3.resource('s3')
        self.s3_client_obj = boto3.client('s3')

    def get_file_list(self, bucket_src: str, prefix_src: str) -> List:
        my_bucket = self.s3_resource_obj.Bucket(bucket_src)
        print(bucket_src)
        print(prefix_src)
        for object_summary in my_bucket.objects.filter(Prefix=prefix_src):
            self.list_files.append(object_summary.key)

        return self.list_files

    def download_file_from_s3(self, bucket, object_name, file_name=None):

        try:
            if file_name is None:
                file_name = object_name
            response = self.s3_client_obj.get_object(Bucket=bucket, Key=object_name)
            rtf_decoded = response["Body"].read()
            print("***************rtf_decoded****************")
            print(type(rtf_decoded))
            # s3_response = self.s3_resource_obj
            # # s3_response = get_s3_object(bucket, object_name)
            # rtf_decoded = s3_response.decode('UTF-8')
            # text = rtf_to_text(rtf_decoded)
            # self.s3_client_obj.put_object(Body=rtf_decoded, bucket=bucket, Key=f"{object_name}")
            # print(rtf_decoded)
            return rtf_decoded

        except Exception as e:
            print(f"error with download function {e}")

    def upload_file_to_s3(self, file_name, bucket, object_name=None):
        try:
            if object_name is None:
                object_name = file_name

            self.upload_file_to_s3(file_name, bucket, object_name)
            print(f"File {object_name} downloaded from {bucket} to {file_name}")
        except Exception as e:
            print(f"error with download function {e}")

    def write_to_s3(self, buffer_content, bucket_nm, key_nm):
        object_key = key_nm.replace(".rtf", ".pdf")  # Replace extension
        self.s3_client_obj.put_object(Body=buffer_content, Bucket=bucket_nm, Key=object_key)

    def delete_file(self, bucket_nm: str, prefix: str, key: str):
        self.s3_resource_obj.Object(bucket_nm, prefix + key).delete()

