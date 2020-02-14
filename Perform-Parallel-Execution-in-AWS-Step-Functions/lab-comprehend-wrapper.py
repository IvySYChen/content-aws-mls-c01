import boto3
import json
import urllib.request

comprehend = boto3.client('comprehend')

def lambda_handler(event, context):

    payload = event['Input']['Payload']
    transcriptFileUri = payload['TranscriptFileUri']
    transcriptionJobName = payload['TranscriptionJobName']

    transcriptFile = urllib.request.urlopen(transcriptFileUri)
    transcript = transcriptFile.read()
    transcript = json.loads(transcript)
    transcript_text = transcript['results']['transcripts'][0]['transcript']
    
    response = comprehend.detect_sentiment(
        Text=transcript_text,
        LanguageCode='en'
    )

    sentiment = response['Sentiment']

    return {
        'Sentiment': sentiment,
        'TranscriptionJobName': transcriptionJobName
    }
    
