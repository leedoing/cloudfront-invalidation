'''
CloudFront Invalidation
'''

try:
    import boto3
    import random
    import time
    import datetime
    import uuid
    from botocore.exceptions import ClientError
except ImportError:
    HAS_BOTO = False

client = boto3.client('cloudfront')

##샘플 변수
DISTRIBUTIONID='E12OX8RSSI1M70'
BUCKETNAME = 'cf-prefetch'
KEY = 'test.txt'

##Invalidation을 위한 랜덤 해쉬값 생성
CALLERREFERENCE = str(uuid.uuid4())


##Path, CF ID 확인(Invalidation 생성 전 체크)
def check_invalidation_path(distributionId, bucketName, key):
    print('[Started check_invalidation_path]')
    try:
        get_distribution_response = client.get_distribution(
            Id = distributionId
        )
        for i in get_distribution_response.get('Distribution').get('DistributionConfig').get('Origins').get('Items'):
            if(bucketName == i.get('DomainName').split('.s3')[0]):
                if(i.get('OriginPath') != ''):
                    print(key.split(i.get('originPath'), 1)[1])
                    print('[Completed check_invalidation_path]')
                    return key.split(i.get('originPath'), 1)[1]
                else:
                    print(key)
                    print('[Completed check_invalidation_path]')
                    return key
    except ClientError as e:
        print('Failed check_invInvalidation_path: {}' . format(e))

##Invalidatoin 생성
def create_invalidation(distributionId, invalidationPath):
    print('[Started create_invalidation]')
    try:
        create_invalidation_response = client.create_invalidation(
            DistributionId = distributionId,
            InvalidationBatch = {
                'Paths': {
                    'Quantity': 1,
                    'Items': [
                        invalidationPath,
                    ]
                },
                'CallerReference': CALLERREFERENCE
            }
        )
        print(create_invalidation_response)
        print('[Completed create_invalidation]')
        return create_invalidation_response
    except ClientError as e:
        print('Failed create_invalidation: {}' . format(e))

##Invalidation 상태 확인
def check_invalidation(distributionId, invalidationId):
    timewait = 0
    status = None
    print('[Started check_invalidation]')
    while 1:
        print('Inprogress Invalidation... {}'.format(timewait))
        try:
            get_invalidation_response = client.get_invalidation(
                DistributionId = distributionId,
                Id = invalidationId
            )
            status = get_invalidation_response.get('Invalidation').get('Status')
            if(status == 'Completed'):
                print(get_invalidation_response)
                print('[Completed Check_Invalidation]')
                return get_invalidation_response
            else:
                timewait += 5
                time.sleep(5)
        except ClientError as e:
            print('Failed check_Invalidation: {}' .format(e))


if __name__ == "__main__":
    start_time = time.time()

    cloudfrontPath = check_invalidation_path(DISTRIBUTIONID, BUCKETNAME, KEY)
    invalidation_response = create_invalidation(DISTRIBUTIONID, '/' + cloudfrontPath)
    invalidation_check_response = check_invalidation(DISTRIBUTIONID, invalidation_response.get('Invalidation').get('Id'))

    print('Completed --- {}seconds ---'.format(time.time() - start_time))
