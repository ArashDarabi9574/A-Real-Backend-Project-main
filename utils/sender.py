import json
import requests

from core.settings import UserApiKeySMS, SecretKeySMS, TEMPLATE_ID_SMS


def sms_sender(number: str, usage: str, **kwargs):
    parameters = []

    for key, value in kwargs.items():
        parameters.append({'Parameter': str(key), 'ParameterValue': str(value)})

    request_data = {
        "Mobile": str(number),
        "TemplateId": str(TEMPLATE_ID_SMS.get(usage)),
        "UserApiKey": str(UserApiKeySMS),
        "SecretKey": str(SecretKeySMS),
        "ParameterArray": parameters,

    }
    response = requests.post(
        url="https://RestfulSms.com/api/UltraFastSend/direct",
        data=json.dumps(request_data),
        headers={"Content-Type": "application/json"}
    )

    print(f'Send SMS for {number} . result :{response.json()}')
