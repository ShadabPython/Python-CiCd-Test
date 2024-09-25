print(""" Skip to content
Navigation Menu
ShadabPython
/
Python-CiCd-Test

Type / to search
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Upload changed files to S3
adde new file7 #11
Jobs
Run details
deploy
succeeded 2 minutes ago in 15s
 service.py
1s
1s
0s
12s
1s
2024-09-25 04:48:49,813 - MainThread - botocore.auth - DEBUG - Signature:
5eab725e07cf7b632a8b2992b83afecdde4b4a7da1b003f1f6f90af117cba84f
2024-09-25 04:48:49,813 - MainThread - botocore.hooks - DEBUG - Event request-created.s3.ListObjectsV2: calling handler <function signal_transferring at 0x7f703559dea0>
2024-09-25 04:48:49,813 - MainThread - botocore.hooks - DEBUG - Event request-created.s3.ListObjectsV2: calling handler <function add_retry_headers at 0x7f7035d6beb0>
2024-09-25 04:48:49,813 - MainThread - botocore.endpoint - DEBUG - Sending http request: <AWSPreparedRequest stream_output=False, method=GET, url=https://dp-codebase-dev.s3.amazonaws.com/?list-type=2&prefix=&encoding-type=url, headers={'User-Agent': b'aws-cli/1.34.26 md/Botocore#1.35.26 ua/2.0 os/linux#6.8.0-1014-azure md/arch#x86_64 lang/python#3.10.15 md/pyimpl#CPython cfg/retry-mode#legacy botocore/1.35.26', 'X-Amz-Date': b'20240925T044849Z', 'X-Amz-Security-Token': b'***', 'X-Amz-Content-SHA256': b'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', 'Authorization': b'AWS4-HMAC-SHA256 Credential=***/20240925/us-east-1/s3/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date;x-amz-security-token, Signature=5eab725e07cf7b632a8b2992b83afecdde4b4a7da1b003f1f6f90af117cba84f', 'amz-sdk-invocation-id': b'cc11e7de-42ba-407c-acf6-c98f762d504d', 'amz-sdk-request': b'attempt=1'}>
2024-09-25 04:48:49,814 - MainThread - botocore.httpsession - DEBUG - Certificate path: /opt/hostedtoolcache/Python/3.10.15/x64/lib/python3.10/site-packages/botocore/cacert.pem
2024-09-25 04:48:49,814 - MainThread - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): dp-codebase-dev.s3.amazonaws.com:443
2024-09-25 04:48:49,915 - MainThread - urllib3.connectionpool - DEBUG - https://dp-codebase-dev.s3.amazonaws.com:443 "GET /?list-type=2&prefix=&encoding-type=url HTTP/11" 200 None
2024-09-25 04:48:49,916 - MainThread - botocore.hooks - DEBUG - Event before-parse.s3.ListObjectsV2: calling handler <function handle_expires_header at 0x7f7035d94280>
2024-09-25 04:48:49,916 - MainThread - botocore.parsers - DEBUG - Response headers: {'x-amz-id-2': 'pK2iWfkoVe6P/RF9Xc/kf1wbofeaC6q5eBi+HwwCKp8Kvt5+mLQSt3l+60I7F+3IKHogK844NaI=', 'x-amz-request-id': 'HFA6JMFD26F5N5TT', 'Date': 'Wed, 25 Sep 2024 04:48:50 GMT', 'x-amz-bucket-region': 'us-east-1', 'Content-Type': 'application/xml', 'Transfer-Encoding': 'chunked', 'Server': 'AmazonS3'}
2024-09-25 04:48:49,916 - MainThread - botocore.parsers - DEBUG - Response body:
b'<?xml version="1.0" encoding="UTF-8"?>\n<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Name>dp-codebase-dev</Name><Prefix></Prefix><KeyCount>3</KeyCount><MaxKeys>1000</MaxKeys><EncodingType>url</EncodingType><IsTruncated>false</IsTruncated><Contents><Key>README.md</Key><LastModified>2024-09-25T04:39:57.000Z</LastModified><ETag>&quot;e39ccd444cd2eba0d67be0fa411a5171&quot;</ETag><Size>18</Size><StorageClass>STANDARD</StorageClass></Contents><Contents><Key>app/my_file.py</Key><LastModified>2024-09-25T04:39:57.000Z</LastModified><ETag>&quot;0f6765e11e03c540745ca3e1d3d9aec5&quot;</ETag><Size>17</Size><StorageClass>STANDARD</StorageClass></Contents><Contents><Key>app/service.py</Key><LastModified>2024-09-25T04:39:57.000Z</LastModified><ETag>&quot;2066e36ff90e67771fc268bbdff5599e&quot;</ETag><Size>24</Size><StorageClass>STANDARD</StorageClass></Contents></ListBucketResult>'
2024-09-25 04:48:49,917 - MainThread - botocore.hooks - DEBUG - Event needs-retry.s3.ListObjectsV2: calling handler <botocore.retryhandler.RetryHandler object at 0x7f70346dde70>
2024-09-25 04:48:49,917 - MainThread - botocore.retryhandler - DEBUG - No retry needed.
2024-09-25 04:48:49,917 - MainThread - botocore.hooks - DEBUG - Event needs-retry.s3.ListObjectsV2: calling handler <bound method S3RegionRedirectorv2.redirect_from_error of <botocore.utils.S3RegionRedirectorv2 object at 0x7f70346ddf30>>
2024-09-25 04:48:49,917 - MainThread - botocore.hooks - DEBUG - Event after-call.s3.ListObjectsV2: calling handler <function decode_list_object_v2 at 0x7f7035d6b490>
2024-09-25 04:48:49,917 - MainThread - botocore.hooks - DEBUG - Event after-call.s3.ListObjectsV2: calling handler <function enhance_error_msg at 0x7f7035261bd0>
2024-09-25 04:48:49,917 - MainThread - awscli.customizations.s3.filters - DEBUG - dp-codebase-dev/README.md did not match exclude filter: /home/runner/work/Python-CiCd-Test/Python-CiCd-Test/.git/*
2024-09-25 04:48:49,917 - MainThread - awscli.customizations.s3.filters - DEBUG - dp-codebase-dev/README.md did not match exclude filter: dp-codebase-dev/.git/*
2024-09-25 04:48:49,917 - MainThread - awscli.customizations.s3.filters - DEBUG - dp-codebase-dev/README.md did not match exclude filter: /home/runner/work/Python-CiCd-Test/Python-CiCd-Test/.github/*
2024-09-25 04:48:49,917 - MainThread - awscli.customizations.s3.filters - DEBUG - dp-codebase-dev/README.md did not match exclude filter: dp-codebase-dev/.github/*
2024-09-25 04:48:49,918 - MainThread - awscli.customizations.s3.filters - DEBUG - =dp-codebase-dev/README.md final filtered status, should_include: True
2024-09-25 04:48:49,918 - MainThread - awscli.customizations.s3.syncstrategy.base - DEBUG - syncing: /home/runner/work/Python-CiCd-Test/Python-CiCd-Test/README.md -> dp-codebase-dev/README.md, size: 18 -> 18, modified time: 2024-09-25 04:48:37.001631+00:00 -> 2024-09-25 04:39:57+00:00
2024-09-25 04:48:49,918 - MainThread - s3transfer.utils - DEBUG - Acquiring 0
2024-09-25 04:48:49,918 - ThreadPoolExecutor-1_0 - s3transfer.tasks - DEBUG - UploadSubmissionTask(transfer_id=0, {'transfer_future': <s3transfer.futures.TransferFuture object at 0x7f7034751660>}) about to wait for the following futures []
2024-09-25 04:48:49,918 - ThreadPoolExecutor-1_0 - s3transfer.tasks - DEBUG - UploadSubmissionTask(transfer_id=0, {'transfer_future': <s3transfer.futures.TransferFuture object at 0x7f7034751660>}) done waiting for dependent futures
2024-09-25 04:48:49,919 - ThreadPoolExecutor-1_0 - s3transfer.tasks - DEBUG - Executing task UploadSubmissionTask(transfer_id=0, {'transfer_future': <s3transfer.futures.TransferFuture object at 0x7f7034751660>}) with kwargs {'client': <botocore.client.S3 object at 0x7f7034672890>, 'config': <s3transfer.manager.TransferConfig object at 0x7f70347477f0>, 'osutil': <s3transfer.utils.OSUtils object at 0x7f7034747880>, 'request_executor': <s3transfer.futures.BoundedExecutor object at 0x7f7034747a60>, 'transfer_future': <s3transfer.futures.TransferFuture object at 0x7f7034751660>}
2024-09-25 04:48:49,922 - ThreadPoolExecutor-1_0 - s3transfer.futures - DEBUG - Submitting task PutObjectTask(transfer_id=0, {'bucket': 'dp-codebase-dev', 'key': 'README.md', 'extra_args': {'ContentType': 'text/markdown'}}) to executor <s3transfer.futures.BoundedExecutor object at 0x7f7034747a60> for transfer request: 0.
2024-09-25 04:48:49,922 - ThreadPoolExecutor-1_0 - s3transfer.utils - DEBUG - Acquiring 0
2024-09-25 04:48:49,922 - ThreadPoolExecutor-0_0 - s3transfer.tasks - DEBUG - PutObjectTask(transfer_id=0, {'bucket': 'dp-codebase-dev', 'key': 'README.md', 'extra_args': {'ContentType': 'text/markdown'}}) about to wait for the following futures []
2024-09-25 04:48:49,922 - ThreadPoolExecutor-0_0 - s3transfer.tasks - DEBUG - PutObjectTask(transfer_id=0, {'bucket': 'dp-codebase-dev', 'key': 'README.md', 'extra_args': {'ContentType': 'text/markdown'}}) done waiting for dependent futures
2024-09-25 04:48:49,923 - ThreadPoolExecutor-0_0 - s3transfer.tasks - DEBUG - Executing task PutObjectTask(transfer_id=0, {'bucket': 'dp-codebase-dev', 'key': 'README.md', 'extra_args': {'ContentType': 'text/markdown'}}) with kwargs {'client': <botocore.client.S3 object at 0x7f7034672890>, 'fileobj': <s3transfer.utils.ReadFileChunk object at 0x7f7034752800>, 'bucket': 'dp-codebase-dev', 'key': 'README.md', 'extra_args': {'ContentType': 'text/markdown'}}
2024-09-25 04:48:49,923 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <function validate_ascii_metadata at 0x7f7035d6ad40>
2024-09-25 04:48:49,923 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <function sse_md5 at 0x7f7035d6a170>
2024-09-25 04:48:49,923 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <function convert_body_to_file_like_object at 0x7f7035d6b640>
2024-09-25 04:48:49,923 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <function validate_bucket_name at 0x7f7035d6a0e0>
2024-09-25 04:48:49,923 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <function remove_bucket_from_url_paths_from_model at 0x7f7035d6bf40>
2024-09-25 04:48:49,923 - ThreadPoolExecutor-1_0 - s3transfer.utils - DEBUG - Releasing acquire 0/None
2024-09-25 04:48:49,924 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <bound method S3RegionRedirectorv2.annotate_request_context of <botocore.utils.S3RegionRedirectorv2 object at 0x7f70346ddf30>>
2024-09-25 04:48:49,924 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <bound method ClientCreator._inject_s3_input_parameters of <botocore.client.ClientCreator object at 0x7f7034850af0>>
2024-09-25 04:48:49,924 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event before-parameter-build.s3.PutObject: calling handler <function generate_idempotent_uuid at 0x7f7035d69f30>
2024-09-25 04:48:49,924 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event before-endpoint-resolution.s3: calling handler <function customize_endpoint_resolver_builtins at 0x7f7035d94160>
2024-09-25 04:48:49,924 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event before-endpoint-resolution.s3: calling handler <bound method S3RegionRedirectorv2.redirect_from_cache of <botocore.utils.S3RegionRedirectorv2 object at 0x7f70346ddf30>>
2024-09-25 04:48:49,924 - ThreadPoolExecutor-0_0 - botocore.regions - DEBUG - Calling endpoint provider with parameters: {'Bucket': 'dp-codebase-dev', 'Region': 'us-east-1', 'UseFIPS': False, 'UseDualStack': False, 'ForcePathStyle': False, 'Accelerate': False, 'UseGlobalEndpoint': True, 'Key': 'README.md', 'DisableMultiRegionAccessPoints': False, 'UseArnRegion': True}
2024-09-25 04:48:49,925 - ThreadPoolExecutor-0_0 - botocore.regions - DEBUG - Endpoint provider result: https://dp-codebase-dev.s3.amazonaws.com
2024-09-25 04:48:49,925 - ThreadPoolExecutor-0_0 - botocore.regions - DEBUG - Selecting from endpoint provider's list of auth schemes: "sigv4". User selected auth scheme is: "None"
2024-09-25 04:48:49,925 - ThreadPoolExecutor-0_0 - botocore.regions - DEBUG - Selected auth type "v4" as "v4" with signing context params: {'region': 'us-east-1', 'signing_name': 's3', 'disableDoubleEncoding': True}
2024-09-25 04:48:49,925 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event before-call.s3.PutObject: calling handler <function conditionally_calculate_checksum at 0x7f70360b2b90>
2024-09-25 04:48:49,925 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event before-call.s3.PutObject: calling handler <function add_expect_header at 0x7f7035d6a440>
2024-09-25 04:48:49,926 - ThreadPoolExecutor-0_0 - botocore.handlers - DEBUG - Adding expect 100 continue header to request.
2024-09-25 04:48:49,926 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event before-call.s3.PutObject: calling handler <bound method S3ExpressIdentityResolver.apply_signing_cache_key of <botocore.utils.S3ExpressIdentityResolver object at 0x7f70346ddfc0>>
2024-09-25 04:48:49,926 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event before-call.s3.PutObject: calling handler <function add_recursion_detection_header at 0x7f7035d69b40>
2024-09-25 04:48:49,926 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event before-call.s3.PutObject: calling handler <function inject_api_version_header_if_needed at 0x7f7035d6b760>
2024-09-25 04:48:49,926 - MainThread - awscli.customizations.s3.filters - DEBUG - /home/runner/work/Python-CiCd-Test/Python-CiCd-Test/app/my_file.py did not match exclude filter: /home/runner/work/Python-CiCd-Test/Python-CiCd-Test/.git/*
2024-09-25 04:48:49,926 - ThreadPoolExecutor-0_0 - botocore.endpoint - DEBUG - Making request for OperationModel(name=PutObject) with params: {'url_path': '/README.md', 'query_string': {}, 'method': 'PUT', 'headers': {'Content-Type': 'text/markdown', 'User-Agent': 'aws-cli/1.34.26 md/Botocore#1.35.26 ua/2.0 os/linux#6.8.0-1014-azure md/arch#x86_64 lang/python#3.10.15 md/pyimpl#CPython cfg/retry-mode#legacy botocore/1.35.26', 'Content-MD5': '45zNREzS66DWe+D6QRpRcQ==', 'Expect': '100-continue'}, 'body': <s3transfer.utils.ReadFileChunk object at 0x7f7034752800>, 'auth_path': '/dp-codebase-dev/README.md', 'url': 'https://dp-codebase-dev.s3.amazonaws.com/README.md', 'context': {'client_region': 'us-east-1', 'client_config': <botocore.config.Config object at 0x7f7034672a10>, 'has_streaming_input': True, 'auth_type': 'v4', 'unsigned_payload': None, 's3_redirect': {'redirected': False, 'bucket': 'dp-codebase-dev', 'params': {'Bucket': 'dp-codebase-dev', 'Key': 'README.md', 'Body': <s3transfer.utils.ReadFileChunk object at 0x7f7034752800>, 'ContentType': 'text/markdown'}}, 'input_params': {'Bucket': 'dp-codebase-dev', 'Key': 'README.md'}, 'signing': {'region': 'us-east-1', 'signing_name': 's3', 'disableDoubleEncoding': True}, 'endpoint_properties': {'authSchemes': [{'disableDoubleEncoding': True, 'name': 'sigv4', 'signingName': 's3', 'signingRegion': 'us-east-1'}]}}}
2024-09-25 04:48:49,926 - MainThread - awscli.customizations.s3.filters - DEBUG - /home/runner/work/Python-CiCd-Test/Python-CiCd-Test/app/my_file.py did not match exclude filter: dp-codebase-dev/.git/*
2024-09-25 04:48:49,926 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event request-created.s3.PutObject: calling handler <function signal_not_transferring at 0x7f703559de10>
2024-09-25 04:48:49,926 - MainThread - awscli.customizations.s3.filters - DEBUG - /home/runner/work/Python-CiCd-Test/Python-CiCd-Test/app/my_file.py did not match exclude filter: /home/runner/work/Python-CiCd-Test/Python-CiCd-Test/.github/*
2024-09-25 04:48:49,927 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event request-created.s3.PutObject: calling handler <bound method RequestSigner.handler of <botocore.signers.RequestSigner object at 0x7f7034672980>>
2024-09-25 04:48:49,927 - MainThread - awscli.customizations.s3.filters - DEBUG - /home/runner/work/Python-CiCd-Test/Python-CiCd-Test/app/my_file.py did not match exclude filter: dp-codebase-dev/.github/*
2024-09-25 04:48:49,927 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event choose-signer.s3.PutObject: calling handler <bound method ClientCreator._default_s3_presign_to_sigv2 of <botocore.client.ClientCreator object at 0x7f7034850af0>>
2024-09-25 04:48:49,927 - MainThread - awscli.customizations.s3.filters - DEBUG - =/home/runner/work/Python-CiCd-Test/Python-CiCd-Test/app/my_file.py final filtered status, should_include: True
2024-09-25 04:48:49,927 - MainThread - awscli.customizations.s3.filters - DEBUG - dp-codebase-dev/app/my_file.py did not match exclude filter: /home/runner/work/Python-CiCd-Test/Python-CiCd-Test/.git/*
2024-09-25 04:48:49,927 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event choose-signer.s3.PutObject: calling handler <function set_operation_specific_signer at 0x7f7035d69d80>
2024-09-25 04:48:49,927 - MainThread - awscli.customizations.s3.filters - DEBUG - dp-codebase-dev/app/my_file.py did not match exclude filter: dp-codebase-dev/.git/*
2024-09-25 04:48:49,928 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event before-sign.s3.PutObject: calling handler <function remove_arn_from_signing_path at 0x7f7035d940d0>
2024-09-25 04:48:49,928 - MainThread - awscli.customizations.s3.filters - DEBUG - dp-codebase-dev/app/my_file.py did not match exclude filter: /home/runner/work/Python-CiCd-Test/Python-CiCd-Test/.github/*
2024-09-25 04:48:49,928 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event before-sign.s3.PutObject: calling handler <bound method S3ExpressIdentityResolver.resolve_s3express_identity of <botocore.utils.S3ExpressIdentityResolver object at 0x7f70346ddfc0>>
2024-09-25 04:48:49,928 - MainThread - awscli.customizations.s3.filters - DEBUG - dp-codebase-dev/app/my_file.py did not match exclude filter: dp-codebase-dev/.github/*
2024-09-25 04:48:49,928 - ThreadPoolExecutor-0_0 - botocore.auth - DEBUG - Calculating signature using v4 auth.
2024-09-25 04:48:49,928 - MainThread - awscli.customizations.s3.filters - DEBUG - =dp-codebase-dev/app/my_file.py final filtered status, should_include: True
2024-09-25 04:48:49,928 - ThreadPoolExecutor-0_0 - botocore.auth - DEBUG - CanonicalRequest:
PUT
/README.md

content-md5:45zNREzS66DWe+D6QRpRcQ==
content-type:text/markdown
host:dp-codebase-dev.s3.amazonaws.com
x-amz-content-sha256:UNSIGNED-PAYLOAD
x-amz-date:20240925T044849Z
x-amz-security-token:***

content-md5;content-type;host;x-amz-content-sha256;x-amz-date;x-amz-security-token
UNSIGNED-PAYLOAD
2024-09-25 04:48:49,928 - MainThread - awscli.customizations.s3.syncstrategy.base - DEBUG - syncing: /home/runner/work/Python-CiCd-Test/Python-CiCd-Test/app/my_file.py -> dp-codebase-dev/app/my_file.py, size: 17 -> 17, modified time: 2024-09-25 04:48:37.002631+00:00 -> 2024-09-25 04:39:57+00:00
2024-09-25 04:48:49,928 - ThreadPoolExecutor-0_0 - botocore.auth - DEBUG - StringToSign:
AWS4-HMAC-SHA256
20240925T044849Z
20240925/us-east-1/s3/aws4_request
1d30efd5754e06f541e51cf1da0137197a382d5a5eff58c680b7767788151b0a
2024-09-25 04:48:49,929 - MainThread - s3transfer.utils - DEBUG - Acquiring 1
2024-09-25 04:48:49,929 - ThreadPoolExecutor-0_0 - botocore.auth - DEBUG - Signature:
19bb2f3714370cb1812b212c225266620d9ca8c351fe941f876bf40f7a08de11
2024-09-25 04:48:49,929 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event request-created.s3.PutObject: calling handler <function signal_transferring at 0x7f703559dea0>
2024-09-25 04:48:49,929 - MainThread - awscli.customizations.s3.filters - DEBUG - /home/runner/work/Python-CiCd-Test/Python-CiCd-Test/app/service.py did not match exclude filter: /home/runner/work/Python-CiCd-Test/Python-CiCd-Test/.git/*
2024-09-25 04:48:49,929 - ThreadPoolExecutor-0_0 - botocore.hooks - DEBUG - Event request-created.s3.PutObject: calling handler <function add_retry_headers at 0x7f7035d6beb0>
2024-09-25 04:48:49,929 - ThreadPoolExecutor-1_0 - s3transfer.tasks - DEBUG - UploadSubmissionTask(transfer_id=1, {'transfer_future': <s3transfer.futures.TransferFuture object at 0x7f7034753a30>}) about to wait for the following futures []
2024-09-25 04:48:49,929 - ThreadPoolExecutor-0_0 - botocore.endpoint - DEBUG - Sending http request: <AWSPreparedRequest stream_output=False, method=PUT, url=https://dp-codebase-dev.s3.amazonaws.com/README.md, headers={'Content-Type': b'text/markdown', 'User-Agent': b'aws-cli/1.34.26 md/Botocore#1.35.26 ua/2.0 os/linux#6.8.0-1014-azure md/arch#x86_64 lang/python#3.10.15 md/pyimpl#CPython cfg/retry-mode#legacy botocore/1.35.26', 'Content-MD5': b'45zNREzS66DWe+D6QRpRcQ==', 'Expect': b'100-continue', 'X-Amz-Date': b'20240925T044849Z', 'X-Amz-Security-Token': b'***', 'X-Amz-Content-SHA256': b'UNSIGNED-PAYLOAD', 'Authorization': b'AWS4-HMAC-SHA256 Credential=***/20240925/us-east-1/s3/aws4_request, SignedHeaders=content-md5;content-type;host;x-amz-content-sha256;x-amz-date;x-amz-security-token, Signature=19bb2f3714370cb1812b212c225266620d9ca8c351fe941f876bf40f7a08de11', 'amz-sdk-invocation-id': b'8a39c4e7-e5e8-490a-a9e3-919de3809887', 'amz-sdk-request': b'attempt=1', 'Content-Length': '18'}>
2024-09-25 04:48:49,930 - MainThread - awscli.customizations.s3.filters - DEBUG - /home/runner/work/Python-CiCd-Test/Python-CiCd-Test/app/service.py did not match exclude filter: dp-codebase-dev/.git/*
2024-09-25 04:48:49,930 - ThreadPoolExecutor-1_0 - s3transfer.tasks - DEBUG - UploadSubmissionTask(transfer_id=1, {'transfer_future': <s3transfer.futures.TransferFuture object at 0x7f7034753a30>}) done waiting for dependent futures
0s
0s
0s
Rephrase
""")
