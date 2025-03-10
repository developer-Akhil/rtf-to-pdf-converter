import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def upload_rtf_to_s3(file_name, bucket, object_name=None):
    """Upload an RTF file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified, file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except FileNotFoundError:
        print(f"The file {file_name} was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except PartialCredentialsError:
        print("Incomplete credentials provided")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    return True

if __name__ == "__main__":
    file_name = 'input.rtf'
    bucket_name = 'your-s3-bucket-name'
    object_name = 'your-object-name.rtf'  # Optional

    success = upload_rtf_to_s3(file_name, bucket_name, object_name)
    if success:
        print(f"Successfully uploaded {file_name} to {bucket_name}/{object_name}")
    else:
        print("File upload failed")





# from spire.doc import Document, FileFormat
#
# # Create a Document instance
# doc = Document()
# # Load a RTF document
# doc.LoadFromFile("Test.rtf", FileFormat.Rtf)
# # Save it to a PDF
# doc.SaveToFile("RtfToPdf.pdf", FileFormat.PDF)
# doc.Close()
