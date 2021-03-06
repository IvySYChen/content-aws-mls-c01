import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    
    rekognition = boto3.client('rekognition')
    
    suspects = ['suspect1', 'suspect2', 'suspect3']
    results = []

    for suspect in suspects:

        response = rekognition.compare_faces(
            SourceImage={
                'S3Object': {
                    'Bucket': 'ai-demos-02032020',
                    'Name': suspect + '.jpg'
                }
            },
            TargetImage={
                'S3Object': {
                    'Bucket': 'ai-demos-02032020',
                    'Name': 'security-camera.jpg'
                }
            }
        )
    
        if len(response['FaceMatches']) > 0:
            results.append({'suspect' : suspect, 'ismatch' : 'yes', 'Similarity' : response['FaceMatches'][0]['Similarity']})
        elif len(response['UnmatchedFaces']) > 0:
            results.append({'suspect' : suspect, 'ismatch' : 'no'})

    return {
        'statusCode': 200,
        'body': results
    }
